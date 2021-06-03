# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import AccessDenied


class PurchasOrder(models.Model):
    _inherit = 'purchase.order'

    delivery_terms_id = fields.Many2one('delivery.terms',string='Delivery Terms', required=True)


class PurchasOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    delivery_terms_id = fields.Many2one(related='order_id.delivery_terms_id', string='Delivery Terms', required=True)