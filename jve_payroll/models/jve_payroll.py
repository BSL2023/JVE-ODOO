from datetime import datetime
import time
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _
from odoo.tools import date_utils
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta


# class PayrollStructureValues(models.Model):
#     _inherit = 'hr.payroll.structure'

#     @api.model
#     def _get_default_rule_ids(self):
#         return [
#             (0, 0, {
#                 'name': _('Salaire de base'),
#                 'sequence': 1,
#                 'code': 'BASIC',
#                 'category_id': self.env.ref('hr_payroll.BASIC').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.salaire_base',
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('Sursalaire'),
#                 'sequence': 2,
#                 'code': 'SURSAL',
#                 'category_id': self.env.ref('hr_payroll.BASIC').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.sursalaire',
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('Accident du travail'),
#                 'sequence': 110,
#                 'code': 'CSSAT',
#                 'category_id': self.env.ref('hr_payroll.COMP').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': """
#                                                 if payslip.salaire_brut<=63000:
#                                                     result=payslip.salaire_brut*0.01
#                                                 elif payslip.salaire_brut > 63000:
#                                                     result=63000*0.01
#                                                 """,
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': 'Allocation familiale',
#                 'sequence': 109,
#                 'code': 'CSSAF',
#                 'category_id': self.env.ref('hr_payroll.COMP').id,
#                 'condition_select': 'none',
#                 'amount_select': 'code',
#                 'amount_python_compute': """
#                                         if payslip.salaire_brut<=63000:
#                                             result=payslip.salaire_brut*0.07
#                                         elif payslip.salaire_brut>63000:
#                                             result=63000*0.07
#                                         """,
#             }),
#             (0, 0, {
#                 'name': 'IPRESS Régime Général Employeur',
#                 'sequence': 107,
#                 'code': 'IPRGEMP',
#                 'struct_id': self.env['hr.payroll.structure'].search([('type_id', '=', 'Général')]),
#                 'category_id': self.env.ref('hr_payroll.COMP').id,
#                 'condition_select': 'none',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.montant_ipress_general_employeur',
#                 # """
#                 #             if payslip.salaire_brut <= 432000:
#                 #                 result = payslip.gross_salary * 0.084
#                 #             elif payslip.salaire_brut > 432000:
#                 #                 result=432000 * 0.084
#                 #             """,
#             }),
#             (0, 0, {
#                 'name': 'IPRESS Régime Cadre Employeur',
#                 'sequence': 107,
#                 'code': 'IPRCEMP',
#                 'struct_id': self.env['hr.payroll.structure'].search([('type_id', '=', 'Cadre')]),
#                 'category_id': self.env.ref('hr_payroll.COMP').id,
#                 'condition_select': 'none',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.montant_ipress_cadre_employeur',
#                 # """
#                 #                     if payslip.salaire_brut <= 1296000:
#                 #                         result = payslip.gross_salary * 0.036
#                 #                     elif payslip.salaire_brut > 1296000:
#                 #                         result=1296000 * 0.036
#                 #                     """,
#             }),
#             (0, 0, {
#                 'name': _('Impôt sur le revenu'),
#                 'sequence': 104,
#                 'code': 'ISR',
#                 'category_id': self.env.ref('hr_payroll.DED').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.impot_revenu',
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('TRIMF'),
#                 'sequence': 105,
#                 'code': 'TRIMF',
#                 'category_id': self.env.ref('hr_payroll.DED').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.trimf',
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('IPRESS Régime Général Employé'),
#                 'sequence': 102,
#                 'code': 'IPRGEMPLOYE',
#                 'struct_id': self.env['hr.payroll.structure'].search([('type_id', '=', 'Général')]),
#                 'category_id': self.env.ref('hr_payroll.DED').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.montant_ipress_general_employee'
#                 # """
#                 #             if payslip.salaire_brut <= 432000:
#                 #                 result = payslip.salaire_brut * 0.056
#                 #             elif payslip.salaire_brut > 432000:
#                 #                 result = 432000 * 0.056
#                 #             """,
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('IPRESS Régime Cadre Employé'),
#                 'sequence': 102,
#                 'code': 'IPRCEMPLOYE',
#                 'struct_id': self.env['hr.payroll.structure'].search([('type_id', '=', 'Cadre')]),
#                 'category_id': self.env.ref('hr_payroll.DED').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.montant_ipress_cadre_employe',
#                 # """
#                 #                     if payslip.salaire_brut <= 1296000:
#                 #                         result = payslip.salaire_brut * 0.024
#                 #                     elif payslip.salaire_brut > 1296000:
#                 #                         result = 1296000 * 0.024
#                 #                     """,
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('Prime de transport'),
#                 'sequence': 3,
#                 'code': 'PRIME',
#                 'category_id': self.env.ref('hr_payroll.BASIC').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.prime_transport',
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('Indemnité de téléphone'),
#                 'sequence': 3,
#                 'code': 'PRIME',
#                 'category_id': self.env.ref('hr_payroll.BASIC').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.indemn_telephone',
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': _('Indemnité de fonction'),
#                 'sequence': 3,
#                 'code': 'PRIME',
#                 'category_id': self.env.ref('hr_payroll.BASIC').id,
#                 'condition_select': 'none',
#                 # 'amount_select': 'fix',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.indemn_fonction',
#                 # 'amount_fix': 0.0,
#             }),
#             (0, 0, {
#                 'name': 'Total cotisation employé',
#                 'sequence': 106,
#                 'code': 'TCEMPYE',
#                 'category_id': self.env.ref('hr_payroll.DED').id,
#                 'condition_select': 'none',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.total_cotisation_employe',
#             }),
#             (0, 0, {
#                 'name': 'Total cotisation employeur',
#                 'sequence': 106,
#                 'code': 'TCEMPYEUR',
#                 'category_id': self.env.ref('hr_payroll.DED').id,
#                 'condition_select': 'none',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.total_cotisation_employeur',
#             }),
#             (0, 0, {
#                 'name': 'Salaire Net',
#                 'sequence': 200,
#                 'code': 'NET',
#                 'category_id': self.env.ref('hr_payroll.NET').id,
#                 'condition_select': 'none',
#                 'amount_select': 'code',
#                 'amount_python_compute': 'result = payslip.salaire_net',
#             })
#         ]

#     rule_ids = fields.One2many(
#         'hr.salary.rule', 'struct_id',
#         string='Salary Rules', default=_get_default_rule_ids)


