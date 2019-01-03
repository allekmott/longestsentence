
import unittest

from sentence import Sentence

class SentenceTest(unittest.TestCase):
	def test_rejects_empty_text(self):
		with self.assertRaises(ValueError):
			sentence = Sentence("")

	def test_rejects_nonterminated_text(self):
		with self.assertRaises(ValueError):
			sentence = Sentence("this is almost a sentence")

	def test_accepts_period(self):
		sentence = Sentence("this is a sentence.")

	def test_accepts_question_mark(self):
		sentence = Sentence("this is a sentence?")

	def test_accepts_exclamation_mark(self):
		sentence = Sentence("this is a sentence!")

	def test_rejects_non_string_text(self):
		with self.assertRaises(TypeError):
			sentence = Sentence(2)

	def test_longest_word_happy_path(self):
		longest_word_expected = "antidisestablismentarianism"
		text = "hello, my name is antidisestablismentarianism."

		sentence = Sentence(text)

		(longest_word_actual, length) = sentence.get_longest_word()
		self.assertEqual(longest_word_actual, longest_word_expected)
		self.assertEqual(len(longest_word_actual), len(longest_word_expected))

	def test_one_word(self):
		word_expected = "sentence"
		text = "sentence."

		sentence = Sentence(text)

		(word_actual, length) = sentence.get_longest_word()
		self.assertEqual(word_actual, word_expected)
		self.assertEqual(len(word_actual), len(word_expected))

	def test_ignores_extra_whitespace(self):
		longest_word_expected = "antidisestablismentarianism"
		text = "hello, 		my   name  is      antidisestablismentarianism."

		sentence = Sentence(text)

		(longest_word_actual, length) = sentence.get_longest_word()
		self.assertEqual(longest_word_actual, longest_word_expected)
		self.assertEqual(len(longest_word_actual), len(longest_word_expected))
