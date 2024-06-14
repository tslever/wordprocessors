'''
Module test_word_counter, which has a function to test counting words in text 
'''


from logger import logger
from tsl2b_DS5111su24_lab_01.word_processors import count_words


def test_count_words(logger):
    '''
    Given a string text_of_which_to_count_words
    that is cleanish according to a restriction on using function count_words,
    when I pass text_of_which_to_count_words to count_words,
    I should get a dictionary of those words and their counts.

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
        f"Given text {text_of_which_to_count_words}, actual dictionary of words and counts does not equal expected dictionary."
