from datetime import datetime
import time
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _
from odoo.tools import date_utils
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta



class JVEEmployee(models.Model):
    _inherit = "hr.employee"

    # payslip_count = fields.Integer(compute='_compute_payslip_count', string='Payslip Count')
    # show_payslip = fields.Boolean(compute='_compute_show_pyslips')
    nbre_parts = fields.Float("Nombre de parts sociales", compute="_compute_nbre_parts", store=True)
    husband_wife_status = fields.Selection([
        ('employee', 'Salarié(e)'),
        ('not_employee', 'Non salarié(e)'),
    ], string='Statut conjoint(e)')
    hire_date = fields.Date(string='Date d\'embauche', store=True, help='Date d\'emauche de l\'employé.')
    seniority_months = fields.Integer(string='Ancienneté (mois)', compute='_compute_seniority', store=True, readonly=True)
    seniority_year = fields.Char(string='Ancienneté (années)', compute='_compute_seniority', store=True, readonly=True)

    # def _compute_payslip_count(self):
    #     for employee in self:
    #         employee.payslip_count = len(employee.slip_ids)

    # def _compute_show_pyslips(self):
    #     for employee in self:
    #         if employee.user_id == self.env.user:
    #             employee.show_payslip = True
    #         else:
    #             employee.show_payslip = False

    @api.depends('hire_date')
    def _compute_seniority(self):        
        for x in self:
            if x.hire_date:
                x.seniority_year = ""
                hiring_date = datetime.strptime(str(x.hire_date), '%Y-%m-%d')
                today = datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d')
                year_diff = today - hiring_date
                day_diff = year_diff.days / float(365)
                x.seniority_year += str(int(year_diff.days / 365)) + ' an(s) et  ' + str(int(day_diff % 1 * 12)) + ' mois'
                x.seniority_months = (today.year - hiring_date.year) * 12 + (today.month - hiring_date.month)

    @api.depends('marital', 'children', 'husband_wife_status')
    def _compute_nbre_parts(self):
        parts = 1
        for a in self:
            if a.marital in ('single', 'widower', 'divorced'):
                a.nbre_parts = parts + (a.children * 0.5)
                a.husband_wife_status = 'employee'
            if a.marital == 'married' and a.husband_wife_status == 'employee':
                a.nbre_parts = parts + 0.5 + (a.children * 0.5)
            if a.marital == 'married' and a.husband_wife_status == 'not_employee':
                a.nbre_parts = parts + 1 + (a.children * 0.5)
            if a.marital == 'widower' and a.children > 0:
                a.nbre_parts = parts + 0.5 + (a.children * 0.5)
            if a.nbre_parts > 5:
                a.nbre_parts = 5
