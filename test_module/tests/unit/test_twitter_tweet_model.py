# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError
from odoo.addons.test_module.helpers import string


class TwitterTweetModel(TransactionCase):
	def setUp(self):
		super(TwitterTweetModel, self).setUp()
		self.tweet_obj = self.env['twitter.tweet']

	def test_tweet_model_exists(self):
		self.assertTrue(self.tweet_obj._name in self.env)

	def test_tweet_creates_with_valid_data(self):
		tweet = self.tweet_obj.create({'description': 'A sweet tweet.'})
		self.assertTrue(bool(self.tweet_obj.search([('id', '=', tweet.id)], limit=1)))

	def test_tweet_creation_throws_exception_with_invalid_data(self):
		with self.assertRaises(ValidationError):
			self.tweet_obj.create({'description': 'abcd' * 150})
