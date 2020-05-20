from odoo import models, fields


class HmsDepartment(models.Model):
    _name = "hms.department"

    Name = fields.Char()
    Capacity = fields.Integer()
    Is_opened = fields.Boolean()
    patients_ids = fields.One2many("hms.patient", "department_id")
