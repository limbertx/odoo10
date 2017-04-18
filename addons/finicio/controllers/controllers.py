# -*- coding: utf-8 -*-
from odoo import http

# class Finicio(http.Controller):
#     @http.route('/finicio/finicio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/finicio/finicio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('finicio.listing', {
#             'root': '/finicio/finicio',
#             'objects': http.request.env['finicio.finicio'].search([]),
#         })

#     @http.route('/finicio/finicio/objects/<model("finicio.finicio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('finicio.object', {
#             'object': obj
#         })