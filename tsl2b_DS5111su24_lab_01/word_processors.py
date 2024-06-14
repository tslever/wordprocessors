'''
Module word_processors, which has functions to clean, tokenize, and count words in text
'''


import logging
from collections import Counter
import string


logger = logging.getLogger(__name__)


def clean_text(text: str) -> str:
    '''
    Cleans text by lowercasing and removing characters in string.punctuation
        
    Keyword arguments:
        text: str -- text

    Return values:
        cleaned_text: str -- cleaned text

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        none
    '''

    assert isinstance(text, str)

    translation_table = str.maketrans('', '', string.punctuation)
    cleaned_text = text.lower().translate(translation_table)

    logger.info("Cleaned text: %s", cleaned_text)

    assert not cleaned_text is None
    assert isinstance(cleaned_text, str)

    return cleaned_text


def tokenize(text: str) -> list[str]:
    '''
    Tokenizes text of words separated by spaces into a list of those words

    Keyword arguments:
        text: str -- text

    Return values:
        list_of_words: list[str] -- list of words

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        text should be cleanish.
    '''

    assert isinstance(text, str)

    list_of_words = text.split()

    logger.info("Tokenized text: %s", list_of_words)

    assert not list_of_words is None
    assert isinstance(list_of_words, list)

    return list_of_words


def count_words(text: str) -> dict[str, int]:
    '''
    Provides a dictionary of the words in specified text and the counts of those words

    Keyword arguments:
        text: str -- text

    Return values:
        dictionary_of_words_and_counts: str -- dictionary of words in specified text and counts

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        text should be cleanish.
    '''

    assert isinstance(text, str)

    list_of_words = tokenize(text)
    the_counter = Counter(list_of_words)
    dictionary_of_words_and_counts = dict(the_counter)

    logger.info("Counted words: %s", dictionary_of_words_and_counts)

    assert not dictionary_of_words_and_counts is None
    assert isinstance(dictionary_of_words_and_counts, dict)

    return dictionary_of_words_and_counts
