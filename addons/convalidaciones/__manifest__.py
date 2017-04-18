# -*- coding: utf-8 -*-
{
    'name': "convalidaciones",

    'summary': """
        Encargado de realizar las convalidaciones del sistema""",

    'description': """
        Es un modulo que se encarga de las descripciones del sistema
    """,

    'author': "Yalusqui ayuda!",
    'website': "http://www.google.com.bo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/alumnos.xml',
        'views/modulos.xml',
        'views/ciclos.xml',
        'views/convalidaciones.xml',
    ],
}