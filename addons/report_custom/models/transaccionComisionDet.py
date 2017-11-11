# -*- coding: utf-8 -*-

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)
"""
	Clase encargada de guardar los detalles de comisiones
"""
class TransaccionComisionDet(models.Model):
    _name = 'report_custom.transaccioncomisiondet'
    _description = "Detalle de comision"
    _rec_name = 'sistema_trabajo_id'

    sistema_trabajo_id = fields.Many2one('report_custom.sistematrabajo', string="Sistema de trabajo")
    monto = fields.Float(string="Monto de comision", default=0)
    transaccioncomision_id = fields.Many2one(comodel_name='report_custom.transaccioncomision', string="Transaccion Comision")
    