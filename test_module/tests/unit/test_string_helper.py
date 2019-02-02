# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase
from odoo.addons.test_module.helpers import string


class StringHelperTest(TransactionCase):
	def test_string_should_truncate_when_greater(self):
		self.assertEqual(len(string.limit('A short string...', size=5)), 5)

	def test_string_should_do_nothing_when_same_size(self):
		sample_str = 'This is my sample string.'
		sample_str_len = len(sample_str)
		self.assertEqual(len(string.limit(sample_str, sample_str_len)), sample_str_len)

	def test_string_should_do_nothing_when_less_than(self):
		sample_str = 'Another cool sample string!'
		sample_str_len = len(sample_str)
		self.assertEqual(len(string.limit(sample_str, sample_str_len)), sample_str_len)