class PayrollValues(models.Model):
    _inherit = 'hr.payslip'

    # pret_nature = fields.Many2one("hr.loan", string="Prêt en nature")
    contract_id = fields.Many2one(
        'hr.contract', string='Contract', domain="[('company_id', '=', company_id)]",
        compute='_compute_contract_id', store=True, readonly=False,
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)], 'paid': [('readonly', True)]})
    salaire_base = fields.Integer('Salaire de base', compute='_compute_salaire', store=True)
    sursalaire = fields.Integer('Sursalaire', compute='_compute_salaire', store=True)
    impot_revenu = fields.Integer('Impôt sur le revenu', compute='_compute_impot_mensuel', store=True)
    base_fiscal_abatt = fields.Integer('Base fiscale après abattement', compute='_compute_impot_mensuel', store=True)
    indemnite_transport = fields.Integer('Indemnité de transport', compute='_compute_salaire', store=True)
    indemn_preavis = fields.Integer('Indemnité de préavis', compute='_compute_salaire', store=True)
    salaire_net = fields.Integer('Salaire net', compute='_compute_cotisation', store=True)
    total_cotisation = fields.Integer('Total des cotisations', compute='_compute_cotisation', store=True)
    salaire_brut = fields.Integer('Salaire brut', compute='_compute_salaire', store=True)
    taux_ipress_general_employe = fields.Float("Taux ipress régime général employé", compute="_compute_cotisation",
                                               store=True)
    regime_general_employe_employeur = fields.Integer("Montant ipress régime général employé employeur",
                                                      compute="_compute_cotisation", store=True)
    regime_cadre_employe_employeur = fields.Integer("Montant ipress régime cadre employé employeur",
                                                    compute="_compute_cotisation", store=True)
    caisse_ss = fields.Integer("Caisee de sécurité sociale",
                               compute="_compute_cotisation", store=True)
    montant_ipress_general_employee = fields.Integer("Montant ipress régime général employé",
                                                     compute="_compute_cotisation", store=True)
    taux_ipress_general_employeur = fields.Float("Taux ipress régime général employeur", compute="_compute_cotisation",
                                                 store=True)
    montant_ipress_general_employeur = fields.Integer("Montant ipress régime général employeur",
                                                      compute="_compute_cotisation", store=True)
    taux_ipress_cadre_employe = fields.Float("Taux ipress régime cadre employé", compute="_compute_cotisation",
                                             store=True)
    montant_ipress_cadre_employe = fields.Integer("Montant ipress régime cadre employé", compute="_compute_cotisation",
                                                  store=True)
    taux_ipress_cadre_employeur = fields.Float("Taux ipress régime cadre employeur", compute="_compute_cotisation",
                                               store=True)
    montant_ipress_cadre_employeur = fields.Integer("Montant ipress régime cadre employeur",
                                                    compute="_compute_cotisation", store=True)
    base_calcul_ipress_cadre = fields.Integer("Base de calcul pour les cotisations cadre",
                                              compute="_compute_cotisation", store=True)
    base_calcul_ipress_general = fields.Integer("Base de calcul pour les cotisations général",
                                                compute="_compute_cotisation", store=True)
    base_calcul_allocation = fields.Integer("Base de calcul allocation familiale", compute="_compute_cotisation",
                                            store=True)
    montant_allocation_familiale = fields.Integer("Montant allocation familiale", compute="_compute_cotisation",
                                                  store=True)
    taux_allocation_familiale = fields.Float("Taux allocation familiale", compute="_compute_cotisation", store=True)
    taux_cfce = fields.Float("Taux CFCE", compute="_compute_cotisation", store=True)
    base_calcul_accident_travail = fields.Integer("Base de calcul accident de travail", compute="_compute_cotisation",
                                                  store=True)
    montant_accident_travail = fields.Integer("Montant accident de travail", compute="_compute_cotisation",
                                              store=True)
    montant_cfce = fields.Integer("Montant CFCE", compute="_compute_cotisation", store=True)
    taux_accident_travail = fields.Float("Taux accident travail", compute="_compute_cotisation", store=True)
    trimf = fields.Integer("Trimf", compute="_compute_trimf", store=True)
    nbre_parts_trimf = fields.Integer("Nombre de parts Trimf", compute="_compute_trimf", store=True)
    cumul_salaire_brut = fields.Integer("Cumul des salaires brut", compute="_compute_cumul_salaire", store=True)
    cumul_charges_salariales = fields.Integer("Cumul charges salariales", compute="_compute_cumul_salaire", store=True)
    cumul_charges_patronales = fields.Integer("Cumul charges patronales", compute="_compute_cumul_salaire", store=True)
    cumul_heures_travail = fields.Float("Cumul heures travaillées", compute="_compute_cumul_salaire", store=True)
    total_imposable = fields.Float("Total brut", compute="_compute_cotisation", store=True)
    total_cotisation_employe = fields.Float("Total cotisation employé", compute="_compute_cotisation", store=True)
    total_cotisation_employeur = fields.Float("Total cotisation employeur", compute="_compute_cotisation", store=True)
    total_non_imposable = fields.Float("Total non imposable", compute="_compute_cotisation", store=True)
    # loan_ids = fields.Many2one('hr.loan.line', string="Prêts", readonly=True)
    montant_anciennete = fields.Float("Montant de l'ancienneté", compute="_compute_salaire", store=True)
    all_cotisation_employe_general = fields.Float("Ensemble cotisation employé général",
                                                  compute="_compute_all_cotisation_employe",
                                                  store=True)
    all_cotisation_employeur_general = fields.Float("Ensemble cotisation employeur général",
                                                    compute="_compute_all_cotisation_employe",
                                                    store=True)
    all_cotisation_employe_cadre = fields.Float("Ensemble cotisation employé cadre",
                                                compute="_compute_all_cotisation_employe",
                                                store=True)
    all_cotisation_employeur_cadre = fields.Float("Ensemble cotisation employeur cadre",
                                                  compute="_compute_all_cotisation_employe",
                                                  store=True)
    base_global_general = fields.Float("base totale général",
                                       compute="_compute_all_cotisation_employe",
                                       store=True)
    base_global_cadre = fields.Float("base totale cadre",
                                     compute="_compute_all_cotisation_employe",
                                     store=True)
    total_ipress_cadre = fields.Float("total ipress cadre",
                                      compute="_compute_all_cotisation_employe",
                                      store=True)
    total_ipress_general = fields.Float("total ipress general",
                                        compute="_compute_all_cotisation_employe",
                                        store=True)
    total_ipress = fields.Float("total ipress",
                                compute="_compute_all_cotisation_employe",
                                store=True)
    total_retenue = fields.Float("Total retenue",
                                compute="_compute_all_cotisation_employe",
                                store=True)
    salaire_moyen = fields.Float('Salaire moyen', compute="_compute_salaire", store=True)
    indemn_licenciement = fields.Float('Indemnité de licenciement', compute="_compute_salaire", store=True)
    indemn_retraite = fields.Float('Indemnité de retraite', compute="_compute_salaire", store=True)
    indemn_deces = fields.Float('Indemnité de décés', compute="_compute_salaire", store=True)
    indemn_fin_cdd = fields.Float('Indemnité de fin cdd', compute="_compute_salaire", store=True)

    @api.depends('contract_id')
    def _compute_struct_id(self):
        for struct in self.filtered('employee_id'):
            struct.struct_id = struct.contract_id.structure_name_id

    @api.depends('date_from', 'date_to', 'struct_id')
    def _compute_warning_message(self):
        for slip in self.filtered(lambda p: p.date_to):
            slip.warning_message = False
            warnings = []
            if slip.contract_id and (slip.date_from < slip.contract_id.date_start
                    or (slip.contract_id.date_end and slip.date_to > slip.contract_id.date_end)):
                pass

            if slip.date_to > date_utils.end_of(fields.Date.today(), 'month'):
                pass

            if (slip.contract_id.schedule_pay or slip.contract_id.structure_type_id.default_schedule_pay)\
                    and slip.date_from + slip._get_schedule_timedelta() != slip.date_to:
                pass

            # if warnings:
            #     warnings = [_("This payslip can be erroneous :")] + warnings
            #     slip.warning_message = "\n  ・ ".join(warnings)

    @api.depends('contract_id.wage', 'contract_id.sursalaire',
                 'contract_id.carburant',
                 'contract_id.indemn_logement',
                 'contract_id.prime_panier', 'contract_id.employee_id.nbre_parts', 'contract_id.employee_id.seniority_months')
    def _compute_salaire(self):
        for val in self:
            nbre_jours = 0
            if val.worked_days_line_ids:
                p = val.worked_days_line_ids
                for a in p:
                    if a.code == 'WORK100':
                        nbre_jours += a.number_of_days
                        print('Number of days', nbre_jours)
            val.indemnite_transport = round((val.contract_id.indemnite_transport * nbre_jours) / 30)
            val.salaire_base = round((val.contract_id.wage * nbre_jours) / 30)
            val.sursalaire = round((val.contract_id.sursalaire * nbre_jours) / 30)

            if 24 <= val.employee_id.seniority_months <= 36:
                val.montant_anciennete = int(round(val.salaire_base * 0.02))
            if 37 <= val.employee_id.seniority_months <= 48:
                val.montant_anciennete = int(round(val.salaire_base * 0.03))
            if 49 <= val.employee_id.seniority_months <= 60:
                val.montant_anciennete = int(round(val.salaire_base * 0.04))
            if 61 <= val.employee_id.seniority_months <= 72:
                val.montant_anciennete = int(round(val.salaire_base * 0.05))
            if 73 <= val.employee_id.seniority_months <= 84:
                val.montant_anciennete = int(round(val.salaire_base * 0.06))
            if 85 <= val.employee_id.seniority_months <= 96:
                val.montant_anciennete = int(round(val.salaire_base * 0.07))
            if 97 <= val.employee_id.seniority_months <= 108:
                val.montant_anciennete = int(round(val.salaire_base * 0.08))
            if 109 <= val.employee_id.seniority_months <= 120:
                val.montant_anciennete = int(round(val.salaire_base * 0.09))
            if 121 <= val.employee_id.seniority_months <= 132:
                val.montant_anciennete = int(round(val.salaire_base * 0.1))
            if 133 <= val.employee_id.seniority_months <= 144:
                val.montant_anciennete = int(round(val.salaire_base * 0.11))
            if 145 <= val.employee_id.seniority_months <= 156:
                val.montant_anciennete = int(round(val.salaire_base * 0.12))
            if 157 <= val.employee_id.seniority_months <= 168:
                val.montant_anciennete = int(round(val.salaire_base * 0.13))
            if 169 <= val.employee_id.seniority_months <= 180:
                val.montant_anciennete = int(round(val.salaire_base * 0.14))
            if 181 <= val.employee_id.seniority_months <= 192:
                val.montant_anciennete = int(round(val.salaire_base * 0.15))
            if 193 <= val.employee_id.seniority_months <= 204:
                val.montant_anciennete = int(round(val.salaire_base * 0.16))
            if 205 <= val.employee_id.seniority_months <= 216:
                val.montant_anciennete = int(round(val.salaire_base * 0.17))
            if 217 <= val.employee_id.seniority_months <= 228:
                val.montant_anciennete = int(round(val.salaire_base * 0.18))
            if 229 <= val.employee_id.seniority_months <= 240:
                val.montant_anciennete = int(round(val.salaire_base * 0.19))
            if 241 <= val.employee_id.seniority_months <= 252:
                val.montant_anciennete = int(round(val.salaire_base * 0.2))
            if 253 <= val.employee_id.seniority_months <= 264:
                val.montant_anciennete = int(round(val.salaire_base * 0.21))
            if 265 <= val.employee_id.seniority_months <= 276:
                val.montant_anciennete = int(round(val.salaire_base * 0.22))
            if 277 <= val.employee_id.seniority_months <= 288:
                val.montant_anciennete = int(round(val.salaire_base * 0.23))
            if 289 <= val.employee_id.seniority_months <= 300:
                val.montant_anciennete = int(round(val.salaire_base * 0.24))
            if val.employee_id.seniority_months >= 301:
                val.montant_anciennete = int(round(val.salaire_base * 0.25))

            val.salaire_brut = val.salaire_base + val.sursalaire + val.contract_id.indemnite_tel + \
                               val.contract_id.indemn_logement + val.contract_id.carburant
            val.salaire_moyen = val.salaire_base + val.sursalaire + val.contract_id.indemnite_tel + \
                               val.contract_id.indemn_logement + val.contract_id.carburant
            if val.contract_id.sortie and val.contract_id.motif == 'licen':
                if val.contract_id.employee_id.seniority_months <= 5:
                    val.indemn_licenciement = val.salaire_moyen * 0.25
                if 6 <= val.contract_id.employee_id.seniority_months <= 10:
                    val.indemn_licenciement = val.salaire_moyen * 0.3
                if val.contract_id.employee_id.seniority_months > 10:
                    val.indemn_licenciement = val.salaire_moyen * 0.4
            if val.contract_id.sortie and val.contract_id.motif == 'retr':
                if val.contract_id.employee_id.seniority_months <= 5:
                    val.indemn_retraite = val.salaire_moyen * 0.25
                if 6 <= val.contract_id.employee_id.seniority_months <= 10:
                    val.indemn_retraite = val.salaire_moyen * 0.3
                if 11 <= val.contract_id.employee_id.seniority_months <= 20:
                    val.indemn_retraite = val.salaire_moyen * 0.45
                if val.contract_id.employee_id.seniority_months > 20:
                    val.indemn_retraite = val.salaire_moyen * 0.5
            if val.contract_id.sortie and val.contract_id.motif == 'dec':
                if val.contract_id.employee_id.seniority_months <= 5:
                    val.indemn_deces = val.salaire_moyen * 0.25
                if 6 <= val.contract_id.employee_id.seniority_months <= 10:
                    val.indemn_deces = val.salaire_moyen * 0.3
                if val.contract_id.employee_id.seniority_months > 10:
                    val.indemn_deces = val.salaire_moyen * 0.4
            if val.contract_id.sortie and val.contract_id.motif == 'cdd':
                a = self.env["hr.payslip"].search([('employee_id.id', '=', val.employee_id.id)])
                total_value = sum(brut.salaire_brut for brut in a)
                val.indemn_fin_cdd = total_value / len(a)
                    
        print('Salaire brut', val.salaire_brut)
        print('Salaire de base', val.salaire_base)
        print('Sursalaire', val.sursalaire)

    @api.depends('salaire_brut', 'contract_id', 'employee_id')
    def _compute_trimf(self):
        for val in self:
            val.trimf = 0
            if not val.contract_id:
                val.trimf = 0
            if val.salaire_brut <= 83999 and val.employee_id.husband_wife_status == 'not_employee':
                val.trimf = 300 * 2
                val.nbre_parts_trimf = 2
            elif val.salaire_brut <= 83999:
                val.trimf = 300
                val.nbre_parts_trimf = 1
            elif 84000 <= val.salaire_brut <= 166999 and val.employee_id.husband_wife_status == 'not_employee':
                val.trimf = 400 * 2
                val.nbre_parts_trimf = 2
            elif 84000 <= val.salaire_brut <= 166999:
                val.trimf = 400
                val.nbre_parts_trimf = 1
            elif 167000 <= val.salaire_brut <= 999999 and val.employee_id.husband_wife_status == 'not_employee':
                val.trimf = 500 * 2
                val.nbre_parts_trimf = 2
            elif 167000 <= val.salaire_brut <= 999999:
                val.trimf = 500
                val.nbre_parts_trimf = 1
            elif val.salaire_brut > 999999 and val.employee_id.husband_wife_status == 'not_employee':
                val.trimf = 1500 * 2
                val.nbre_parts_trimf = 2
            else:
                val.trimf = 1500
                val.nbre_parts_trimf = 1

    @api.depends('salaire_brut')
    def _compute_impot_mensuel(self):
        for rep in self:
            salaire_brut_annuel = rep.salaire_brut * 12
            print("Salaire brut annuel", salaire_brut_annuel)
            abattement = salaire_brut_annuel * 0.3
            if abattement > 900000:
                abattement = 900000
            print("Abattement", abattement)
            brut_annuel_apres_abattement = salaire_brut_annuel - abattement
            rep.base_fiscal_abatt = brut_annuel_apres_abattement
            print("Brut fiscal après abattement", brut_annuel_apres_abattement)
            impot_brut = 0

            # Impôt brut
            reduction_impot_brut = 0
            impot_final = 0
            if brut_annuel_apres_abattement <= 630000:
                impot_brut = impot_brut + 0
            if 630001 <= brut_annuel_apres_abattement <= 1500000:
                impot_brut = impot_brut + (brut_annuel_apres_abattement - 630001) * 0.2
            if 1500001 <= brut_annuel_apres_abattement <= 4000000:
                impot_brut = impot_brut + 174000 + ((brut_annuel_apres_abattement - 1500001) * 0.3)
            if 4000001 <= brut_annuel_apres_abattement <= 8000000:
                impot_brut = impot_brut + 924000 + ((brut_annuel_apres_abattement - 4000001) * 0.35)
            if 8000001 <= brut_annuel_apres_abattement <= 13500000:
                impot_brut = impot_brut + 2324000 + ((brut_annuel_apres_abattement - 8000001) * 0.37)
                print("Premier impot brut", impot_brut)
            if 13500001 <= brut_annuel_apres_abattement <= 1000000000:
                impot_brut = impot_brut + 4359000 + ((brut_annuel_apres_abattement - 13500001) * 0.4)

            # Réduction impôt brut
            if rep.contract_id.employee_id.nbre_parts == 1:
            # if rep.contract_id.nbre_parts == 1:
                reduction_impot_brut = 0
            if rep.contract_id.employee_id.nbre_parts == 1.5:
            # if rep.contract_id.nbre_parts == 1.5:
                reduction_impot_brut = impot_brut * 0.1
                if reduction_impot_brut < 100000:
                    reduction_impot_brut = 100000
                if reduction_impot_brut > 300000:
                    reduction_impot_brut = 300000
            if rep.contract_id.employee_id.nbre_parts == 2:
            # if rep.contract_id.nbre_parts == 2:
                reduction_impot_brut = impot_brut * 0.15
                if reduction_impot_brut < 200000:
                    reduction_impot_brut = 200000
                if reduction_impot_brut > 650000:
                    reduction_impot_brut = 650000
            if rep.contract_id.employee_id.nbre_parts == 2.5:
            # if rep.contract_id.nbre_parts == 2.5:
                reduction_impot_brut = impot_brut * 0.2
                if reduction_impot_brut < 300000:
                    reduction_impot_brut = 300000
                if reduction_impot_brut > 1100000:
                    reduction_impot_brut = 1100000
            if rep.contract_id.employee_id.nbre_parts == 3:
            # if rep.contract_id.nbre_parts == 3:
                reduction_impot_brut = impot_brut * 0.25
                if reduction_impot_brut < 400000:
                    reduction_impot_brut = 400000
                if reduction_impot_brut > 1650000:
                    reduction_impot_brut = 1650000
            if rep.contract_id.employee_id.nbre_parts == 3.5:
            # if rep.contract_id.nbre_parts == 3.5:
                reduction_impot_brut = impot_brut * 0.3
                if reduction_impot_brut < 500000:
                    reduction_impot_brut = 500000
                if reduction_impot_brut > 2030000:
                    reduction_impot_brut = 2030000
            if rep.contract_id.employee_id.nbre_parts == 4:
            # if rep.contract_id.nbre_parts == 4:
                reduction_impot_brut = impot_brut * 0.35
                if reduction_impot_brut < 600000:
                    reduction_impot_brut = 600000
                if reduction_impot_brut > 2490000:
                    reduction_impot_brut = 2490000
            if rep.contract_id.employee_id.nbre_parts == 4.5:
            # if rep.contract_id.nbre_parts == 4.5:
                reduction_impot_brut = impot_brut * 0.4
                if reduction_impot_brut < 700000:
                    reduction_impot_brut = 700000
                if reduction_impot_brut > 2755000:
                    reduction_impot_brut = 2755000
            if rep.contract_id.employee_id.nbre_parts == 5:
            # if rep.contract_id.nbre_parts == 5:
                reduction_impot_brut = impot_brut * 0.45
                if reduction_impot_brut < 800000:
                    reduction_impot_brut = 800000
                if reduction_impot_brut > 3180000:
                    reduction_impot_brut = 3180000
            print("Réduction impot", reduction_impot_brut)

            # Impôt mensuel
            impot_final = impot_final + int(round((impot_brut - reduction_impot_brut) / 12))
            if impot_final < 0:
                rep.impot_revenu = 0
            else:
                rep.impot_revenu = impot_final
            print("Impôt mensuel", rep.impot_revenu)

    @api.depends('contract_id', 'struct_id', 'salaire_brut')
    def _compute_cotisation(self):
        for cot in self:
            cot.taux_ipress_general_employe = 0.056
            cot.taux_ipress_general_employeur = 0.084
            cot.taux_ipress_cadre_employe = 0.024
            cot.taux_ipress_cadre_employeur = 0.036
            cot.taux_allocation_familiale = 0.07
            cot.taux_accident_travail = 0.03
            cot.taux_cfce = 0.03
            if cot.struct_id.name == 'Régime non cadre':
                if cot.salaire_brut > 63000:
                    cot.base_calcul_allocation = cot.base_calcul_accident_travail = 63000
                cot.montant_allocation_familiale = int(
                    round(cot.base_calcul_allocation * cot.taux_allocation_familiale))
                print("Allocation familiale", cot.montant_allocation_familiale)
                cot.montant_accident_travail = int(round(cot.base_calcul_accident_travail * cot.taux_accident_travail))
                print("Accident de travail", cot.montant_accident_travail)
                cot.caisse_ss = cot.montant_allocation_familiale + cot.montant_accident_travail
                cot.total_imposable = int(cot.salaire_brut)
                print("Total imposable", cot.total_imposable)

                cot.base_calcul_ipress_general = cot.salaire_brut
                cot.montant_cfce = cot.salaire_brut * cot.taux_cfce
                if cot.salaire_brut > 432000:
                    cot.base_calcul_ipress_general = 432000
                cot.montant_ipress_general_employee = int(
                    round(cot.base_calcul_ipress_general * cot.taux_ipress_general_employe))
                print("Ipress RG employe", cot.montant_ipress_general_employee)
                cot.montant_ipress_general_employeur = int(
                    round(cot.base_calcul_ipress_general * cot.taux_ipress_general_employeur))
                cot.regime_general_employe_employeur = cot.montant_ipress_general_employee + cot.montant_ipress_general_employeur
                print("Ipress RG employeur", cot.montant_ipress_general_employeur)
                cot.total_cotisation = cot.montant_ipress_general_employee + cot.impot_revenu + cot.trimf

                cot.total_cotisation_employe = int(
                    cot.impot_revenu + cot.montant_ipress_general_employee + cot.trimf)
                print("Total cotisation employé général", cot.total_cotisation_employe)
                cot.total_cotisation_employeur = int(
                    cot.montant_allocation_familiale + cot.montant_accident_travail + cot.montant_ipress_general_employeur + cot.montant_cfce)
                print("Total cotisation employeur général", cot.total_cotisation_employeur)

            if cot.struct_id.name == 'Régime cadre':
                if cot.salaire_brut > 63000:
                    cot.base_calcul_allocation = cot.base_calcul_accident_travail = 63000
                cot.montant_allocation_familiale = int(
                    round(cot.base_calcul_allocation * cot.taux_allocation_familiale))
                print("Allocation familiale", cot.montant_allocation_familiale)
                cot.montant_accident_travail = int(round(cot.base_calcul_accident_travail * cot.taux_accident_travail))
                print("Accident de travail", cot.montant_accident_travail)
                cot.caisse_ss = cot.montant_allocation_familiale + cot.montant_accident_travail
                cot.total_imposable = int(cot.salaire_brut)
                print("Total imposable", cot.total_imposable)

                cot.base_calcul_ipress_cadre = cot.base_calcul_ipress_general = cot.salaire_brut
                cot.montant_cfce = cot.salaire_brut * cot.taux_cfce
                if cot.salaire_brut > 1296000: 
                    cot.base_calcul_ipress_cadre = 1296000
                cot.montant_ipress_cadre_employe = int(
                    round(cot.base_calcul_ipress_cadre * cot.taux_ipress_cadre_employe))
                print("Ipress RC employe", cot.montant_ipress_cadre_employe)
                cot.montant_ipress_cadre_employeur = int(
                    round(cot.base_calcul_ipress_cadre * cot.taux_ipress_cadre_employeur))
                print("Ipress RC employeur", cot.montant_ipress_cadre_employeur)
                cot.regime_cadre_employe_employeur = cot.montant_ipress_cadre_employe + cot.montant_ipress_cadre_employeur
                if cot.salaire_brut > 432000:
                    cot.base_calcul_ipress_general = 432000
                cot.montant_ipress_general_employee = int(
                    round(cot.base_calcul_ipress_general * cot.taux_ipress_general_employe))
                print("Ipress RG employe", cot.montant_ipress_general_employee)
                cot.montant_ipress_general_employeur = int(
                    round(cot.base_calcul_ipress_general * cot.taux_ipress_general_employeur))
                print("Ipress RG employeur", cot.montant_ipress_general_employeur)
                cot.regime_general_employe_employeur = cot.montant_ipress_general_employee + cot.montant_ipress_general_employeur
                cot.total_cotisation_employe = int(
                    cot.impot_revenu + cot.montant_ipress_cadre_employe + cot.montant_ipress_general_employee + cot.trimf)
                print("Total cotisation employé cadre", cot.total_cotisation_employe)
                cot.total_cotisation_employeur = int(
                    cot.montant_allocation_familiale + cot.montant_accident_travail + cot.montant_ipress_cadre_employeur + cot.montant_ipress_general_employeur + cot.montant_cfce)
                print("Total cotisation employeur cadre", cot.total_cotisation_employeur)
                cot.total_retenue = int(cot.impot_revenu)

            cot.total_non_imposable = cot.indemnite_transport + \
                                      cot.contract_id.prime_panier + cot.indemn_retraite + cot.indemn_deces + \
                                      cot.indemn_licenciement + \
                                      cot.contract_id.indemnite_respon + cot.contract_id.indemnite_kilom + cot.contract_id.indemnite_kilom_com + cot.indemn_fin_cdd
            # print("Total non imposable", cot.total_non_imposable)
            #########################################################################
            #                           BON
            ##########################################################################
            cot.salaire_net = cot.salaire_brut - cot.total_cotisation_employe - cot.contract_id.retenue + \
                              cot.total_non_imposable
            print("Salaire net", cot.salaire_net)

    # @api.depends('montant_ipress_general_employee', 'montant_ipress_general_employeur',
    #              'montant_ipress_cadre_employe', 'montant_ipress_cadre_employeur', 'base_calcul_ipress_general',
    #              'base_calcul_ipress_cadre')
    def _compute_all_cotisation_employe(self):
        for all in self:
            validated_payslip = self.env["hr.payslip"].search([])
            for x in validated_payslip:
                all.all_cotisation_employe_general += x.montant_ipress_general_employee
                all.all_cotisation_employeur_general += x.montant_ipress_general_employeur
                all.all_cotisation_employe_cadre += x.montant_ipress_cadre_employe
                all.all_cotisation_employeur_cadre += x.montant_ipress_cadre_employeur
                all.base_global_general += x.base_calcul_ipress_general
                all.base_global_cadre += x.base_calcul_ipress_cadre
            all.total_ipress_cadre = all.all_cotisation_employe_cadre + all.all_cotisation_employeur_cadre
            all.total_ipress_general = all.all_cotisation_employe_general + all.all_cotisation_employeur_general
            all.total_ipress = all.total_ipress_cadre + all.total_ipress_general
        print("Résumé ipress employé général", all.all_cotisation_employe_general)
        print("Résumé ipress employeur général", all.all_cotisation_employeur_general)
        print("Résumé ipress employé cadre", all.all_cotisation_employe_cadre)
        print("Résumé ipress employeur cadre", all.all_cotisation_employeur_cadre)
        print("Base global général", all.base_global_general)
        print("Base global cadre", all.base_global_cadre)
        print("Total ipress cadre", all.total_ipress_cadre)
        print("Total ipress general", all.total_ipress_general)
        print("Total ipress", all.total_ipress)

    def _get_worked_day_lines_values(self, domain=None):
        self.ensure_one()
        res = []
        hours_per_day = self._get_worked_day_lines_hours_per_day()
        work_hours = self.contract_id.get_work_hours(self.date_from, self.date_to, domain=domain)
        work_hours_ordered = sorted(work_hours.items(), key=lambda x: x[1])
        biggest_work = work_hours_ordered[-1][0] if work_hours_ordered else 0
        add_days_rounding = 0
        for work_entry_type_id, hours in work_hours_ordered:
            work_entry_type = self.env['hr.work.entry.type'].browse(work_entry_type_id)
            days = round(hours / hours_per_day, 5) if hours_per_day else 0
            if work_entry_type_id == biggest_work:
                days += add_days_rounding
            day_rounded = self._round_days(work_entry_type, days)
            add_days_rounding += (days - day_rounded)
            attendance_line = {
                'sequence': work_entry_type.sequence,
                'work_entry_type_id': work_entry_type_id,
                'number_of_days': 30.00,
                'number_of_hours': 173.33,
            }
            res.append(attendance_line)

        # Sort by Work Entry Type sequence
        work_entry_type = self.env['hr.work.entry.type']
        return sorted(res, key=lambda d: work_entry_type.browse(d['work_entry_type_id']).sequence)


