from odoo import models, fields

class Ciclo(models.Model):
	_name = 'convalidaciones.ciclo'
	_rec_name = 'nombre'

	nombre = fields.Char(string="Nombre del ciclo")
	descripcion = fields.Text(string="Descripcion")
	modulo_ids = fields.Many2many(comodel_name="convalidaciones.modulo")