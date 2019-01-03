
import re

"""Container for a sentence, stored in a string"""
class Sentence(object):
	"""Create new sentence object"""
	def __init__(self, text):
		self._text = None
		self.text = text

	"""Get the sentence's text"""
	@property
	def text(self):
		return self._text

	"""Set the sentence's text

	Validates for length, termination, words, etc.

	Assumes text is not high-bit unicode, and only one sentence is to be
	contained. Will not attempt to deduce if two sentences are present.

	Text must be terminated with '.', '?', or '!'"""
	@text.setter
	def text(self, text):
		if type(text) is not str:
			raise TypeError("Sentence text must be of type str")
		elif not len(text) or text[-1] not in [ ".", "?", "!" ]:
			raise ValueError(
				"Sentence must be terminated with a period")
		elif not len(text) or not len(self.parse_words(text)):
			raise ValueError("Sentence text must contain words")

		self._text = text

	"""Parse all words from a string of text. Filters out everything but
	word chars."""
	@staticmethod
	def parse_words(text):
		pieces = re.split("\W+", text)
		words = filter(lambda piece: len(piece), pieces)

		return words

	"""Get longest word, along with length, contained in the sentence's
	text.

	Returns tuple: (word, word_length)"""
	def get_longest_word(self):
		words = self.parse_words(self.text)

		def longer_word(word_a, word_b):
			if len(word_b) > len(word_a):
				return word_b
			else:
				return word_a

		longest_word = reduce(longer_word, words)
		return (longest_word, len(longest_word),)