# class CotisationsSociales(models.Model):
#     _name = 'nrt.contributions'
#     _description = 'Résumé des cotisations sur une période déterminée'

#     name = fields.Char('Nom', required=True, store=True)
#     date_from = fields.Date('Date de debut', required=True, store=True)
#     company_id = fields.Many2one(
#         'res.company', string='Company', copy=False, required=True, store=True, readonly=False,
#         default=lambda self: self.env.company)
#     date_to = fields.Date('Date de fin', required=True, store=True)
#     base_general = fields.Float('Base régime général', compute='get_payslips', store=True)
#     base_cadre = fields.Float('Base régime cadre', compute='get_payslips', store=True)
#     ipress_regime_general_h = fields.Float('Ipress régime général homme', compute='get_payslips', store=True)
#     ipress_regime_general_f = fields.Float('Ipress régime général femme', compute='get_payslips', store=True)
#     ipress_regime_cadre_h = fields.Float('Ipress régime cadre homme', compute='get_payslips', store=True)
#     ipress_regime_cadre_f = fields.Float('Ipress régime cadre femme', compute='get_payslips', store=True)
#     report_ipress_general_employee_h = fields.Float('Ipress régime général employés homme', compute='get_payslips', store=True)
#     report_ipress_general_employee_f = fields.Float('Ipress régime général employés femme', compute='get_payslips', store=True)
#     report_ipress_general_employeur_h = fields.Float('Ipress régime général employeur homme', compute='get_payslips',
#                                                    store=True)
#     report_ipress_general_employeur_f = fields.Float('Ipress régime général employeur femme', compute='get_payslips',
#                                                    store=True)
#     report_ipress_cadre_employe_h = fields.Float('Ipress régime cadre employé homme', compute='get_payslips', store=True)
#     report_ipress_cadre_employe_f = fields.Float('Ipress régime cadre employé femme', compute='get_payslips', store=True)
#     report_ipress_cadre_employeur_h = fields.Float('Ipress régime cadre employeur homme', compute='get_payslips', store=True)
#     report_ipress_cadre_employeur_f = fields.Float('Ipress régime cadre employeur femme', compute='get_payslips', store=True)
#     totat_ipress_general_h = fields.Float('Total ipress general homme', compute='get_payslips', store=True)
#     totat_ipress_general_f = fields.Float('Total ipress general femme', compute='get_payslips', store=True)
#     totat_ipress_cadre_h = fields.Float('Total ipress cadre homme', compute='get_payslips', store=True)
#     totat_ipress_cadre_f = fields.Float('Total ipress cadre femme', compute='get_payslips', store=True)
#     reprot_total_ipress_h = fields.Float('Total cotisations homme', compute='get_payslips', store=True)
#     reprot_total_ipress_f = fields.Float('Total cotisations femme', compute='get_payslips', store=True)
#     brut_imposable_h = fields.Float('Total brut imposable homme', compute='get_payslips', store=True)
#     brut_imposable_f = fields.Float('Total brut imposable femme', compute='get_payslips', store=True)
#     nbre_homme = fields.Integer('Nombre hommes', compute='get_payslips', store=True)
#     nbre_femme = fields.Integer('Nombre femmes', compute='get_payslips', store=True)

