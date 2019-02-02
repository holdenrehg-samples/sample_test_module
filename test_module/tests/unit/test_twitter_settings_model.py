# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase
from odoo.addons.test_module.helpers import string


class TwitterSettingsModel(TransactionCase):
	def test_settings_model_exists(self):
		self.assertTrue('twitter.settings' in self.env)
