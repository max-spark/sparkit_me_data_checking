# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp import exceptions

class sparkit_me_data_checking(models.TransientModel):
    _name = 'sparkit.vrf_verification_wizard'

    vrf_ids = fields.Many2many('sparkit.vrf', string="Visit Report Forms")

    verified = fields.Boolean(string="Visit Report Form Verified and Attendance Information Entered?")

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        # else:
        if self.verified:self.vrf_ids.write({'state':'approved'})
        return True

    @api.multi
    def do_reopen_form(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window',
                'res_model': self._name, # this model
                'res_id': self.id,  # the current wizard record
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new'}

    @api.multi
    def do_populate_tasks(self):
        self.ensure_one()
        VRF = self.env['sparkit.vrf']
        all_vrfs = VRF.search([('state', '!=', 'approved'), ('state', '!=', 'cancelled'), ('m_e_assistant_id', '=', self.env.uid)])
        self.vrf_ids = all_vrfs
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
