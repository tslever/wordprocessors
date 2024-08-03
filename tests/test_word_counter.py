'''
Module test_word_counter, which has functions to test counting words in text 
'''


from wordprocessors.word_processors import clean_text
from wordprocessors.word_processors import count_words
import json
from fixtures import list_of_paths_to_files_with_English_texts
from fixtures import logger
import os
import pickle
import pytest
from fixtures import quote_from_The_Raven
import subprocess
from fixtures import temporary_directory
from fixtures import temporary_directory_of_files_with_texts
from wordprocessors.word_processors import tokenize


def test_counting_words_for_all_English_texts_together(list_of_paths_to_files_with_English_texts, logger, temporary_directory_of_files_with_texts):
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
    with open(temporary_directory_of_files_with_texts / "Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_Anthology_Of_English_Texts.pickle", 'rb') as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)

    assert \
        actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
        "Actual and expected dictionaries of words in cleaned version of anthology of English texts and their counts are not equal."


def test_count_words_in_each_English_text(list_of_paths_to_files_with_English_texts, logger, temporary_directory_of_files_with_texts):
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
        with open(temporary_directory_of_files_with_texts / base_name, 'r') as file:
            text = file.read()

        cleaned_text = clean_text(text)

        actual_dictionary_of_words_and_counts = count_words(cleaned_text)

        file_name, extension = os.path.splitext(base_name)

        expected_dictionary_of_words_and_counts = None
        with open(temporary_directory_of_files_with_texts / f"Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_{file_name}.pickle", 'rb') as file:
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


def test_counting_words_in_quote_from_Le_Corbeau(logger):
    '''
    Given a string quote_from_Le_Corbeau of text with words from Le Corbeau,
    when I pass a cleaned version of quote_from_Le_Corbeau to function count_words,
    I should get a dictionary of words in the version and their counts as return.
    Each word should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares actual and expected dictionaries of words in cleaned version of Le Corbeau and their counts

    Exceptions raised:
        AssertionError if actual and expected dictionaries are not equal

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing counting words in cleaned version of quote from Le Corbeau")

    quote_from_Le_Corbeau = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

    cleaned_text = clean_text(quote_from_Le_Corbeau)

    actual_dictionary_of_words_and_counts = count_words(cleaned_text)

    expected_dictionary_of_words_and_counts = {
        "mais": 1,
        "le": 1,
        "corbeau": 1,
        "perché": 1,
        "solitairement": 1,
        "sur": 1,
        "ce": 4,
        "buste": 1,
        "placide": 1,
        "parla": 1,
        "seul": 2,
        "mot": 2,
        "comme": 2,
        "si": 1,
        "son": 1,
        "âme": 1,
        "en": 1,
        "il": 3,
        "la": 1,
        "répandait": 1,
        "je": 2,
        "ne": 1,
        "proférai": 1,
        "donc": 2,
        "rien": 1,
        "de": 2,
        "plus": 2,
        "nagita": 1,
        "pas": 1,
        "plumejusquà": 1,
        "que": 2,
        "fis": 1,
        "à": 1,
        "peine": 1,
        "davantage": 1,
        "marmotter": 1,
        "dautres": 1,
        "amis": 1,
        "déjà": 2,
        "ont": 2,
        "pris": 2,
        "leur": 2,
        "voldemain": 1,
        "me": 1,
        "laissera": 1,
        "mes": 1,
        "espérances": 1,
        "vol": 1,
        "alors": 1,
        "loiseau": 1,
        "dit": 1,
        "jamais": 1
    }

    assert \
        actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
        "Actual and expected dictionaries of words and counts in cleaned version of Le Corbeau are not equal."


def test_counting_words_in_The_Raven(logger, temporary_directory_of_files_with_texts):
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
    with open(temporary_directory_of_files_with_texts / "The_Raven.txt", 'r') as file:
        text = file.read()

    text_of_which_to_count_words = clean_text(text)

    actual_dictionary_of_words_and_counts = count_words(text_of_which_to_count_words)

    expected_dictionary_of_words_and_counts = None
    with open(temporary_directory_of_files_with_texts / "Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_The_Raven.pickle", "rb") as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)

    assert \
        actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts, \
        f"Actual dictionary of words in cleaned version of The Raven and their counts does not equal expected dictionary."


def test_counting_words_in_The_Raven_using_command_and_function(logger, temporary_directory_of_files_with_texts):
    '''
    Given a file with text or a string text with words from The Raven,
    when I pass a cleaned version of text to a command or count_words,
    I should get a dictionary of words in the version.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares dictionaries of words in cleaned version of text

    Exceptions raised:
        AssertionError if dictionaries are not equal

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing text")

    file_name = temporary_directory_of_files_with_texts / "The_Raven.txt"
    command = "bash clean_text.sh " + str(file_name) + " | tr '\n' ' ' | sed 's/  */ /g' | sed 's/[[:space:]]*$//' | jq -R 'split(\" \")' | jq -c 'reduce .[] as $word ({}; .[$word] += 1)'"

    serialized_dictionary_of_words_and_counts = subprocess.run(command, shell = True, capture_output = True, text = True).stdout
    dictionary_of_words_and_counts_from_command = json.loads(serialized_dictionary_of_words_and_counts)

    text = None
    with open(temporary_directory_of_files_with_texts / "The_Raven_Cleaned.txt", 'r') as file:
        text = file.read()
    dictionary_of_words_and_counts_from_function = count_words(text)

    assert \
        dictionary_of_words_and_counts_from_command == dictionary_of_words_and_counts_from_command, \
        f"Dictionaries of words and counts are not equal."


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
