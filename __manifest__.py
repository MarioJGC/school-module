# -*- coding: utf-8 -*-
{
    'name': "Sistema de Escuela",

    'summary': "Gestionar información de estudiantes, profesores y cursos.",

    'description': """
        Sistema creado para la gestion escolar de estudiantes, profesores y cursos.
    """,

    'author': "Mario Jarod Grande Contreras",
    'website': "www.linkedin.com/in/mjgc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'views/school_teacher_view.xml',
        'views/school_student_view.xml',
        'views/school_subject_view.xml',
        'views/menu_item_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

