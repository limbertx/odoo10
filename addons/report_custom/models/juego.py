# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Juego(models.Model):
    _name = 'report_custom.juego'
    _description = "Juegos"
    _rec_name = 'descripcion' # lo que esta aqui sale en la descripcion

    idjuego = fields.Integer(string="Identificador (web-comercial)")
    descripcion = fields.Char(string = "Descripcion de juego")
