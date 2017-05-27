# -*- coding: utf-8 -*-
import logging
from odoo import fields, models, api, _

_logger = logging.getLogger(__name__)

class AccountReportJerarquiaForm(models.TransientModel):
    _name = "report_custom.account.report.jerarquia.form"
    _description = "Cuentas contables con jerarquia"
    fecha_ini = fields.Date(string='Fecha Inicial')
    fecha_fin = fields.Date(string="Fecha Final")

    def _construir_contexts(self, data):
        result = {}
        result['fecha_ini'] = data['form']['fecha_ini'] or False
        result['fecha_fin'] = data['form']['fecha_fin'] or False
        return result


    @api.multi
    def imprimir_informe(self):
        _logger.info(':INFO: nESECTIO AYUDA LIMBERT')
        # Con esto nos aseguramos que se esta enviando un solo registro
        # si hay multiples ocurre un error
        self.ensure_one()
        data = {}
        data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
        data['form'] = self.read(['fecha_ini', 'fecha_fin'])[0]
        used_context = self._construir_contexts(data)
        # por defecto asumimos que los datos se estan enviando en lenguaje ingles
        data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang', 'en_US'))
        _logger.info(':INFO: ANTES DE REPORTE')
        reporte = self.env["report"]
        _logger.info(':INFO: PASE REPORTE')

        value = reporte.get_action(self, 'report_custom.accountreportjerarquia', data=data)
        _logger.error(':INFO: PASE VALUE')
        return value


class AccountReportJerarquia(models.TransientModel):
    _name = "report.report_custom.accountreportjerarquia"
    _template = "report_custom.accountreportjerarquia"
    def consulta():
        return ""

    @api.model
    def render_html(self, docids, data=None):
        docargs = {}
        return self.env['report'].render('report_custom.accountreportjerarquia', docargs)
