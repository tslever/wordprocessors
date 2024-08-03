'''
Module test_tokenizer, which has functions to test cleaning, tokenizing, and counting words in text 
'''


import logging
import pytest
from tokenizer import clean_text, count_words, tokenize


class TestTokenizer:
    '''
    Tests the methods of a TestTokenizer object 

    Instance variables:
        logger

    Public methods:
        test_clean_text
        test_tokenize_text
        test_count_words
    '''

    @pytest.fixture(scope = "class", autouse = True)
    def logger(self):
        '''
        Sets up a logger

        Keyword arguments:
            none

        Return values:
            logger

        Side effects:
            none

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            pytest only should call this method to set up logger.
        '''

        logger = logging.getLogger(__name__)
        return logger


    def test_clean_text(self, logger):
        '''
        Tests cleaning text

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Compares actual and expected cleaned texts

        Exceptions raised:
            AssertionError if actual cleaned text does not equal expected cleaned text

        Restrictions on when this method can be called:
            none
        '''

        logger.info("Testing cleaning text")

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

        assert \
            actual_cleaned_text == expected_cleaned_text, \
            "Actual cleaned text is not equal to expected cleaned text."


    def test_tokenize(self, logger):
        '''
        Tests tokenizing text

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Compares actual and expected lists of words from text

        Exceptions raised:
            AssertionError if actual list of words does not equal expected list of words

        Restrictions on when this method can be called:
            none
        '''

        logger.info("Testing tokenizing text")

        text_to_tokenize = "This is a vast world you can't traverse world in a day"

        actual_list_of_words = tokenize(text_to_tokenize)

        expected_list_of_words = [
            "This",
            "is",
            "a",
            "vast",
            "world",
            "you",
            "can't",
            "traverse",
            "world",
            "in",
            "a",
            "day"
        ]

        assert \
            actual_list_of_words == expected_list_of_words, \
            "Actual list of words is not equal to expected list of words."


    def test_count_words(self, logger):
        '''
        Tests providing a dictionary of words in text and the counts of those words

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Compares actual and expected dictionaries of words and counts

        Exceptions raised:
            AssertionError if actual dictionary does not equal expected dictionary

        Restrictions on when this method can be called:
            none
        '''

        logger.info("Testing counting words")

        text_of_which_to_count_words = "This is a vast world you can't traverse world in a day"

        actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

        expected_dictionary_of_words_and_counts = {
            'a': 2,
            'world': 2,
            "can't": 1,
            'day': 1,
            'traverse': 1, 
            'is': 1,
            'vast': 1,
            'in': 1,
            'you': 1,
            'This': 1
        }

        assert \
            actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
            "Actual dictionary of words and counts does not equal expected dictionary."
