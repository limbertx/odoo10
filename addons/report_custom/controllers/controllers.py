# -*- coding: utf-8 -*-
from odoo import http

# class ReportCustom(http.Controller):
#     @http.route('/report_custom/report_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_custom/report_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_custom.listing', {
#             'root': '/report_custom/report_custom',
#             'objects': http.request.env['report_custom.report_custom'].search([]),
#         })

#     @http.route('/report_custom/report_custom/objects/<model("report_custom.report_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_custom.object', {
#             'object': obj
#         })