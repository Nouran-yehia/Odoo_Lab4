from odoo import models, fields


class HmsDoctor(models.Model):
    _name = "hms.doctor"

    Firstname = fields.Char()
    Lastname = fields.Char()
    Image = fields.Binary()
    patient_id = fields.Many2many("hms.patient")
    department_id = fields.Many2many("hms.department")