# -*- coding: utf-8 -*-

from odoo import fields, models


class account_report_libro_diario(models.TransientModel):
    _inherit = "report_custom.account.common.journal.report"
    _name = "report_custom.account_report_libro_diario"
    _description = "*Libros diarios*"

    sort_selection = fields.Selection([('date', 'Fecha'), ('move_name', 'Numero de asiento'),], 'Asientos ordenados por', required=True, default='move_name')
    # journal_ids = fields.Many2many('account.journal', string='Journals', required=True)# sin nada por defecto

    def _print_report(self, data):
        data = self.pre_print_report(data)
        data['form'].update({'sort_selection': self.sort_selection})
        return self.env['report'].with_context(landscape=True).get_action(self, 'account.report_journal', data=data)
