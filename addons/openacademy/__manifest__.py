# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Desarrollo de modulos y paquetes en python odoo""",

    'description': """
        Es un modulo creado para las pruebas
    """,

    'author': "yalusqui",
    'website': "http://www.yalusqui.com",

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
        'views/openacademy.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}