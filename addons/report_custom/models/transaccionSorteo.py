# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TransaccionSorteo(models.Model):
    _name = 'report_custom.transaccionsorteo'
    _description = "Transacciones de Sorteo"
    _rec_name = "fecha_cierre"

    fecha_cierre = fields.Date(string = "Fecha de Cierre", required=True, help="Fecha del cierre del sorteo")
    venta_efect = fields.Float(string="Venta Efectiva", required=True, help="Monto Efectivo total")
    comision = fields.Float(string="Comision (%)", required=True, help="Comision que se cobra por el sorteo")
    juego_id = fields.Many2one("report_custom.juego", string="Juego")
    sorteo_id = fields.Many2one("report_custom.sorteo", string="sorteo")
    # juego = fields.Char(string="Nombre de juego")
    #sorteo = fields.Char(string="Nro de sorteo") #ej: nro 1, 2, 3, 4....
    direct_dpto = fields.Char(string="Director departamental")
    fecha_sorteo = fields.Date(string="Fecha de sorteo", required=True, help="Fecha de sorteo")
    glosa = fields.Char(string="Glosa detalle", help="Es la descripcion de la operacion")
    concepto = fields.Char(string="Concepto de asiento contable")
    pais = fields.Char(string="Pais de origen", help="Pais donde se origina el comprobante")
    departamento = fields.Char(string="Departamento de origen", help="Departamento donde se origina el comprobante")

    @api.model
    #def createtransaccion(self, fecha_cierre, venta_efect, comision, juego, sorteo, direct_dpto, fecha_sorteo, glosa, concepto, pais, departamento):
    def createtransaccion(self, fecha_cierre, venta_efect, comision, juego_id, juego, sorteo_id, sorteo, direct_dpto, fecha_sorteo, glosa, concepto, pais, departamento):
        transaccion = self.env['report_custom.transaccionsorteo']
        idTransaccion = transaccion.create({
                                            "fecha_cierre" : fecha_cierre,
                                            "venta_efect" : venta_efect,
                                            "comision" : comision,
                                            "juego_id" : 1, # por ahora en defecto 1
                                            "sorteo_id" : 1, # por ahora en defecto 1
                                            "direct_dpto" : direct_dpto,
                                            "fecha_sorteo" : fecha_sorteo,
                                            "glosa" : glosa,
                                            "concepto" : concepto,
                                            "pais" : pais,
                                            "departamento" : departamento
                                            })
        #if(idTransaccion >0):
            #generamos un comprobante contable
            #idComprobante = 0 #self._createComprobante()
        print(idTransaccion.id)
        return (str(idTransaccion.id))
    # def _createComprobante(self):
    #     comprobante = self.env["account.move"]
    #     dctMove = {
    #         "name" : "/", # al ser draf todavia no tiene nombre
    #         "state" : "draft", # Quiere decir que el comprobante falta consolidar
    #         "ref" : self.concepto, # referencia
    #         "company_id" : self.env.user.company_id, # es id de la compañia
    #         "journal_id" : self._getConfigTransDiario(), # id egreso nesecitamos obtenerlo
    #         "currency_id" : self._getConfigTransMoneda(), # es el id de la moneda
    #         "amount" : (self.comision * self.venta_efect), # es el monto total
    #         "matched_percentage" : 0, # ???????
    #         "narration" : "", # Nota internal
    #         "date" : self.fecha_cierre, #fecha del comprobante
    #         "partner_id" : self._getConfigTransMoneda(), # es id de la empresa que realiza la transaccion
    #         "statement_line_id" : "" # Línea de estado de cuenta bancaria reconciliada con esta entrada
    #     }
    #     print(dctMove.items())
    # # metodo que devuelve el diccionario con los items detalle
    # def _getItems(self):
    #     # Cuenta del sorteo
    #     dtc1 = {
    #         "statement_id" : False, # None puede ser nulo para la bd
    #         "journal_id" : self._getConfigTransDiario(), # el es id del diario
    #         "currency_id" : False, # por defecto esta nulo
    #         "date_maturity" : self.fecha_cierre, # igual a la fecha del comprobante
    #         "user_type_id" : self._getTypeAccount(self._getConfigCuenta_inv()), # Esto es user_type_id que esta en account.account
    #         "partner_id" : 0,
    #         "blocked" : False,
    #         "analytic_account_id" : ,
    #         "full_reconcile_id" : ,
    #         "amount_residual" : 100,
    #         "company_id" : 1, # id de la empresa
    #         "credit_cash_basis" : 1111,
    #         "amount_residual_currency" : 0,
    #         "debit" : 2000, # debito
    #         "ref" : "", # es la referencia del account.move
    #         "account_id" : 1, # id de la cuenta contable
    #         "debit_cash_basis" : 2000, # igual al debito
    #         "reconciled" : False, # por defecto falso
    #         "tax_exigible" : True, # por defecto true
    #         "balance_cash_basis" : -2000, # si es credito va como negativo : debito va como positivo
    #         "date" : "2017-02-02", # es la fecha del comprobante contable
    #         "move_id" : -1, # id del encabezado account.move
    #         "product_id" : , # por defecto vacio
    #         "payment_id" : , # por defecto vacio
    #         "company_currency_id" : 2, # idcurrency de res.company
    #         "name" : 2, # glosa del detalle
    #         "invoice_id" : , # factura :: vacio por defecto
    #         "tax_line_id" : , # impuesto :: vacio por defecto
    #         "credit" : 0, # si ya esta el debito
    #         "product_uom_id" : , # vacio por defecto
    #         "amount_currency" : 0, # CERO por defecto
    #         "balance" : -2000, # si es credito va como negativo : debito va como positivo
    #         "quantity" : , # vacio por defecto
    #     }
    #
    # # metodo que retorna el id del diario de transaccion
    # def _getConfigTransDiario(self):
    #     conftrans = self.env['report_custom.conftransaccion']
    #     conftrans1 = conconftrans.search([("estado", "=", "activo")], limit=1)
    #     print("estado : " + conftrans1.estado)
    #     return conftrans1.diario_id
    #
    # def _getConfigTransMoneda(self):
    #     conftrans = self.env['report_custom.conftransaccion']
    #     conftrans1 = conconftrans.search([("estado", "=", "activo")], limit=1)
    #     print("id moneda : " + conftrans1.estado)
    #     return conftrans1.moneda_id
    #
    # def _getConfigParner(self):
    #     conftrans = self.env['report_custom.conftransaccion']
    #     conftrans1 = conconftrans.search([("estado", "=", "activo")], limit=1)
    #     print("id socio : " + conftrans1.partner_id)
    #     return conftrans1.partner_id
    #
    # # devuelve el id de la cuenta inversa
    # def _getConfigCuenta_inv(self):
    #     conftrans = self.env['report_custom.conftransaccion']
    #     conftrans1 = conconftrans.search([("estado", "=", "activo")], limit=1)
    #     print("id cuenta inversa : " + conftrans1.estado)
    #     return conftrans1.account_inv_id
    #
    # # devuelve el id del tipo de cuenta contable
    # def _getTypeAccount(self, account_id):
    #     account = self.env["account.account"]
    #     account1 = account.search(["id" , "=", account_id], limit=1)
    #     print(" id type de cuenta" + account1.user_type_id)
