from tokenizer import clean_text, tokenize
import unittest


class TestTokenizer(unittest.TestCase):

    def test_clean_text(self):

        text_to_clean = """And he looked over at the alarm clock,
ticking on the chest of drawers. "God in Heaven!" he thought.
It was half past six and the hands were quietly moving forwards,
it was even later than half past, more like quarter to seven.
Had the alarm clock not rung? He could see from the bed that it
had been set for four o'clock as it should have been; it certainly must have rung.
Yes, but was it possible to quietly sleep through that furniture-rattling noise?
True, he had not slept peacefully, but probably all the more deeply because of that"""

        actual_cleaned_text = clean_text(text_to_clean)

        expected_cleaned_text = """and he looked over at the alarm clock
ticking on the chest of drawers god in heaven he thought
it was half past six and the hands were quietly moving forwards
it was even later than half past more like quarter to seven
had the alarm clock not rung he could see from the bed that it
had been set for four oclock as it should have been it certainly must have rung
yes but was it possible to quietly sleep through that furniturerattling noise
true he had not slept peacefully but probably all the more deeply because of that"""

        self.assertEqual(actual_cleaned_text, expected_cleaned_text, "Actual cleaned text is not equal to expected cleaned text.")


    def test_tokenize(self):

        text_to_tokenize = "This is a vast world you can't traverse world in a day"

        actual_list_of_words = tokenize(text_to_tokenize)

        expected_list_of_words = ["This", "is", "a", "vast", "world", "you", "can't", "traverse", "world", "in", "a", "day"]

        self.assertEqual(actual_list_of_words, expected_list_of_words, "Actual list of words is not equal to expected list of words.")


if __name__ == '__main__':
    verbose = 3
    unittest.main(verbosity = verbose)