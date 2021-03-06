# -*- coding: utf-8 -*-
#
#
#    Author: Yannick Vaucher
#    Copyright 2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{"name": "NGO - Purchase Order",
 "summary": "Base Purchase Order view for NGO",
 "version": "1.0.1",
 "author": "Camptocamp,Odoo Community Association (OCA)",
 "license": "AGPL-3",
 "category": "Purchase Management",
 'complexity': "normal",
 "images": [],
 "website": "http://www.camptocamp.com",
 "depends": ["framework_agreement",
             "framework_agreement_requisition",
             "purchase_origin_address",
             "purchase_delivery_address",
             "purchase_requisition",
             "purchase_requisition_bid_selection",
             "purchase_rfq_bid_workflow",
             "purchase_transport_document",
             ],
 "demo": [],
 "data": ["view/purchase_order.xml",
          ],
 "test": [],
 'installable': True,
 'auto_install': False,
 }
