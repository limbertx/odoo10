# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Sorteo(models.Model):
    _name = 'report_custom.sorteo'
    _description = "Sorteos"
    _rec_name = 'descripcion' # lo que esta aqui sale en la descripcion

    idsorteo = fields.Integer(string="Identificador (web-comercial)")
    descripcion = fields.Char(string = "Descripcion de sorteo")
