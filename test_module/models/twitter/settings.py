# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class TwitterSettings(models.Model):
	_name = 'twitter.settings'

	username = fields.Char(string='Username')
	password = fields.Char(string='Password')
	connected = fields.Boolean(string='Connected', default=False)

	def connect(self):
		"""
		Attempt to connect to Twitter.
		"""
		self.ensure_one()
		self.update({'connected': True, })