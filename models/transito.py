from odoo import fields, models, api


class Transito(models.Model):
    _inherit = 'stock.move'

    preciounitario_oc = fields.Float(
        string='En tránsito',
        compute='_getPrecioUnitario'
    )

    @api.depends('purchase_line_id')
    def _getPrecioUnitario(self):
        for record in self:
            self.preciounitario_oc = record.price_unit


#Este se estaba utilizando para un ejemplo heredando stock.move.line
# @api.depends('move_line_ids')
#     def _getPrecioUnitario(self):
#         for record in self:
#             for move in record.move_line_ids:
#                 for purchase in record.created_purchase_line_id:
#                     for product in purchase.product_id:
#                         if product == 

