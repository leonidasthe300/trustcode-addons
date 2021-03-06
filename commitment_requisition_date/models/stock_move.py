from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _prepare_procurement_values(self):
        res = super(StockMove, self)._prepare_procurement_values()

        res.update({
            'commitment_date': self.sale_line_id.order_id.commitment_date,
            'requisition_date': self.sale_line_id.order_id.requested_date,
        })
        return res

    def _get_new_picking_values(self):
        res = super(StockMove, self)._get_new_picking_values()

        res.update({
            'commitment_date': self.sale_line_id.order_id.commitment_date,
            'requisition_date': self.sale_line_id.order_id.requested_date,
        })
        return res
