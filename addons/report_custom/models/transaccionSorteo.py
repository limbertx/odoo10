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