#     @api.depends('date_from', 'date_to')
#     def get_payslips(self):
#         for x in self:
#             h = self.env["hr.payslip"].search([('date_from', '<=', x.date_to),
#                                                ('date_to', '>=', x.date_from), ('employee_id.gender', '=', 'male')])
#             f = self.env["hr.payslip"].search([('date_from', '<=', x.date_to),
#                                                ('date_to', '>=', x.date_from), ('employee_id.gender', '=', 'female')])
#             for val in h:
#                 x.nbre_homme = len(h)
#                 x.brut_imposable_h += val.salaire_brut 
#                 x.ipress_regime_general_h += val.base_calcul_ipress_general
#                 x.ipress_regime_cadre_h += val.base_calcul_ipress_cadre
#                 x.report_ipress_general_employee_h += val.montant_ipress_general_employee
#                 x.report_ipress_general_employeur_h += val.montant_ipress_general_employeur
#                 x.report_ipress_cadre_employe_h += val.montant_ipress_cadre_employe
#                 x.report_ipress_cadre_employeur_h += val.montant_ipress_cadre_employeur
#                 x.totat_ipress_general_h = x.report_ipress_general_employee_h + x.report_ipress_general_employeur_h
#                 x.totat_ipress_cadre_h = x.report_ipress_cadre_employe_h + x.report_ipress_cadre_employeur_h
#                 x.reprot_total_ipress_h = x.totat_ipress_general_h + x.totat_ipress_cadre_h
#             for soc in f:
#                 x.nbre_femme = len(f)
#                 x.brut_imposable_f += soc.salaire_brut 
#                 x.ipress_regime_general_f += soc.base_calcul_ipress_general
#                 x.ipress_regime_cadre_f += soc.base_calcul_ipress_cadre
#                 x.report_ipress_general_employee_f += soc.montant_ipress_general_employee
#                 x.report_ipress_general_employeur_f += soc.montant_ipress_general_employeur
#                 x.report_ipress_cadre_employe_f += soc.montant_ipress_cadre_employe
#                 x.report_ipress_cadre_employeur_f += soc.montant_ipress_cadre_employeur
#                 x.totat_ipress_general_f = x.report_ipress_general_employee_f + x.report_ipress_general_employeur_f
#                 x.totat_ipress_cadre_f = x.report_ipress_cadre_employe_f + x.report_ipress_cadre_employeur_f
#                 x.reprot_total_ipress_f = x.totat_ipress_general_f + x.totat_ipress_cadre_f
                

