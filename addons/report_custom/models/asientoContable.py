# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AsientoContable(models.Model):
    _name = 'report_custom.asientocontable'
    _inherit = "account.move"
