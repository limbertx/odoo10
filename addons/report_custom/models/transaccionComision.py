# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import api, fields, models
import json
import logging
from Constantes.ResponseJson import ResponseJson
from Constantes.Constantes import Constantes
from Excepciones.ModelError import ModelError

_logger = logging.getLogger(__name__)

class TransaccionComision(models.Model):
    """
        Clase encargada de guardar las comisiones del sistema web comercial
    """
    _name = 'report_custom.transaccioncomision'
    _description = "Transaccion de comision"
    _rec_name = 'nro_sorteo'

    nro_sorteo = fields.Char(string="Numero de sorteo (web-comercial)")
    fecha = fields.Date(string="Fecha de sorteo")
    monto_total = fields.Float(string="Monto total de sorteo", default=0)
    descripcion = fields.Char(string="Descripcion de Sorteo y Comision")
    trans_comision_ids = fields.One2many(comodel_name="report_custom.transaccioncomisiondet", inverse_name="transaccioncomision_id", string="Detalle de comision")

    @api.model
    def update_transaccion_comision(self, nro_sorteo, fecha_sorteo, monto_total, descripcion, detail):
        """ 
            Metodo que crea la transaccion de las comisiones
            que nos llega desde el sistema web comercial

            Parametros:

            nro_sorteo --- Es el numero de sorteo al que pertenecen las comisiones
            fecha_sorteo --- Es la fecha que se ejecuto el sorteo que sera la fecha del comprobante contable
            monto_total --- Es el monto total de las comisiones
            descripcion --- Es una descripcion sobre el tema del comprobante
            detail_json --- son las comisiones en detalle de acuerdo a los roles de trabajo

        """
    	json_acceptable_string = detail.replace("'", "\"")
    	detail_json = json.loads(json_acceptable_string)
    	# detalle de comision
    	_logger.info("detalle de comision descr")
    	comision_detail = []
    	for data in detail_json:
            #_logger.info("ODOO : " + str(self.get_sistema_trabajo_id(data["sistema_trabajo"])))
            sistema = self._get_sistema_trabajo(data["sistema_trabajo"])
            if not sistema:
                return json.dumps((ResponseJson(Constantes.ERROR_VALIDACION, "No se encuentra sistema de trabajo : " + data["sistema_trabajo"], "ERROR", {})).__dict__)
            else:
                comision_detail.append((0, 0, 
                    {
                        "sistema_trabajo_id": sistema.id,
                        "monto": data["comision"]
                    }))

        comision = {
			"nro_sorteo": nro_sorteo,
			"fecha": fecha_sorteo,
			"monto_total": monto_total,
			"descripcion": descripcion,
			"trans_comision_ids": comision_detail
		}        
        try:

            response = self._createComprobante(nro_sorteo, fecha_sorteo, monto_total, descripcion, detail_json)
            if(response.error == Constantes.ERROR_OK):
                transaccion = self.create(comision)
            else:
                raise ModelError(Constantes.ERROR_VALIDACION, response.message)

            message = "Sistema de trabajo guardado correctamente"            
            return json.dumps((ResponseJson(response.error, response.message, response.status, response.values)).__dict__)
        except ModelError as e:
            _logger.error(":ODOO: " + e.message)
            return json.dumps((ResponseJson(e.expresion, e.message, "ERROR", {})).__dict__)

    def _get_sistema_trabajo(self, sistema_trabajo):
        """
        Metodo que obtiene el sistema de trabajo
        """        
        transaccion = self.env["report_custom.sistematrabajo"]
        model = transaccion.search([("sistema_trabajo", "=", sistema_trabajo)])
        if(len(model)>0):
            return model
        else:
            return None

    def _createComprobante(self, nro_sorteo, fecha_sorteo, monto_total, descripcion, detail_json):
        """
            Metodo que crea un comprobante contable
        """
        comprobante = self.env["account.move"]
        
        # primero creamos los detalles
        account_move_lines = []
        ref_encabezado = "NRO SORTEO : " + str(nro_sorteo) + " - " + descripcion
        for data in detail_json:
            sistema_trabajo = self._get_sistema_trabajo(data["sistema_trabajo"])
            if (not sistema_trabajo.account_id) or (not sistema_trabajo.account_against_id):
                return ResponseJson(Constantes.ERROR_FAIL, "Sistema de trabajo : " + sistema_trabajo.descripcion + " no tiene cuenta contable. (Consulte con su contador)", "ERROR", {})
            else:
                account_move_lines.append((0, 0, self._get_move_line(fecha_sorteo, data["comision"], sistema_trabajo.account_id.id, True, ref_encabezado)))
                account_move_lines.append((0, 0, self._get_move_line(fecha_sorteo, data["comision"], sistema_trabajo.account_against_id.id, False, ref_encabezado)))

        account_move = {
            "name" : "/", # al ser draf todavia no tiene nombre
            "state" : "draft", # Quiere decir que el comprobante falta consolidar
            "ref" : ref_encabezado, # referencia
            "company_id" : self.env.user.company_id.id, # es id de la compañia
            "journal_id" : self._getConfigTransDiario(), # id diario  nesecitamos obtenerlo
            "currency_id" : self._getConfigTransMoneda(), # es el id de la moneda
            "amount" : monto_total , # es el monto total
            "matched_percentage" : 1, # ??? 1 si no hay cuentas por pagar caso contrario 0 :: mejor verificar mas profunfamente esta parte
            "narration" : False, # Nota internal
            "date" : fecha_sorteo, # Fecha del comprobante
            "partner_id" : self._getConfigPartner(), # self._getConfigPartner(), # es id de la empresa que realiza la transaccion
            "statement_line_id" : False, # Línea de estado de cuenta bancaria reconciliada con esta entrada
            "line_ids": account_move_lines
        }
    
        _logger.info(json.dumps(account_move))
        transaccion = comprobante.create(account_move)    

        try:                        
            if(len(transaccion) <= 0):                
                return ResponseJson(Constantes.ERROR_FAIL, "No se pudo ejecutar transaccion", "ERROR", {})
            else:
                return ResponseJson(Constantes.ERROR_OK, "Transaccion ejecutada correctamente", "OK", {"id":transaccion.id})
            _logger.info("ODOO:: HA OCURRIDO UN ERROR X2")
        except ValidationError as ex:
            _logger.info("ODOO:: ERROR DE VALIDACION" + ex.message)
            return ResponseJson(Constantes.ERROR_FAIL, ex.message, "ERROR", {})
        except Exception as e:            
            _logger.info("ODOO:: HA OCURRIDO UN ERROR" + e.message)
            return ResponseJson(Constantes.ERROR_FAIL, e.message, "ERROR", {})

    def _get_move_line(self, fecha_sorteo, comision, account_id, is_debito, ref_encabezado):
        """Devuelve un diccionario con el detalle del comprobante

        Parametros:
        fecha_sorteo --- Es la fecha de la realizacion del sorteo
        comision     --- Es la comision que se gana en el sorteo
        account_id   --- Identificador de la cuenta contable
        is_debito    --- True si se carga al debito :: Falso si se carga al credito

        """
        # Cuenta del sorteo
        account_move_line = {
            "statement_id" : False, # None puede ser nulo para la bd
            "journal_id" : self._getConfigTransDiario(), # el es id del diario
            "currency_id" : False, # por defecto esta vacio
            "date_maturity" : fecha_sorteo, # fecha de vencimiento :: por defecto la misma del comprobante
            "user_type_id" : self._getTypeAccount(account_id), # Esto es user_type_id que esta en account.account es account.account.type
            "partner_id" : self._getConfigPartner(), # id de la empresa que se esta ejecutando
            "blocked" : False, # por defecto en falso (sin seguimiento)
            "analytic_account_id" : False, # no tenemos cuenta analitica todavia
            "full_reconcile_id" : False, # en las pruebas salia vacio en la BD, en seguimiento
            "amount_residual" : 1, #??? esto no esta bien por el momento , verificar como funciona
            "company_id" : self.env.user.company_id.id, # id de la empresa
            "credit_cash_basis" : 0 if is_debito else comision, # lo mismo que el credito (CERO si ya esta en el debito)
            "amount_residual_currency" : 0,# ???? no se como se calcula
            "debit" : comision if is_debito else 0, # debito (ej: digamos q es una cuenta que va al debito)
            "ref" : ref_encabezado, # es la referencia del account.move.line (lo dejaremos vacio)
            "account_id" : account_id, # id de la cuenta contable
            "debit_cash_basis" : comision if is_debito else 0, # igual al debito (es decir comision)
            "reconciled" : False, # por defecto falso
            "tax_exigible" : True, # por defecto true
            "balance_cash_basis" : comision if is_debito else (comision * -1), # si es credito va como negativo : debito va como positivo
            "date" : fecha_sorteo, # es la fecha del comprobante contable
            #"move_id" : -1, # id del encabezado account.move (no se ingresa ya q se va generar automaticamente)
            "product_id" : False, # por defecto vacio
            "payment_id" : False, # por defecto vacio
            "company_currency_id" : self.env.user.company_id.currency_id.id, # company_id.currency_id idcurrency de res.company es la moneda del documento
            "name" : ref_encabezado, # glosa del detalle por defecto en vacio la tendre!!
            "invoice_id" : False, # factura :: vacio por defecto
            "tax_line_id" : False, # impuesto :: vacio por defecto
            "credit" : 0 if is_debito else comision, # si ya esta el debito
            "product_uom_id" : False, # vacio por defecto
            "amount_currency" : 0, # ??? CERO por defecto (no se cuando cambia ni idea)
            "balance" : comision if is_debito else (comision * -1), # si es credito va como negativo : debito va como positivo
            "quantity" : False, # vacio por defecto (creo que se lo usa cuando se realizan las ventas de productos que seria la cantidad)
        }
        return account_move_line


    def _getConfigTransDiario(self):
        """
            metodo que retorna el id del diario de transaccion
            para la creacion del comprobante contable
        """
        conftrans = self.env['report_custom.conftransaccion']
        conftrans1 = conftrans.search([("estado", "=", "activo")], limit=1)
        _logger.info("ODOO : id de diario : " + str(conftrans1.diario_id))
        return conftrans1.diario_id.id

    def _getConfigTransMoneda(self):
        """
            metodo que retorna el id de la moneda en la 
            que se esta realizando las transacciones del sistema
        """
        conftrans = self.env['report_custom.conftransaccion']
        conftrans1 = conftrans.search([("estado", "=", "activo")], limit=1)
        _logger.info(":ODOO : id moneda : " + str(conftrans1.moneda_id))
        return conftrans1.moneda_id.id

    def _getConfigPartner(self):
        """
            Metodo que retorna el id de la empresa de cual es el comprobante

        """
        conftrans = self.env['report_custom.conftransaccion']
        conftrans1 = conftrans.search([("estado", "=", "activo")], limit=1)
        print("id socio : " + str(conftrans1.partner_id))
        return conftrans1.partner_id.id

    def _getTypeAccount(self, account_id):
        """
            Metodo que devuelve el tipo de cuenta contable

            Parametros:
            account_id --- Identificador primario de la cuenta contable
        """
        account = self.env["account.account"]
        account1 = account.search([("id" , "=", account_id)], limit=1)
        print(" id type de cuenta" + str(account1.user_type_id))
        return account1.user_type_id.id        