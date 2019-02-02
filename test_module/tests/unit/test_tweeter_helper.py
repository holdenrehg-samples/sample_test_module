# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError
from odoo.addons.test_module.helpers import tweeter


class TweeterHelperTest(TransactionCase):
	def setUp(self):
		super(TweeterHelperTest, self).setUp()

		self.settings = self.env['twitter.settings'].create({'username': 'my_username', 'pasword': 'my_password'})
		self.tweeter = tweeter.Tweeter(self.settings)

	def test_tweeter_creates_tweet_with_valid_data(self):
		tweet = self.tweeter.tweet(description='Great new day.')
		self.assertTrue(bool(self.env['twitter.tweet'].search([('id', '=', tweet.id)], limit=1)))

	def test_tweeter_create_tweet_throws_exception_with_invalid_data(self):
		with self.assertRaises(ValidationError):
			self.tweeter.tweet(description='=' * 150)