# class RetenuesFiscales(models.Model):
#     _name = 'nrt.retenue'
#     _description = 'Résumé des retenues fiscales sur une période déterminée'

#     name = fields.Char('Nom', required=True, store=True)
#     date_from = fields.Date('Date de debut', required=True, store=True)
#     company_id = fields.Many2one(
#         'res.company', string='Company', copy=False, required=True, store=True, readonly=False,
#         default=lambda self: self.env.company)
#     date_to = fields.Date('Date de fin', required=True, store=True)
#     base_general = fields.Float('Base régime général', compute='get_payslips', store=True)
#     base_cadre = fields.Float('Base régime cadre', compute='get_payslips', store=True)
#     ipress_regime_general = fields.Float('Ipress régime général', compute='get_payslips', store=True)
#     ipress_regime_cadre = fields.Float('Ipress régime cadre', compute='get_payslips', store=True)
#     report_ipress_general_employee = fields.Float('Ipress régime général employés', compute='get_payslips', store=True)
#     report_ipress_general_employeur = fields.Float('Ipress régime général employeur', compute='get_payslips',
#                                                    store=True)
#     report_ipress_cadre_employe = fields.Float('Ipress régime cadre employé', compute='get_payslips', store=True)
#     report_ipress_cadre_employeur = fields.Float('Ipress régime cadre employeur', compute='get_payslips', store=True)
#     totat_ipress = fields.Float('Total ipress', compute='get_payslips', store=True)
#     report_alloc_familiales = fields.Float('Allocations familiales', compute='get_payslips', store=True)
#     report_accident_travail = fields.Float('Accident de travail', compute='get_payslips', store=True)
#     reprot_total_css = fields.Float('Total cotisations sociales', compute='get_payslips', store=True)
#     reprot_impot_revenu_h = fields.Float('Impôt sur le revenu homme', compute='get_payslips', store=True)
#     reprot_impot_revenu_f = fields.Float('Impôt sur le revenu femme', compute='get_payslips', store=True)
#     reprot_trimf_h = fields.Float('Trimf homme', compute='get_payslips', store=True)
#     reprot_trimf_f = fields.Float('Trimf femme', compute='get_payslips', store=True)
#     reprot_total_impot_h = fields.Float('Total impôt homme', compute='get_payslips', store=True)
#     reprot_total_impot_f = fields.Float('Total impôt femme', compute='get_payslips', store=True)
#     report_total_cfce_homme = fields.Float('Total cfce homme', compute='get_payslips', store=True)
#     report_total_cfce_femme = fields.Float('Total cfce femme', compute='get_payslips', store=True)
#     brut_imposable_h = fields.Float('Total brut imposable homme', compute='get_payslips', store=True)
#     brut_imposable_f = fields.Float('Total brut imposable femme', compute='get_payslips', store=True)
#     nbre_homme = fields.Integer('Nombre hommes', compute='get_payslips', store=True)
#     nbre_femme = fields.Integer('Nombre femmes', compute='get_payslips', store=True)

