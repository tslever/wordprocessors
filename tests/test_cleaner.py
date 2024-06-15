'''
Module test_cleaner, which has functions to test cleaning text 
'''


from tsl2b_DS5111su24_lab_01.word_processors import clean_text
from fixtures import list_of_file_names_of_English_texts
from fixtures import logger
import os
import pytest
from fixtures import quote_from_The_Raven


def test_clean_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass quote_from_The_Raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven to clean

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned quotes from The Raven

    Exceptions raised:
        AssertionError if actual cleaned quote does not equal expected cleaned quote

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing cleaning text")

    actual_cleaned_text = clean_text(quote_from_The_Raven)

    expected_cleaned_text = """but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"""

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Actual cleaned quote from The Raven is not equal to expected cleaned quote from The Raven."


def test_clean_The_Raven(logger):
    '''
    Given a string text with words from The Raven,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned texts

    Exceptions raised:
        AssertionError if actual cleaned text does not equal expected cleaned text

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing cleaning text")

    text = None
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    actual_cleaned_text = clean_text(text)

    expected_cleaned_text = None
    with open("The_Raven_Cleaned.txt", 'r') as file:
        expected_cleaned_text = file.read()

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Actual cleaned text is not equal to expected cleaned text."



def test_clean_texts(logger, list_of_file_names_of_English_texts):
    '''
    Given a string text with words from an English text with a file name in a specified list,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_file_names_of_English_texts: list[str] -- list of file names of English texts

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned texts

    Exceptions raised:
        AssertionError if an actual cleaned text does not equal an expected cleaned text

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing cleaning texts")

    file_name = list_of_file_names_of_English_texts[0]

    base_name = os.path.basename(file_name)

    text = None
    with open(base_name, 'r') as file:
        text = file.read()

    actual_cleaned_text = clean_text(text)

    prefix, extension = os.path.splitext(base_name)

    expected_cleaned_text = None
    with open(f"{prefix}_Cleaned{extension}", 'r') as file:
        expected_cleaned_text = file.read()

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Actual cleaned text is not equal to expected cleaned text."


def test_that_characters_in_cleaned_quote_from_The_Raven_are_all_lowercase(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass quote_from_The_Raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether characters in quote from The Raven are all lowercase

    Exceptions raised:
        AssertionError if characters in quote from The Raven are not all lowercase

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that characters in quote from The Raven are all lowercase")

    actual_cleaned_text = clean_text(quote_from_The_Raven)

    assert \
        actual_cleaned_text.islower(), \
        f"Characters in quote from The Raven are not all lowercase."


@pytest.mark.xfail
def test_that_there_is_a_capital_letter_in_cleaned_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass quote_from_The_Raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in string.punctuation.
    A test that there is a capital letter in the quote should fail.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether there is a capital letter in cleaned quote from The Raven

    Exceptions raised:
        AssertionError if there is not a capital letter in cleaned quote from The Raven

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing cleaning text")

    actual_cleaned_text = clean_text(quote_from_The_Raven)

    assert \
        not actual_cleaned_text.islower(), \
        f"Characters in quote from The Raven are not all lowercase; there is at least one capital letter."
