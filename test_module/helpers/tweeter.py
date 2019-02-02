# -*- coding: utf-8 -*-

class Tweeter():
	def __init__(self, settings):
		"""
		Initialize the Tweeter object.
		"""
		self.settings = settings

	def tweet(self, description):
		"""
		Create a tweet.

		:param description: The content of the tweet.
		:return: The generated tweet.
		"""
		return self.settings.env['twitter.tweet'].create({
			'description': description, })