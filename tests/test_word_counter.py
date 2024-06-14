'''
Module test_word_counter, which has a function to test counting words in text 
'''


from fixtures import logger, quote_from_The_Raven
from tsl2b_DS5111su24_lab_01.word_processors import clean_text, count_words


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
