# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ConfTransaccion(models.Model):
    _name = 'report_custom.conftransaccion'
    _description = "Configuracion de transaccion"
    _rec_name = 'diario_id' # lo que esta aqui sale arriba del list

    diario_id = fields.Many2one('account.journal', string='Diario de transaccion', required=True)
    moneda_id = fields.Many2one('res.currency', string="Moneda de transaccion", required = True)
    estado = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')],
                            string='Estado de Confg.',
                            required=True, default="activo")
    partner_id = fields.Many2one("res.partner", string="Empresa", ondelete="restrict")
    det_ids = fields.One2many('report_custom.detconftransaccion', 'conftran_id', string='Detalles de configuracion', copy=True)


class DetConfTransaccion(models.Model):
    _name = 'report_custom.detconftransaccion'
    _description = "Detalle de configuracion"
    _rec_name = "account_id"

    conftran_id = fields.Many2one('report_custom.conftransaccion', string='Detalle', ondelete="cascade",
        help="Detalle de configuracion.", index=True, required=True, auto_join=True)
    account_id = fields.Many2one('account.account', string="Contra Cuenta", ondelete="set null", required=True)
    porcentaje = fields.Float(string="Porcentaje (<1)")
