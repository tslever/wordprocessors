'''
Module test_tokenizer, which has a function to test tokenizing text
'''


from logger import logger
from tsl2b_DS5111su24_lab_01.word_processors import tokenize


def test_tokenize(logger):
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