#     @api.depends('date_from', 'date_to')
#     def get_payslips(self):
#         for x in self:
#             h = self.env["hr.payslip"].search([('date_from', '<=', x.date_to),
#                                                ('date_to', '>=', x.date_from), ('employee_id.gender', '=', 'male')])
#             f = self.env["hr.payslip"].search([('date_from', '<=', x.date_to),
#                                                ('date_to', '>=', x.date_from), ('employee_id.gender', '=', 'female')])                                   
#             for val in h:
#                 x.nbre_homme = len(h)
#                 x.reprot_impot_revenu_h += val.impot_revenu
#                 x.reprot_trimf_h += val.trimf
#                 x.report_total_cfce_homme += val.montant_cfce
#                 x.brut_imposable_h += val.salaire_brut 
#                 x.reprot_total_impot_h = x.reprot_impot_revenu_h + x.reprot_trimf_h + x.report_total_cfce_homme
#             for el in f:
#                 x.nbre_femme = len(f)
#                 x.reprot_impot_revenu_f += el.impot_revenu
#                 x.reprot_trimf_f += el.trimf
#                 x.report_total_cfce_femme += el.montant_cfce
#                 x.brut_imposable_f += el.salaire_brut 
#                 x.reprot_total_impot_f = x.reprot_impot_revenu_f + x.reprot_trimf_f + x.report_total_cfce_femme


