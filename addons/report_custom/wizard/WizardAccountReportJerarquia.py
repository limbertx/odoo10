# -*- coding: utf-8 -*-
# modelo que representa los datos del formulario
import logging
from odoo import fields, models, api, _

_logger = logging.getLogger(__name__)

class WizardAccountReportJerarquia(models.TransientModel):
    _name = "report_custom.wizard_account_report_jerarquia"
    _description = "Cuentas contables con jerarquia"
    fecha_ini = fields.Date(string='Fecha Inicial')
    fecha_fin = fields.Date(string="Fecha Final")

    @api.multi
    def action_report(self):
        #metodo que llama a la logica que genera el metodo
        _logger.info(':CONT_ODOO: entre a la accion action reporte')

        datas = {'ids': self.env.context.get('active_ids', [])}

        # lee los datos de la clase actual y los guarda en "res"
        res = self.read(['fecha_ini', 'fecha_fin'])

        res = res and res[0] or {}
        datas['form'] = res

        domain = []

        # si la fecha ini contiene algo :: 
        # que nos muestre solo las cuentas que fueron creadas menores a fecha_ini
        if self.fecha_ini:
            domain=[('create_date', '<', self.fecha_fin)]

        # los datos que queremos mostrar de la tabla accountaccount
        fields=['id', 'code', 'name', 'internal_type']

        #busco dentro de la tabla account_account ::: devuelve un diccionario
        account_data = self.env['account.account'].search_read(domain, fields)

        datas['account_data'] = account_data
        _logger.info(':CONT_ODOO XXD: llegue hasta aqui!!')

        return self.env['report'].get_action([], 'report_custom.account_report_jerarquia_view', data=datas)