'''
Module test_tokenizer, which has functions to test tokenizing text
'''


from tsl2b_DS5111su24_lab_01.word_processors import clean_text
from fixtures import logger
import pickle
import pytest
from fixtures import quote_from_The_Raven
from tsl2b_DS5111su24_lab_01.word_processors import tokenize


def test_tokenize(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words from quote

    Exceptions raised:
        AssertionError if actual list of words does not equal expected list of words

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing text")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    expected_list_of_words = [
        "but",
        "the",
        "raven",
        "sitting",
        "lonely",
        "on",
        "the",
        "placid",
        "bust",
        "spoke",
        "only",
        "that",
        "one",
        "word",
        "as",
        "if",
        "his",
        "soul",
        "in",
        "that",
        "one",
        "word",
        "he",
        "did",
        "outpour"
    ]

    assert \
        actual_list_of_words == expected_list_of_words, \
        f"Actual list of words in quote from The Raven is not equal to expected list of words in quote from The Raven."


def test_tokenize_The_Raven(logger):
    '''
    Given a string of text with words from The Raven,
    when I pass a cleaned version of the text to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words from The Raven

    Exceptions raised:
        AssertionError if actual list of words from The Raven does not equal expected list of words from The Raven

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing The Raven")

    text = None
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    text_to_tokenize = clean_text(text)

    actual_list_of_words = tokenize(text_to_tokenize)

    with open("List_Of_Words_In_The_Raven.pickle", "rb") as file:
        expected_list_of_words = pickle.load(file)
    
    assert \
        actual_list_of_words == expected_list_of_words, \
        f"Actual list of words from The Raven is not equal to expected list of words from The Raven."



def test_that_there_are_no_hyphens_in_words_in_cleaned_version_of_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in string.punctuation.
    The words should not have hyphens.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether there are no hyphens in words in a cleaned version of quote_from_The_Raven

    Exceptions raised:
        AssertionError if there is a hyphen in a word

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that there are no hyphens in words in cleaned version of quote from The Raven")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    there_are_no_hyphens = True
    for word in actual_list_of_words:
        if '-' in word:
            there_are_no_hyphens = False

    assert \
        there_are_no_hyphens, \
        f"There is a hyphen in a word in a cleaned version of a quote from The Raven."


@pytest.mark.xfail
def test_that_a_word_in_cleaned_version_of_quote_from_The_Raven_has_a_hyphen(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in string.punctuation.
    The words should not have hyphens; a test that a word has a hyphen should fail.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether a word in a cleaned version of a quote from The Raven has a hyphen

    Exceptions raised:
        AssertionError if no word has a hyphen

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing text")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    there_are_no_hyphens = True
    for word in actual_list_of_words:
        if '-' in word:
            there_are_no_hyphens = False

    assert \
        not there_are_no_hyphens, \
        f"There are no hyphens in the words in a cleaned version of a quote from The Raven."

