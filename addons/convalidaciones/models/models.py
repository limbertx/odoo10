# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alumno(models.Model):
	_name = 'convalidaciones.alumno'
	_rec_name = 'nombre'

	nombre = fields.Char(string="Nombre y apellidos")
	edad = fields.Integer(string="Edad")
	localidad = fields.Char(string="Localidad")
	provincia = fields.Char(string="Provincia")
	email = fields.Char(string="Correo Electronico")
	convalidacion_ids = fields.One2many(comodel_name="convalidaciones.convalidacion", inverse_name="alumno_id", string="Convalidaciones del Alumno")
	# esto es para usar una tabla del modulo odoo
	pais_id = fields.Many2one('res.country', string="Pais de origen")