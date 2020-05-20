from datetime import date
from odoo import models, fields, api

class HmsPatient(models.Model):
    _name = "hms.patient"

    def _calc_age(self):
        for rec in self:
            today = date.today()
            rec.Age = today.year - rec.Birthdate.year - ((today.month, today.day) < (rec.Birthdate.month, rec.Birthdate.day))

    Firstname = fields.Char()
    email = fields.Char()
    Lastname = fields.Char()
    Birthdate = fields.Date()
    History = fields.Html()
    CRRatio = fields.Float()
    Blood = fields.Selection([
        ("O", "O blood"),
        ("A", "A blood"),
        ("B", "B blood"),
    ])
    PCR = fields.Boolean()
    Image = fields.Binary()
    Address = fields.Text()
    Age = fields.Integer(compute="_calc_age")
    department_id = fields.Many2one("hms.department")
    states = fields.Selection([
        ("good", "good"),
        ("Undetirmend", "Undetirmend"),
        ("fair", "fair"),
        ("serious", "serious")
    ])
    doctor_id = fields.Many2many("hms.doctor")

    # is_department_open = fields.Boolean(related = "department_id.", "")

    @api.onchange("Age")
    def onchange_age(self):
        if self.Age < 30:
            self.PCR = True
    _sql_constraints = [
    ('email_valid', "CHECK(email  like '%@%.%')", 'please enter a valid format'),
    ("unique_email", "UNIQUE(email)", "Please enter a unique email")
    ]