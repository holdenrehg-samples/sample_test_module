# -*- coding: utf-8 -*-

def limit(str, size):
	"""
	Truncate a string down to a certain size limit.

	In the case where the string is less than `size` it will
	return the string as is.

	:param str: The string to truncate.
	:param size: The max number of characters the string can be.
	:return: The size limited string.
	"""
	if len(str) <= size:
		return str
	return str[0:size] 