{
    'name': 'Cuba Report ejemplo',    
    'summary': 'Ejemplo de un módulo de Odoo',
    'description': """
Es un módulo de ejemplo
Nota: Necesita Ventas.
    """,
    'author': 'Limbert Yalusqui',
    'website': 'https://github.com/limbertx/',
    'category': 'Accounting & Finance',
    'version': '1.0',

    #'sequence': 30,     
    'license' : 'AGPL-3',

    'depends': ['account','base','report'],

    'data': [
        'diario_report_view.xml',
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
}	