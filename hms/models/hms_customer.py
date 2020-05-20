from odoo import models, fields, api
from odoo.exceptions import UserError


class HmsCustomer(models.Model):
    _inherit = "res.partner"

    related_patient_id = fields.Many2one("hms.patient")
    Tax_id = fields.Char(required=True)

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise UserError('You are not allowed to delete this customer!')
        return super().unlink()

    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            if self.env['hms.patient'].search([('email', '=', rec.email)], count=True) >= 1:
                raise UserError('Email is not valid!')