'''
Module test_word_counter, which has a function to test counting words in text 
'''


from fixtures import logger, quote_from_The_Raven
from tsl2b_DS5111su24_lab_01.word_processors import clean_text, count_words, tokenize
import pickle
import pytest


def test_count_words(logger, quote_from_The_Raven):
    '''
    Given a string text_of_which_to_count_words
    that is cleanish according to a restriction on using function count_words,
    when I pass text_of_which_to_count_words to count_words,
    I should get a dictionary of those words and their counts.
    The words should consist of lowercase characters not in string.punctuation.

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

    text_of_which_to_count_words = clean_text(quote_from_The_Raven)

    actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

    expected_dictionary_of_words_and_counts = {
        "but": 1,
        "the": 2,
        "raven": 1,
        "sitting": 1,
        "lonely": 1, 
        "on": 1,
        "placid": 1,
        "bust": 1,
        "spoke": 1,
        "only": 1,
        "that": 2,
        "one": 2,
        "word": 2,
        "as": 1,
        "if": 1,
        "his": 1,
        "soul": 1,
        "in": 1,
        "he": 1,
        "did": 1,
        "outpour": 1
    }

    assert \
        actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
        f"Given text {text_of_which_to_count_words}, actual dictionary of words and counts does not equal expected dictionary."


def test_count_words_in_The_Raven(logger):
    '''
    Given a string text_of_which_to_count_words
    that is cleanish according to a restriction on using function count_words,
    when I pass text_of_which_to_count_words to count_words,
    I should get a dictionary of those words and their counts.
    The words should consist of lowercase characters not in string.punctuation.

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

    text = None
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    text_of_which_to_count_words = clean_text(text)

    actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

    expected_dictionary_of_words_and_counts = None
    with open("Dictionary_Of_Words_And_Counts_For_The_Raven.pickle", "rb") as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)

    assert \
        actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
        f"Given text {text_of_which_to_count_words}, actual dictionary of words and counts does not equal expected dictionary."



def test_that_there_are_21_unique_words(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven
    that is cleanish according to a restriction on using function count_words,
    when I pass quote_from_The_Raven to count_words,
    I should get a dictionary of those words and their counts.
    There should be 21 unique words in the dictionary
    consisting of lowercase characters not in string.punctuation.

    Keyword arguments:
        none

    Return values:
        none

    Side effects:
        Determines whether there are 21 unique words
        in the dictionary produced by count_words
        given a cleaned version of quote from The Raven

    Exceptions raised:
        AssertionError if there are not 21 unique words in the dictionary

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that there are 21 unique words in dictionary")

    text_of_which_to_count_words = clean_text(quote_from_The_Raven)

    actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

    assert len(actual_dictionary_of_words_and_counts) == 21


@pytest.mark.xfail
def test_that_the_number_of_unique_words_is_equal_to_the_number_of_words(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven
    that is cleanish according to a restriction on using function count_words,
    when I pass a cleaned version of quote_from_The_Raven to count_words,
    I should get a dictionary of those words and their counts.
    There should be 21 unique words in the dictionary
    consisting of lowercase characters not in string.punctuation.

    Keyword arguments:
        none

    Return values:
        none

    Side effects:
        Determines whether that the number of unique words
        in the dictionary produced by count_words
        given a cleaned version of quote from The Raven
        is equal to the number of words.

    Exceptions raised:
        AssertionError if the number of unique words is not equal to the number of words

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that the number of unique words is equal to the number of words")

    text_of_which_to_count_words = clean_text(quote_from_The_Raven)

    actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

    assert len(actual_dictionary_of_words_and_counts) == len(tokenize(text_of_which_to_count_words))
