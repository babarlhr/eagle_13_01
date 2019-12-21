# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import http, _
from eagle.http import request


class PortalRating(http.Controller):

    @http.route(['/website/rating/comment'], type='json', auth="user", method=['POST'], website=True)
    def publish_rating_comment(self, rating_id, publisher_comment):
        rating = request.env['rating.rating'].search([('id', '=', int(rating_id))])
        if not rating:
            return {'error': _('Invalid rating')}
        rating.write({'publisher_comment': publisher_comment})
        # return to the front-end the created/updated publisher comment
        return rating.read(['publisher_comment', 'publisher_id', 'publisher_datetime'])[0]