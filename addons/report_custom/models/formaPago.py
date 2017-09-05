# -*- coding: utf-8 -*-

from odoo import api, fields, models

class FormaPago(models.Model):
    _name = 'report_custom.formapago'
    _description = "Forma de pago"
    _rec_name = 'descripcion' # lo que esta aqui sale en la descripcion

    descripcion = fields.Char(string = "Forma de pago")
    abrevi = fields.Char(string = "Abreviatura")
