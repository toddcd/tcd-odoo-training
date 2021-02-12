# -*- coding: utf-8 -*-
# from odoo import http


# class ArtGallery(http.Controller):
#     @http.route('/art_gallery/art_gallery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/art_gallery/art_gallery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('art_gallery.listing', {
#             'root': '/art_gallery/art_gallery',
#             'objects': http.request.env['art_gallery.art_gallery'].search([]),
#         })

#     @http.route('/art_gallery/art_gallery/objects/<model("art_gallery.art_gallery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('art_gallery.object', {
#             'object': obj
#         })
