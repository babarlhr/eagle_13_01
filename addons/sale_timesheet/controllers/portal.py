# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle.http import request
from eagle.osv import expression

from eagle.addons.account.controllers.portal import PortalAccount


class PortalAccount(PortalAccount):

    def _invoice_get_page_view_values(self, invoice, access_token, **kwargs):
        values = super(PortalAccount, self)._invoice_get_page_view_values(invoice, access_token, **kwargs)
        domain = request.env['account.analytic.line']._timesheet_get_portal_domain()
        domain = expression.AND([domain, [('timesheet_invoice_id', '=', invoice.id)]])
        values['timesheets'] = request.env['account.analytic.line'].sudo().search(domain)
        return values
