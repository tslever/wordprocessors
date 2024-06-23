'''
Module test_system, which has functions to test the word processing system 
'''


from wordprocessors.word_processors import clean_text
from fixtures import logger
import requests
from fixtures import temporary_directory
from fixtures import temporary_directory_of_files_with_texts


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
    text_from_temporary_file = None
    with open(temporary_directory_of_files_with_texts / "The_Raven_Cleaned.txt", 'r') as file:
        text_from_temporary_file = file.read()
    assert cleaned_text == text_from_temporary_file
