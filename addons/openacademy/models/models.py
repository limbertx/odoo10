# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
	_name = 'openacademy.course'
	name = fields.Char(string="Nombre de Curso", required=True)
	description = fields.Text(string="Descripcion del curso")