from odoo import fields, models, api


class Productostransito(models.Model):
    _inherit = 'purchase.order.line'

    entransito = fields.Float(
        string='En tránsito',
        compute='_en_transito'
    )

    @api.depends('move_ids')
    def _en_transito(self):
        for record in self.filtered(lambda e: e.state == 'purchase'):
            data = []
            for move in record.move_ids.filtered(lambda e: record.order_id.name == e.origin and e.state == 'assigned'):
                data.append(move.product_uom_qty)
            record.entransito = sum(data)


