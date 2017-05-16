# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
# TransientModel
class accountlibromayform(models.TransientModel):
	_name = "report_custom.accountlibromayform"
	_description = "Libro Mayor"
	select_nivel = fields.Selection([('1', 'nivel 1'), ('2', 'nivel 2'),('3', 'nivel 3')], string="Seleccione nivel de informe", required=True, select=True)
	account_id = fields.Many2one("account.account", string="Cuenta Contable")
	fecha_ini = fields.Date(string='Fecha Inicial')
	fecha_fin = fields.Date(string='Fecha Final')

#modelo para la consulta sql del informe
class accountlibromayquery(models.TransientModel):
	_name = "report_custom.accountlibromayquery"
	_description = "Consulta query de libro mayor"
