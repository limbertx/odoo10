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
    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/account_report_libro_diario.xml', # vista de libro diario heredado
        #'views/account_common_report_view.xml',
        # plan contable
        #'views/accountReportJerarquia_form.xml',
        #'views/accountReportJerarquia_view.xml',
        "views/formapago_view.xml"
    ],
}