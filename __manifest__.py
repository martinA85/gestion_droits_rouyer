# -*- coding: utf-8 -*-
{
    'name': "Gestion de droit Rouyer",

    'summary': """
        Gestion de droit Royer auto""",

    'description': """
        Gestion des droits pour le Client rouyer auto
    """,

    'author': "NOOSYS",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','brand_model_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "security/security.xml",
        'views/res_users_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}