# class RetenuesFiscales(models.Model):
#     _name = 'nrt.fichier.controle'
#     _description = 'Fichier de contrôle'

#     name = fields.Char('Nom', required=True, store=True)
#     company_id = fields.Many2one(
#         'res.company', string='Company', copy=False, required=True, store=True, readonly=False,
#         default=lambda self: self.env.company)
#     date_from = fields.Date('Date de debut', required=True, store=True)
#     # prev_date_from = fields.Date('Date de debut', required=True, store=True)
#     date_to = fields.Date('Date de fin', required=True, store=True)
#     # prev_date_to = fields.Date('Date de fin', required=True, store=True)
#     # brut = fields.Integer('Salaire brut', compute='get_payslips_book', store=True)
#     # net = fields.Integer('Salaire net', compute='get_payslips_book', store=True)

#     def _get_brut_courant(self, employee_id, date_from, date_to):
#         slip = self.env['hr.payslip'].search([
#             ('employee_id', '=', employee_id),
#             ('date_from', '>=', date_from),
#             ('date_to', '<=', date_to)
#         ], limit=1)
#         return slip.salaire_brut

#     def _get_net_courant(self, employee_id, date_from, date_to):
#         slip = self.env['hr.payslip'].search([
#             ('employee_id', '=', employee_id),
#             ('date_from', '>=', date_from),
#             ('date_to', '<=', date_to)
#         ], limit=1)
#         return slip.salaire_net

