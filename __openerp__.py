# -*- coding: utf-8 -*-
{
    'name': "Sparkit M&E Data Checking Module",

    'summary': """
        Data checking and verification module for SparkIt M&E Users.""",

    'description': """
        Wizards to check the Visit Report Forms, Community Profile
    """,

    'author': "Spark MicroGrants",
    'website': "http://www.sparkmicrogrants.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sparkit'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/vrf_verification_wizard_views.xml',
    ],

}
