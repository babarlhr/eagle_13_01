# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import models, fields


class Challenge(models.Model):
    _inherit = 'gamification.challenge'

    category = fields.Selection(selection_add=[('forum', 'Website / Forum')])
