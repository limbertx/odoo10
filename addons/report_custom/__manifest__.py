# -*- coding: utf-8 -*-
{
    'name': "Reportes sistema contable odoo",

    'summary': """
        Modulo de reporte del sistema contable con jerarquia""",

    'description': """
        Modulo de reportes del sistema contable, con jerarquia
    """,

    'author': "odoo 10",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
        #'views/account_report_libro_diario.xml',
    ],
}