# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
# TransientModel
class accountlibrodiarioform(models.TransientModel):
	_name = "report_custom.accountlibrodiarioform"
	_description = "Libro diario contable"
	fecha_ini = fields.Date(string='Fecha Inicial', required=True)
	fecha_fin = fields.Date(string='Fecha Final', required=True)
	diarios_ids = fields.Many2many('account.journal', string='Diarios', required=True, default=lambda self: self.env['account.journal'].search([]))

	@api.multi
	def check_report(self):
		self.ensure_one()
		data = {}
		data['ids'] = self.env.context.get()
class accountlibrodiarioquery(models.TransientModel):
	_name = "report_custom.accountlibrodiarioquery"
	_description = "Consulta query de libro diario"
