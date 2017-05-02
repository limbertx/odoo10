# -*- coding: utf-8 -*-
{
    'name': "Parent Account",
    'summary': """
        Adds Parent account and ability to open chart of account list view based on the date and moves""",
    'description': """
This module will be very useful for those who are still using v7/v8 because of the no parent account and chart of account heirarchy view in the latest versions
        * Adds parent account in account
        * Adds new type 'view' in account type
        * Adds Chart of account heirachy view
        * Adds credit, debit and balance in account
        * Shows chart of account based on the date and target moves we have selected
    - Need to set the group show chart of account structure to view the chart of account heirarchy.
    
    """,

    'author': '',
    'website': 'http://www.google.com',
    'category': 'Accounting &amp; Finance',
    'version': '1.2.1',
    'depends': ['account'],
    'data': [
        'security/account_parent_security.xml',
        'views/account_view.xml',
        'views/open_chart.xml',
        'data/account_type_data.xml',
    ],
    'demo': [
    ],
}