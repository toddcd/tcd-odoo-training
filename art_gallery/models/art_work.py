# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date

class ArtWork(models.Model):
    _name = 'art_gallery.art.work'
    _description = 'Art Work'
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    name = fields.Char(string='Name')
    description = fields.Text(string='Description', default='Art Work History')

    height = fields.Float(string='Height', required=True, default=1.0)
    width = fields.Float(string='Width', required=True, default=1.0)
    
    finished_date = fields.Date(string='Finished Date', default=date.today())
    
    sold_date = fields.Date(string='Sold Date')
    
    product_id = fields.Many2one(comodel_name='product.template', string='Product')
    
    art_price = fields.Float(string='Art Price', compute='_compute_art_price', store=True)
    standard_price = fields.Float(related='product_id.standard_price', string='Standard Price')
    
    @api.depends('product_id','height', 'width')
    def _compute_art_price(self):
        for art in self:
            if art.standard_price > 0.0 and art.height > 1.0 and art.width > 1.0:
                art.art_price = art.product_id.standard_price * art.height * art.width
            else:
                art.art_price = 100.0
                
        
#     @api.model
#     def test_function(self):
         
#         self.env['sale.order'].create({
#             'partner_id': 2,
#             'order_line': [(0, 0, {'product_id': 4})]
#         })
        
                
    
