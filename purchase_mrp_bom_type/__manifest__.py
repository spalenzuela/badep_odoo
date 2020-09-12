{
    'name': 'Purchase MRP Separate BOM Type',
    'author': 'BADEP',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
Allow to define a bom type for purchases different than that of sales
    """,
    'depends': ['purchase_mrp'],
    'data': [
        'views/bom_views.xml'
    ],
    'Installable': False,
    'auto_install': True,
}
