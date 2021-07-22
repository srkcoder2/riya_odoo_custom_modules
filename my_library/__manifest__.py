# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format

    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '13.0,0.0' ,
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
