'''
Module test_cleaner, which has functions to test cleaning text 
'''

import os
import platform
import subprocess
import sys
import pytest
from fixtures import \
    list_of_paths_to_files_with_english_texts, \
    logger, \
    quote_from_the_raven, \
    temporary_directory, \
    temporary_directory_of_files_with_texts
from utilities import anthology, text_from_file, quote_from_le_corbeau
from pkg_tsl2b import clean_text


def test_cleaning_all_english_texts_together(
    list_of_paths_to_files_with_english_texts,
    logger,
    temporary_directory_of_files_with_texts
):
    '''
    Given a string text with words from English texts with paths in a specified list,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_english_texts: list[str] --
        a list of paths to files with English texts

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned text

    Exceptions raised:
        AssertionError if actual cleaned text does not equal expected cleaned text

    Restrictions on when this method can be called:
        none
    '''
    
    '''
    list_of_texts = []
    for path in list_of_paths_to_files_with_english_texts:
        with open(path, 'r', encoding = "utf-8") as file:
            text = file.read()
            list_of_texts.append(text)
    anthology_of_english_texts = '\n'.join(list_of_texts)
    '''
    anthology_of_english_texts = anthology(list_of_paths_to_files_with_english_texts)
    actual_cleaned_anthology_of_english_texts = clean_text(anthology_of_english_texts)

    expected_cleaned_anthology_of_english_texts = None
    with open(
        temporary_directory_of_files_with_texts / "Anthology_Of_English_Texts_Cleaned.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        expected_cleaned_anthology_of_english_texts = file.read()

    assert \
        actual_cleaned_anthology_of_english_texts == expected_cleaned_anthology_of_english_texts, \
        "Actual and cleaned anthologies of English texts are not equal."


def test_cleaning_each_english_text(
    list_of_paths_to_files_with_english_texts,
    logger,
    temporary_directory_of_files_with_texts
):
    '''
    Given a string text with words from an English text with a path in a specified list,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_english_texts: list[str] --
        a list of paths to files with English texts

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

    for path in list_of_paths_to_files_with_english_texts:

        logger.info(f"Testing cleaning {path}")

        base_name = os.path.basename(path)
        
        text = text_from_file(base_name, temporary_directory_of_files_with_texts)

        actual_cleaned_text = clean_text(text)

        file_name, extension = os.path.splitext(base_name)

        expected_cleaned_text = None
        with open(
            temporary_directory_of_files_with_texts / f"{file_name}_Cleaned{extension}",
            'r',
            encoding = "utf-8"
        ) as file:
            expected_cleaned_text = file.read()

        assert \
            actual_cleaned_text == expected_cleaned_text, \
            f"For {path}, actual cleaned text is not equal to expected cleaned text."


def test_cleaning_quote_from_le_corbeau(logger):
    '''
    Given a string quote_from_Le_Corbeau of text with words from Le Corbeau,
    when I pass quote_from_Le_Corbeau to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned quotes from Le Corbeau

    Exceptions raised:
        AssertionError if actual and expected cleaned quotes are not equal

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing cleaning quote from Le Corbeau")

    actual_cleaned_text = clean_text(quote_from_le_corbeau)

    print(actual_cleaned_text)

    expected_cleaned_text = """mais le corbeau perché solitairement sur ce buste placide parla
    ce seul mot comme si son âme en ce seul mot il la répandait je ne
    proférai donc rien de plus il nagita donc pas de plumejusquà ce
    que je fis à peine davantage que marmotter dautres amis déjà ont
    pris leur voldemain il me laissera comme mes espérances déjà ont
    pris leur vol alors loiseau dit jamais plus"""

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        "Actual cleaned quote from Le Corbeau " + \
        "is not equal to expected cleaned quote from Le Corbeau."


@pytest.mark.skip(reason = "clean_text does not clean Japanese characters.")
def test_cleaning_quote_from_the_great_raven(logger):
    '''
    Given a string quote_from_The_Great_Raven with words from 「大鴉」(Japanese for The Great Raven),
    when I pass quote_from_The_Great_Raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

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

    logger.info("Testing cleaning quote from The Great Raven")

    text = "しかし、大鴉は、穏やかな胸像の上に一人座って、その一言だけを話した。まるでその一言に彼の魂を注ぎ込んだかのように。"

    actual_cleaned_text = clean_text(text)

    expected_cleaned_text = "しかし、大鴉は、穏やかな胸像の上に一人座って、その一言だけを話した。まるでその一言に彼の魂を注ぎ込んだかのように。"

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        "Actual cleaned text is not equal to expected cleaned text."


def test_cleaning_quote_from_the_raven(logger, quote_from_the_raven):
    '''
    Given a string quote_from_the_raven of text with words from The Raven,
    when I pass quote_from_the_raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_the_raven: str -- a quote from The Raven to clean

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned quotes from The Raven

    Exceptions raised:
        AssertionError if actual cleaned quote does not equal expected cleaned quote

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing cleaning quote from The Raven")

    actual_cleaned_text = clean_text(quote_from_the_raven)

    expected_cleaned_text = \
        "but the raven " + \
        "sitting lonely on the placid bust " + \
        "spoke only " + \
        "that one word " + \
        "as if his soul in that one word he did outpour"

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        "Actual cleaned quote from The Raven " + \
        "is not equal to expected cleaned quote from The Raven."


def test_cleaning_the_raven(logger, temporary_directory_of_files_with_texts):
    '''
    Given a string text with words from The Raven,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

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
    with open(
        temporary_directory_of_files_with_texts / "The_Raven.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        text = file.read()

    actual_cleaned_text = clean_text(text)

    expected_cleaned_text = None
    with open(
        temporary_directory_of_files_with_texts / "The_Raven_Cleaned.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        expected_cleaned_text = file.read()

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        "Actual cleaned text is not equal to expected cleaned text."


def test_cleaning_the_raven_only_on_linux(logger, temporary_directory_of_files_with_texts):
    '''
    Given a string text with words from The Raven,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.
    This test should only pass on Linux.

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

    current_os = platform.system()
    if current_os != "Linux":
        pytest.fail("You have not tested cleaning The Raven on {current_os}.")

    text = None
    with open(
        temporary_directory_of_files_with_texts / "The_Raven.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        text = file.read()

    actual_cleaned_text = clean_text(text)

    expected_cleaned_text = None
    with open(
        temporary_directory_of_files_with_texts / "The_Raven_Cleaned.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        expected_cleaned_text = file.read()

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        "Actual cleaned text is not equal to expected cleaned text."


def test_cleaning_the_raven_only_for_python_3_10_12(
    logger,
    temporary_directory_of_files_with_texts
):
    '''
    Given a string text with words from The Raven,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.
    This test should only pass on for Python 3.10.12.

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

    version_tuple = sys.version_info[:3]
    current_version_of_python = \
        str(version_tuple[0]) + \
        "." + \
        str(version_tuple[1]) + \
        "." + \
        str(version_tuple[2])
    print(current_version_of_python)
    if current_version_of_python != "3.10.12":
        pytest.fail(
            "You have not tested cleaning The Raven for Python version {current_version_of_Python}."
        )

    text = None
    with open(
        temporary_directory_of_files_with_texts / "The_Raven.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        text = file.read()

    actual_cleaned_text = clean_text(text)

    expected_cleaned_text = None
    with open(
        temporary_directory_of_files_with_texts / "The_Raven_Cleaned.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        expected_cleaned_text = file.read()

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        "Actual cleaned text is not equal to expected cleaned text."


def test_cleaning_the_raven_using_command_and_function(
    logger,
    temporary_directory_of_files_with_texts
):
    '''
    Given a file with text or a string text with words from The Raven,
    when I pass text to a command or clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares cleaned texts

    Exceptions raised:
        AssertionError if cleaned texts are not equal

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing cleaning text")

    temporary_file = temporary_directory_of_files_with_texts / "The_Raven.txt"
    command = "bash clean_text.sh " + str(temporary_file)
    actual_cleaned_text_from_command = subprocess.run(
        command,
        shell = True,
        capture_output = True,
        text = True,
        check = False
    ).stdout

    text = None
    with open(
        temporary_directory_of_files_with_texts / "The_Raven.txt",
        'r',
        encoding = "utf-8"
    ) as file:
        text = file.read()

    actual_cleaned_text_from_function = clean_text(text)

    assert \
        actual_cleaned_text_from_command == actual_cleaned_text_from_function, \
        "Actual cleaned texts are not equal."


def test_that_characters_in_cleaned_quote_from_the_raven_are_all_lowercase(
    logger,
    quote_from_the_raven
):
    '''
    Given a string quote_from_the_raven of text with words from The Raven,
    when I pass quote_from_the_raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_the_raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether characters in cleaned version of quote from The Raven are all lowercase

    Exceptions raised:
        AssertionError
        if characters in cleaned version of quote from The Raven are not all lowercase

    Restrictions on when this method can be called:
        none
    '''

    logger.info(
        "Testing that characters in cleaned version of quote from The Raven are all lowercase"
    )

    actual_cleaned_text = clean_text(quote_from_the_raven)

    assert \
        actual_cleaned_text.islower(), \
        "Characters in cleaned version of quote from The Raven are not all lowercase."


@pytest.mark.xfail
def test_that_there_is_a_capital_letter_in_cleaned_quote_from_the_raven(
    logger,
    quote_from_the_raven
):
    '''
    Given a string quote_from_the_raven of text with words from The Raven,
    when I pass quote_from_the_raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in augmentation of string.punctuation.
    A test that there is a capital letter in the quote should fail.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_the_raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether there is a capital letter in cleaned quote from The Raven

    Exceptions raised:
        AssertionError if there is not a capital letter in cleaned quote from The Raven

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that there is a capital letter in cleaned quote from The Raven")

    actual_cleaned_text = clean_text(quote_from_the_raven)

    assert \
        not actual_cleaned_text.islower(), \
        "Characters in cleaned version of quote from The Raven are all lowercase."
