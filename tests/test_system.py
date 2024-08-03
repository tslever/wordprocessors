'''
Module test_system, which has functions to test the word processing system 
'''


from src.pkg_tsl2b.word_processors import clean_text
from src.pkg_tsl2b.word_processors import count_words
from fixtures import logger
import pickle
import pytest
import requests
from fixtures import temporary_directory
from fixtures import temporary_directory_of_files_with_texts
from src.pkg_tsl2b.word_processors import tokenize


@pytest.mark.integration
def test_downloading_cleaning_tokenizing_and_counting_words_in_The_Raven(logger, temporary_directory_of_files_with_texts):
    '''
    Given a string text with words from The Raven,
    when I clean, tokenize, and count words in text,
    I should get previously created cleaned text, a list of words in cleaned text, and a dictionary of words in cleaned text and their counts as return.

    Keyword arguments:
        logger: Logger -- a logger
        temporary_directory_of_files_with_texts: pathlib.PosixPath -- a PosixPath representing a temporary directory of files with texts

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned texts, lists of words in cleaned texts, and dictionaries of words in cleaned texts and their counts

    Exceptions raised:
        AssertionError if actual and expected objects are not equal

    Restrictions on when this method can be called:
        none
    '''

    ID_of_The_Raven = 17192
    URL = f"https://www.gutenberg.org/cache/epub/{ID_of_The_Raven}/pg{ID_of_The_Raven}.txt"
    response = requests.get(URL)
    text = response.text
    cleaned_text = clean_text(text)
    assert cleaned_text == (temporary_directory_of_files_with_texts / "The_Raven_Cleaned.txt").read_text()
    actual_list_of_words = tokenize(cleaned_text)
    expected_list_of_words = None
    with open(temporary_directory_of_files_with_texts / "List_Of_Words_In_Cleaned_Version_Of_The_Raven.pickle", "rb") as file:
        expected_list_of_words = pickle.load(file)
    assert actual_list_of_words == expected_list_of_words
    actual_dictionary_of_words_and_counts = count_words(cleaned_text)
    expected_dictionary_of_words_and_counts = None
    with open(temporary_directory_of_files_with_texts / "Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_The_Raven.pickle", "rb") as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)
    assert actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts


@pytest.mark.integration
def test_downloading_cleaning_tokenizing_and_counting_words_in_anthology_of_English_texts(logger, temporary_directory_of_files_with_texts):
    '''
    Given a string text with words from an anthology of English texts,
    when I clean, tokenize, and count words in text,
    I should get previously created cleaned text, a list of words in cleaned text, and a dictionary of words in cleaned text and their counts as return.

    Keyword arguments:
        logger: Logger -- a logger
        temporary_directory_of_files_with_texts: pathlib.PosixPath -- a PosixPath representing a temporary directory of files with texts

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned texts, lists of words in cleaned texts, and dictionaries of words in cleaned texts and their counts

    Exceptions raised:
        AssertionError if actual and expected objects are not equal

    Restrictions on when this method can be called:
        none
    '''

    dictionary_of_IDs_and_base_names_of_English_texts = {
        17192: "The_Raven.txt",
        932: "The_Fall_of_the_House_of_Usher.txt",
        1063: "The_Cask_of_Amontillado.txt",
        10031: "The_Complete_Poetical_Works_of_Edgar_Allan_Poe.txt"
    }
    list_of_texts = []
    for ID in dictionary_of_IDs_and_base_names_of_English_texts.keys():
        URL = f"https://www.gutenberg.org/cache/epub/{ID}/pg{ID}.txt"
        response = requests.get(URL)
        text = response.text
        list_of_texts.append(text)
    anthology_of_English_texts = '\n'.join(list_of_texts)
    cleaned_anthology_of_English_texts = clean_text(anthology_of_English_texts)
    assert cleaned_anthology_of_English_texts == (temporary_directory_of_files_with_texts / "Anthology_Of_English_Texts_Cleaned.txt").read_text()
    actual_list_of_words = tokenize(cleaned_anthology_of_English_texts)
    expected_list_of_words = None
    with open(temporary_directory_of_files_with_texts / "List_Of_Words_In_Cleaned_Version_Of_Anthology_Of_English_Texts.pickle", "rb") as file:
        expected_list_of_words = pickle.load(file)
    assert actual_list_of_words == expected_list_of_words
    actual_dictionary_of_words_and_counts = count_words(cleaned_anthology_of_English_texts)
    expected_dictionary_of_words_and_counts = None
    with open(temporary_directory_of_files_with_texts / "Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_Anthology_Of_English_Texts.pickle", "rb") as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)
    assert actual_dictionary_of_words_and_counts == expected_dictionary_of_words_and_counts