#     @api.depends('date_from', 'date_to')
#     def get_payslips_book(self):
#         values = self.env['hr.payslip'].search([('date_from', '>=', self.date_from),
#                                                    ('date_to', '<=', self.date_to)])
#         # today = datetime.today()
#         # date_from = today.replace(day=1).date()
#         first_day_prev_month = (self.date_from - relativedelta(months=1))
#         last_day_prev_month = self.date_from - timedelta(days=1)
#         report_data = []

#         for x in values:
#             brut_courant = self._get_brut_courant(
#                 x.employee_id.id,
#                 self.date_from,
#                 self.date_to
#             )
#             brut_previous = self._get_brut_courant(
#                 x.employee_id.id,
#                 first_day_prev_month,
#                 last_day_prev_month
#             )
#             net_courant = self._get_net_courant(
#                 x.employee_id.id,
#                 self.date_from,
#                 self.date_to
#             )
#             net_previous = self._get_net_courant(
#                 x.employee_id.id,
#                 first_day_prev_month,
#                 last_day_prev_month
#             )
#             report_data.append({
#                 'employee': x.employee_id.name,
#                 'brut_courant': brut_courant,
#                 'brut_previous': brut_previous,
#                 'net_courant': net_courant,
#                 'net_previous': net_previous
#             })
#         print('rrrrrrrrTTTTTTTTTTTTTT', report_data)
#         return report_data


            # prev_date_from = self.date_from - timedelta(days=30)
            # prev_date_to = self.date_to - timedelta(days=30)
            # c = self.env["hr.payslip"].search([('date_from', '>=', val.date_from),
            #                                       ('date_to', '<=', val.date_to)])
            # p = self.env["hr.payslip"].search([('date_from', '<=', val.prev_date_to),
            #                                    ('date_to', '>=', val.prev_date_from)])

            # return self.env["hr.payslip"].search([('date_from', '>=', val.date_from),
            #                                       ('date_to', '<=', val.date_to)])




class LivrePaieNRT(models.Model):
    _name = 'nrt.livre.paie'
    _description = 'Ensemble des éléments de salaire pour chaque employé'

    name = fields.Char('Nom', required=True, store=True)
    company_id = fields.Many2one(
        'res.company', string='Company', copy=False, required=True, store=True, readonly=False,
        default=lambda self: self.env.company)
    date_from = fields.Date('Date de debut', required=True, store=True)
    date_to = fields.Date('Date de fin', required=True, store=True)
    sal_base = fields.Float('Salaire de base', compute='_compute_total_values', store=True)
    sur_sal = fields.Float('Sursalaire', compute='_compute_total_values', store=True)
    carburant = fields.Float('Carburant', compute='_compute_total_values', store=True)
    
    prime_panier = fields.Float('Indemnité compensatrice', compute='_compute_total_values', store=True)
    prime_transp = fields.Float('Indemnité de transport', compute='_compute_total_values', store=True)
    brut_impos = fields.Float('Brut imposable', compute='_compute_total_values', store=True)
    imp_rev = fields.Float('Impôt sur le revenu', compute='_compute_total_values', store=True)
    trimf = fields.Float('Trimf', compute='_compute_total_values', store=True)
    ipres_rg = fields.Float('IPRES RG', compute='_compute_total_values', store=True)
    ipres_rg_pat = fields.Float('IPRES RG PAT', compute='_compute_total_values', store=True)
    ipres_rc = fields.Float('IPRES RC', compute='_compute_total_values', store=True)
    ipres_rc_pat = fields.Float('IPRES RC PAT', compute='_compute_total_values', store=True)
    total_cot = fields.Float('Total cotisations', compute='_compute_total_values', store=True)
    retenue = fields.Float('Retenue', compute='_compute_total_values', store=True)
    total_ret = fields.Float('Total retenue', compute='_compute_total_values', store=True)
    total_salar = fields.Float('Total charges salariales', compute='_compute_total_values', store=True)
    total_patr = fields.Float('Total charges patronales', compute='_compute_total_values', store=True)
    net_payer = fields.Float('Net à payer', compute='_compute_total_values', store=True)

    @api.depends('date_from', 'date_to')
    def _compute_total_values(self):
        for x in self:
            if x.date_from and x.date_to:
                date_diff = x.date_to - x.date_from
                print('date_diff', date_diff)
                if x.date_from > x.date_to:
                    raise ValidationError('La date de début ne doit pas être supérieure à la date de fin')
                if date_diff.days > 31:
                    raise ValidationError('Veuillez choisir une période d\'un mois')
            all_values = self.env["hr.payslip"].search([('date_from', '<=', x.date_to),
                                                 ('date_to', '>=', x.date_from)])
            print('all_values', all_values)
            for val in all_values:
                if all_values:
                    print('Salaire net', val.salaire_net)
                    x.sal_base += val.salaire_base
                    x.sur_sal += val.sursalaire
                    x.carburant += val.contract_id.carburant
                    x.prime_panier += val.prime_panier
                    x.prime_transp += val.contract_id.indemnite_transport
                    x.brut_impos += val.salaire_brut
                    x.imp_rev += val.impot_revenu
                    x.trimf += val.trimf
                    x.ipres_rg += val.montant_ipress_general_employee
                    x.ipres_rg_pat += val.montant_ipress_general_employeur
                    x.ipres_rc += val.montant_ipress_cadre_employe
                    x.ipres_rc_pat += val.montant_ipress_cadre_employeur
                    x.total_cot = val.montant_ipress_general_employee + val.montant_ipress_general_employeur + val.montant_ipress_cadre_employe + val.montant_ipress_cadre_employeur
                    x.retenue_assur += val.contract_id.retenue
                    x.total_salar += val.total_cotisation_employe
                    x.total_patr += val.total_cotisation_employeur
                    x.net_payer += val.salaire_net
                else:
                    raise ValidationError('Il n\'y a pas de bulletins sur cette période')

    @api.depends('date_from', 'date_to')
    def get_payslips_book(self):
        for val in self:
            print(self.env["hr.payslip"].search([('date_from', '>=', val.date_from),
                                                 ('date_to', '<=', val.date_to)]))
            return self.env["hr.payslip"].search([('date_from', '>=', val.date_from),
                                                  ('date_to', '<=', val.date_to)])
