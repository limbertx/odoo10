# -*- coding: utf-8 -*-
import logging
from odoo import fields, models, api
from odoo.tools import float_round

_logger = logging.getLogger(__name__)

class AccountReportJerarquia(models.AbstractModel):
    _name = "report.report_custom.account_report_jerarquia_view"

    @api.model
    def render_html(self, docids, data=None):
        data = data if data is not None else {}
        accounts = self.env["account.account"].browse(data.get('ids', data.get('active_ids')))
        docargs = {
            'doc_ids' : data.get('ids', data.get('active_ids')),
            'doc_model' : 'account.account',
            'docs' : accounts,
            'data' : dict(data),
        }

        return self.env['report'].render("report_custom.accountReportJerarquia_template", docargs)