# -*- coding: utf-8 -*-
# Copyright 2014-2019 Therp BV <https://therp.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# pylint: disable=no-member
from odoo import api, fields, models


class AccountAnalyticInvoiceLine(models.Model):
    _inherit = 'account.analytic.invoice.line'

    publication = fields.Boolean(
        string='Subscription product line',
        related='product_id.publication',
        store=True)

    @api.multi
    def action_distribution_list(self):
        self.ensure_one()
        action = self.env.ref(
            'publication.action_distribution_list').read()[0]
        partner = self.analytic_account_id.partner_id
        action['context'] = {
            'default_product_id': self.product_id.id,
            'default_contract_partner_id': partner.id}
        action['domain'] = [
            ('contract_partner_id', '=', partner.id),
            ('product_id', '=', self.product_id.id)]
        action['view_mode'] = 'form'
        action['target'] = 'current'
        return action
