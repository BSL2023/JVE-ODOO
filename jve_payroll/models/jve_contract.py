from odoo import models, fields, api, _


class ContractInformations(models.Model):
    _inherit = 'hr.contract'

    indemnite_transport = fields.Float("Indemnité de transport", store=True)
    indemnite_tel = fields.Float("Indemnité de téléphone", store=True)
    prime_panier = fields.Float("Indemnité compensatrice", store=True)
    indemnite_respon = fields.Float("Indemnité de responsabilité", store=True)
    indemn_logement = fields.Float("Indemnité de logement", store=True)
    # indenm_fin_contract = fields.Float("Indemnité de fin de contrat", store=True)
    # indemn_licenc = fields.Float("Indemnité de licenciement", store=True)
    # indemn_retraite = fields.Float("Indemnité de départ à la retraite", store=True)
    # indemn_deces = fields.Float("Indemnité de décès", store=True)
    retenue = fields.Float("Retenue", store=True)
    category = fields.Many2one('hr.salary', "Catégorie salariale", store=True)
    wage = fields.Integer('Salaire de base', required=True, tracking=True, help="Employee's monthly gross wage.", related="category.salary")
    sursalaire = fields.Float("Sursalaire", store=True)
    structure_name_id = fields.Many2one('hr.payroll.structure', string="Régime")
    carburant = fields.Float("Indemnité Carburant", store=True)
    indemnite_kilom = fields.Float("Indemnité kilométrique(non commercial)", store=True)
    indemnite_kilom_com = fields.Float("Indemnité kilométrique(commercial)", store=True)
    sortie = fields.Boolean("Sortie", store=False)
    motif  = fields.Selection([
        ('cdd', 'Fin de contrat'),
        ('dem', 'Démission'),
        ('retr', 'Retraite'),
        ('licen', 'Licenciement'),
        ('dec', 'Décès')
    ], tracking=True)
    societe = fields.Many2one('res.company', related="employee_id.company_id")
    # nbre_parts = fields.Float('Nombre de parts')
    # anciennete = fields.Integer('Ancienneté')
    structure_name_id = fields.Many2one('hr.payroll.structure', string="Régime salarial")

class SalaryCategory(models.Model):
    _name = 'hr.salary'

    name = fields.Selection(
        [('1ère A', '1ère A'), ('1ère B', '1ère B'), ('2ème', '2ème'), ('3ème', '3ème'), ('4ème', '4ème'),
         ('5ème', '5ème'), ('6ème', '6ème'), ('7ème A', '7ème A'), ('7ème B', '7ème B'), ('8ème A', '8ème A'),
         ('8ème B', '8ème B'), ('8ème C', '8ème C'), ('9ème A', '9ème A'), ('9ème B', '9ème B'), ('10ème A', '10ème A'),
         ('10ème B', '10ème B'), ('10ème C', '10ème C'), ('11ème', '11ème')], required=True, string="Catégories")

    salary = fields.Integer('Salaire catégoriel', compute='_compute_category_salary')

    @api.depends('name')
    def _compute_category_salary(self):
        for sal in self:
            if sal.name == '1ère A':
                sal.salary = 69421
            elif sal.name == '1ère B':
                sal.salary = 73508
            elif sal.name == '2ème':
                sal.salary = 73990
            elif sal.name == '3ème':
                sal.salary = 76425
            elif sal.name == '4ème':
                sal.salary = 83083
            elif sal.name == '5ème':
                sal.salary = 89242
            elif sal.name == '6ème':
                sal.salary = 93790
            elif sal.name == '7ème A':
                sal.salary = 105341
            elif sal.name == '7ème B':
                sal.salary = 113984
            elif sal.name == '8ème A':
                sal.salary = 115717
            elif sal.name == '8ème B':
                sal.salary = 123485
            elif sal.name == '8ème C':
                sal.salary = 125450
            elif sal.name == '9ème A':
                sal.salary = 129130
            elif sal.name == '9ème B':
                sal.salary = 136284
            elif sal.name == '10ème A':
                sal.salary = 141024
            elif sal.name == '10ème B':
                sal.salary = 157096
            elif sal.name == '10ème C':
                sal.salary = 174049
            elif sal.name == '11ème':
                sal.salary = 195119
            else:
                sal.salary = 0

