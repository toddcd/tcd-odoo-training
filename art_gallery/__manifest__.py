# -*- coding: utf-8 -*-
{
    'name': "Art Gallery",

    'summary': """
        Module to collect and sell art.""",

    'description': """
        Module to collect and sell art. Including more details on the art pieces and prices. 
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/art_gallery_menu_items.xml',
        'views/art_gallery_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
#         'demo/demo.xml',
    ],
}
