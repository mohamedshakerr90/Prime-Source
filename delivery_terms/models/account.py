# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import AccessDenied


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_delivery_terms(self):

        for move in self:
            if move.invoice_origin:
                print("invoice_origin", move.invoice_origin)
                if move.invoice_origin.startswith('P'):
                    main = self.env['purchase.order'].search([('name', '=', move.invoice_origin)], limit=1)
                    if main:
                        move.delivery_terms_id = main.delivery_terms_id.id
                else:
                    move.delivery_terms_id = False
            else:
                move.delivery_terms_id = False

    delivery_terms_id = fields.Many2one('delivery.terms',compute='get_delivery_terms',string='Delivery Terms')
