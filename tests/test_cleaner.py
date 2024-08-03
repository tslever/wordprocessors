'''
Module test_cleaner, which has functions to test cleaning text 
'''


from tsl2b_DS5111su24_lab_01.word_processors import clean_text
from fixtures import list_of_paths_to_files_with_English_texts
from fixtures import logger
import os
import platform
import pytest
from fixtures import quote_from_The_Raven
import subprocess
import sys


def test_cleaning_all_English_texts_together(logger, list_of_paths_to_files_with_English_texts):
    '''
    Given a string text with words from English texts with paths in a specified list,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_English_texts: list[str] -- a list of paths to files with English texts

    Return values:
        none

    Side effects:
        Compares actual and expected cleaned text

    Exceptions raised:
        AssertionError if actual cleaned text does not equal expected cleaned text

    Restrictions on when this method can be called:
        none
    '''

    list_of_texts = []
    for path in list_of_paths_to_files_with_English_texts:
        with open(path, 'r') as file:
            text = file.read()
            list_of_texts.append(text)
    anthology_of_English_texts = '\n'.join(list_of_texts)
    actual_cleaned_anthology_of_English_texts = clean_text(anthology_of_English_texts)

    expected_cleaned_anthology_of_English_texts = None
    with open("Cleaned_Anthology_Of_English_Texts.txt", 'r') as file:
        expected_cleaned_anthology_of_English_texts = file.read()

    assert \
        actual_cleaned_anthology_of_English_texts == expected_cleaned_anthology_of_English_texts, \
        "Actual and cleaned anthologies of English texts are not equal."
    

def test_cleaning_each_English_text(logger, list_of_paths_to_files_with_English_texts):
    '''
    Given a string text with words from an English text with a path in a specified list,
    when I pass text to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_English_texts: list[str] -- a list of paths to files with English texts

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

    for path in list_of_paths_to_files_with_English_texts:

        logger.info(f"Testing cleaning {path}")

        base_name = os.path.basename(path)
        text = None
        with open(base_name, 'r') as file:
            text = file.read()

        actual_cleaned_text = clean_text(text)

        file_name, extension = os.path.splitext(base_name)

        expected_cleaned_text = None
        with open(f"{file_name}_Cleaned{extension}", 'r') as file:
            expected_cleaned_text = file.read()

        assert \
            actual_cleaned_text == expected_cleaned_text, \
            f"For {path}, actual cleaned text is not equal to expected cleaned text."


def test_cleaning_quote_from_Le_Corbeau(logger):
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

    quote_from_Le_Corbeau = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

    actual_cleaned_text = clean_text(quote_from_Le_Corbeau)

    print(actual_cleaned_text)

    expected_cleaned_text = """mais le corbeau perché solitairement sur ce buste placide parla
    ce seul mot comme si son âme en ce seul mot il la répandait je ne
    proférai donc rien de plus il nagita donc pas de plumejusquà ce
    que je fis à peine davantage que marmotter dautres amis déjà ont
    pris leur voldemain il me laissera comme mes espérances déjà ont
    pris leur vol alors loiseau dit jamais plus"""

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Actual cleaned quote from Le Corbeau is not equal to expected cleaned quote from Le Corbeau."



@pytest.mark.skip(reason = "clean_text does not clean Japanese characters.")
def test_cleaning_quote_from_The_Great_Raven(logger):
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
        f"Actual cleaned text is not equal to expected cleaned text."


def test_cleaning_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass quote_from_The_Raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

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

    logger.info("Testing cleaning quote from The Raven")

    actual_cleaned_text = clean_text(quote_from_The_Raven)

    expected_cleaned_text = """but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"""

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Actual cleaned quote from The Raven is not equal to expected cleaned quote from The Raven."


def test_cleaning_The_Raven(logger):
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
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    actual_cleaned_text = clean_text(text)

    expected_cleaned_text = None
    with open("The_Raven_Cleaned.txt", 'r') as file:
        expected_cleaned_text = file.read()

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Actual cleaned text is not equal to expected cleaned text."


def test_cleaning_The_Raven_only_on_Linux(logger):
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
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    actual_cleaned_text = clean_text(text)

    expected_cleaned_text = None
    with open("The_Raven_Cleaned.txt", 'r') as file:
        expected_cleaned_text = file.read()

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Actual cleaned text is not equal to expected cleaned text."


def test_cleaning_The_Raven_only_for_Python_3_10_12(logger):
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
    current_version_of_Python = str(version_tuple[0]) + "." + str(version_tuple[1]) + "." + str(version_tuple[2])
    print(current_version_of_Python)
    if current_version_of_Python != "3.10.12":
        pytest.fail("You have not tested cleaning The Raven for Python version {current_version_of_Python}.")

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


def test_cleaning_The_Raven_using_command_and_function(logger):
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

    # Command to run in bash: cat The_Raven.txt | gawk '{print tolower($0)}' | tr -d "\!\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~"
    command = "cat The_Raven.txt | gawk '{print tolower($0)}' | tr -d \"!\\\"#$%&'()*+,-./:;<=>?@[\\\\]^_\\`{|}~\" | sed 's/«//g' | sed 's/»//g'"

    actual_cleaned_text_from_command = subprocess.run(command, shell = True, capture_output = True, text = True).stdout
    with open("The_Raven_Cleaned_By_Command.txt", 'r') as file:
        actual_cleaned_text_from_command = file.read()

    text = None
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    actual_cleaned_text_from_function = clean_text(text)

    assert \
        actual_cleaned_text_from_command == actual_cleaned_text_from_function, \
        f"Actual cleaned texts are not equal."


def test_that_characters_in_cleaned_quote_from_The_Raven_are_all_lowercase(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass quote_from_The_Raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether characters in cleaned version of quote from The Raven are all lowercase

    Exceptions raised:
        AssertionError if characters in cleaned version of quote from The Raven are not all lowercase

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that characters in cleaned version of quote from The Raven are all lowercase")

    actual_cleaned_text = clean_text(quote_from_The_Raven)

    assert \
        actual_cleaned_text.islower(), \
        f"Characters in cleaned version of quote from The Raven are not all lowercase."


@pytest.mark.xfail
def test_that_there_is_a_capital_letter_in_cleaned_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass quote_from_The_Raven to function clean_text,
    I should get a string as return
    representing a cleaned version of that quote.
    The string should consist of lowercase characters not in augmentation of string.punctuation.
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

    logger.info("Testing that there is a capital letter in cleaned quote from The Raven")

    actual_cleaned_text = clean_text(quote_from_The_Raven)

    assert \
        not actual_cleaned_text.islower(), \
        f"Characters in cleaned version of quote from The Raven are all lowercase."
