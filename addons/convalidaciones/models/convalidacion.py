from odoo import models, fields, api

class Convalidacion(models.Model):
	_name = 'convalidaciones.convalidacion'
	_rec_name = 'fecha_convalidacion'
	fecha_convalidacion = fields.Date(string="Fecha de convalidacion")
	modulo_id = fields.Many2one(comodel_name='convalidaciones.modulo', string="Modulo")
	alumno_id = fields.Many2one(comodel_name='convalidaciones.alumno', string="Alumno")