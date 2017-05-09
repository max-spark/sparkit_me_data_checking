# -*- coding: utf-8 -*-
from openerp import http

# class SparkitMeDataChecking(http.Controller):
#     @http.route('/sparkit_me_data_checking/sparkit_me_data_checking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sparkit_me_data_checking/sparkit_me_data_checking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sparkit_me_data_checking.listing', {
#             'root': '/sparkit_me_data_checking/sparkit_me_data_checking',
#             'objects': http.request.env['sparkit_me_data_checking.sparkit_me_data_checking'].search([]),
#         })

#     @http.route('/sparkit_me_data_checking/sparkit_me_data_checking/objects/<model("sparkit_me_data_checking.sparkit_me_data_checking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sparkit_me_data_checking.object', {
#             'object': obj
#         })