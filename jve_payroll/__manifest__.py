# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'JVE Sénégal',
    'version': '1.0.0',
    'category': 'Systéme d\'informations Ressources humaines',
    'summary': 'JVE Sénégal est une organisation à but non lucratif de la société civile qui joue un rôle essentiel dans la préservation de l\'environnement et la promotion du développement durable au Sénégal.',

    'author': "BSL",
    'website': "https://jvesenegal.org/",

    'description': """
Accélérer la transformation numérique sociétale et environnementale de l’Afrique par des services innovants et créateurs de valeurs.
    """,
    'depends': ['hr_payroll', 'hr', 'hr_contract'],

    'assets': {
        'web.assets_qweb': [
        ],
    },

    'data': [
        'security/ir.model.access.csv',
        #'security/security.xml',
        'report/jve_report_bulletin.xml',
        'report/jve_livre_paie.xml',
        #'report/nrt_cotisation_sociale.xml',
        #'report/nrt_retenues_fiscales.xml',
        #'report/nrt_report_fichier_controle.xml',
        'views/jve_contract_view.xml',
        'views/jve_payslip_view .xml',
        'views/jve_employee_view.xml',
        'views/template_header_body.xml',
        # 'views/template_custom_footer.xml',
        'wizard/view_jve_batch_payroll.xml'
    ],
    'installable': True,
    'auto_install': False,

    'license': 'LGPL-3',
}
