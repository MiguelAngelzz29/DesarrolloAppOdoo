# -*- coding: utf-8 -*-
{
    'name': "Garantia",  # Module title
    'summary': "Tramitar garantias",  # Module subtitle phrase
    'description': """
      Modulo para tramitar garantias
    """,  # Supports reStructuredText(RST) format
    'author': "Miguel Angel",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '15.0.1',
    'depends': ['base'],

    'data': [
    #    'security/groups.xml',
      #  'security/ir.model.access.csv',
        'views/garantia.xml',
       'views/garantia_categoria.xml',
       'reports/reportes_garantia.xml'
    ],

    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
     'installable': True,
    'application': True,
}



