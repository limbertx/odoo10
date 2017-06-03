# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ConfTransaccion(models.Model):
    _name = 'report_custom.conftransaccion'
    _description = "Configuracion de transaccion"
    _rec_name = 'account_inv_id' # lo que esta aqui sale arriba del list

    diario_id = fields.Many2one('account.journal', string='Diario de transaccion', required=True)
    moneda_id = fields.Many2one('res.currency', string="Moneda de transaccion", required = True)
    account_inv_id = fields.Many2one('account.account', string="Contra Cuenta", ondelete="set null", required=True)
    estado = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')],
                            string='Estado de Confg.',
                            required=True, default="activo")
    partner_id = fields.Many2one("res.partner", string="Empresa", ondelete="restrict")
