from odoo import fields, models

class Account_report_libro_diario(models.TransientModel):
    _inherit = "account.print.journal"
    _name = "report_custom.account_report_libro_diario"
    _description = "Libro diario de asientos contables"

    sort_selection = fields.Selection([('date', 'Date'), ('move_name', 'Journal Entry Number'),], 'Entries Sorted by', required=True, default='move_name')
	#cambio que se modifico para el reporte diario     
    #journal_ids = fields.Many2many('account.journal', string='Journals', required=True, default=lambda self: self.env['account.journal'].search([('type', 'in', ['sale', 'purchase'])]))
    journal_ids = fields.Many2many('account.journal', string='Journals', required=True)
    def _print_report(self, data):
        data = self.pre_print_report(data)
        data['form'].update({'sort_selection': self.sort_selection})
        return self.env['report'].with_context(landscape=True).get_action(self, 'account.report_journal', data=data)
