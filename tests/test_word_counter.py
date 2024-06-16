'''
Module test_word_counter, which has functions to test counting words in text 
'''


from tsl2b_DS5111su24_lab_01.word_processors import clean_text
from tsl2b_DS5111su24_lab_01.word_processors import count_words
from fixtures import list_of_paths_to_files_with_English_texts
from fixtures import logger
import os
import pickle
import pytest
from fixtures import quote_from_The_Raven
from tsl2b_DS5111su24_lab_01.word_processors import tokenize


def test_counting_words_for_all_English_texts_together(logger, list_of_paths_to_files_with_English_texts):
    '''
    Given a string text with words from English texts with paths in a specified list,
    when I pass a cleaned version of text to function count_words,
    I should get a lists of words in the version as return.
    Each word should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_English_texts: list[str] -- a list of paths to files with English texts

    Return values:
        none

    Side effects:
        Compares actual and expected dictionaries of words in a cleaned version of text and their counts

    Exceptions raised:
        AssertionError if actual and expected dictionaries are not equal

    Restrictions on when this method can be called:
        none
    '''

    list_of_texts = []
    for path in list_of_paths_to_files_with_English_texts:
        with open(path, 'r') as file:
            text = file.read()
            list_of_texts.append(text)
    anthology_of_English_texts = '\n'.join(list_of_texts)
    cleaned_anthology_of_English_texts = clean_text(anthology_of_English_texts)

    actual_dictionary_of_words_and_counts = count_words(cleaned_anthology_of_English_texts)

    expected_dictionary_of_words_and_counts = None
    with open("Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_Anthology_Of_English_Texts.pickle", 'rb') as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)

    assert \
        actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
        "Actual and expected dictionaries of words in cleaned version of anthology of English texts and their counts are not equal."


def test_count_words_in_each_English_text(logger, list_of_paths_to_files_with_English_texts):
    '''
    Given a string text with words from an English text with a path in a specified list,
    when I pass a cleaned version of the text to function count_words,
    I should get a dictionary of the words in the version and their counts.
    Each word should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_English_texts: list[str] -- a list of paths to files with English texts

    Return values:
        none

    Side effects:
        Compares actual and expected dictionaries of the words in a cleaned version of a text and their counts

    Exceptions raised:
        AssertionError if actual and expected dictionaries are not equal

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing counting words in clean versions of texts")

    for path in list_of_paths_to_files_with_English_texts:

        logger.info(f"Testing counting words in cleaned version of text in file at {path}")

        base_name = os.path.basename(path)
        text = None
        with open(base_name, 'r') as file:
            text = file.read()

        cleaned_text = clean_text(text)

        actual_dictionary_of_words_and_counts = count_words(cleaned_text)

        file_name, extension = os.path.splitext(base_name)

        expected_dictionary_of_words_and_counts = None
        with open(f"Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_{file_name}.pickle", 'rb') as file:
            expected_dictionary_of_words_and_counts = pickle.load(file)

        assert \
            actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
            f"For {path}, actual and expected dictionaries of words in cleaned version of text are not equal."


def test_counting_words_for_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of words from a quote from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to count_words,
    I should get a dictionary of the words in the version and their counts.
    The words should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Compares actual and expected dictionaries of words in a cleaned version of a quote from The Raven and their counts

    Exceptions raised:
        AssertionError if actual dictionary does not equal expected dictionary

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing counting words in a cleaned version of a quote from The Raven")

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
        f"Actual dictionary of words in a cleaned version of a quote from The Raven and their counts does not equal expected dictionary."


def test_count_words_in_The_Raven(logger):
    '''
    Given a string text of words in The Raven,
    when I pass a cleaned version of text to count_words,
    I should get a dictionary of the words in the version and their counts.
    The words should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares actual and expected dictionaries of words in a cleaned version of The Raven and their counts

    Exceptions raised:
        AssertionError if actual dictionary does not equal expected dictionary

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing counting words in a cleaned version of The Raven")

    text = None
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    text_of_which_to_count_words = clean_text(text)

    actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

    expected_dictionary_of_words_and_counts = None
    with open("Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_The_Raven.pickle", "rb") as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)

    assert \
        actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
        f"Actual dictionary of words in cleaned version of The Raven and their counts does not equal expected dictionary."


@pytest.mark.xfail
def test_that_number_of_unique_words_in_cleaned_version_of_quote_is_equal_to_number_of_words_in_version(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of words from a quote from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to count_words,
    I should get a dictionary of those words and their counts.
    There should be 21 unique words in the dictionary
    consisting of lowercase characters not in augmentation of string.punctuation.
    The number of instances of words in the version should not be 21.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether the number of unique words
        in the dictionary produced by count_words
        given a cleaned version of quote from The Raven
        is equal to the number of instances of words in the version.

    Exceptions raised:
        AssertionError if the number of unique words is not equal to the number of words

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that the number of unique words in a cleaned version of a quote from The Raven is equal to the number of instances of words")

    text_of_which_to_count_words = clean_text(quote_from_The_Raven)

    actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

    assert len(actual_dictionary_of_words_and_counts) == len(tokenize(text_of_which_to_count_words))


def test_that_there_are_21_unique_words_in_cleaned_version_of_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of words from a quote from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to count_words,
    I should get a dictionary of the words in the version and their counts.
    There should be 21 unique words in the dictionary
    consisting of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

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
