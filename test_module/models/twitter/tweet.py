# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Tweet(models.Model):
	_name = 'twitter.tweet'
	_rec_name = 'description'

	description = fields.Text(string='Description', size=140, required=True)

	@api.constrains('description')
	def constrain_description(self):
		"""
		Raises a ValidationError if tweets are longer than 140 characters.
		"""
		if self and len(self.description) > 140:
			raise ValidationError('Tweets cannot be longer than 140 characters.')
