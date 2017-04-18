from odoo import models, fields

class Modulo(models.Model):
	_name = 'convalidaciones.modulo'
	_rec_name = 'nombre'
	nombre = fields.Char(string="Nombre del modulo")
	descripcion = fields.Text(string="Descripcion")
	ciclo_ids = fields.Many2many(comodel_name="convalidaciones.ciclo")