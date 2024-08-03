'''
Module test_tokenizer, which has functions to test tokenizing text
'''


from tsl2b_DS5111su24_lab_01.word_processors import clean_text
import json
from fixtures import list_of_paths_to_files_with_English_texts
from fixtures import logger
import os
import pickle
import pytest
from fixtures import quote_from_The_Raven
import subprocess
from tsl2b_DS5111su24_lab_01.word_processors import tokenize


def test_tokenizing_all_English_texts_together(logger, list_of_paths_to_files_with_English_texts):
    '''
    Given a string text with words from English texts with paths in a specified list,
    when I pass a cleaned version of text to function tokenize,
    I should get a lists of words in the version as return.
    Each word should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_English_texts: list[str] -- a list of paths to files with English texts

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words in a cleaned version of text

    Exceptions raised:
        AssertionError if actual and expected lists of words in a cleaned version of text are not equal

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

    actual_list_of_words = tokenize(cleaned_anthology_of_English_texts)

    expected_list_of_words = None
    with open("List_Of_Words_In_Cleaned_Version_Of_Anthology_Of_English_Texts.pickle", 'rb') as file:
        expected_list_of_words = pickle.load(file)

    assert \
        actual_list_of_words == expected_list_of_words, \
        "Actual and expected lists of words in cleaned version of anthology of English texts are not equal."


def test_tokenizing_each_English_text(logger, list_of_paths_to_files_with_English_texts):
    '''
    Given a string text with words from an English text with a path in a specified list,
    when I pass a cleaned version of the text to function tokenize,
    I should get a list of words in the version.
    Each word should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        list_of_paths_to_files_with_English_texts: list[str] -- a list of paths to files with English texts

    Return values:
        none

    Side effects:
        Compares an actual list of words in a cleaned version of a text to an expected list of words in a cleaned version of a text

    Exceptions raised:
        AssertionError if an actual list of words in a cleaned version of a text does not equal an expected list of words in a cleaned version of a text

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing clean versions of texts")

    for path in list_of_paths_to_files_with_English_texts:

        logger.info(f"Testing tokenizing cleaned version of text in file at {path}")

        base_name = os.path.basename(path)
        text = None
        with open(base_name, 'r') as file:
            text = file.read()

        cleaned_text = clean_text(text)

        actual_list_of_words = tokenize(cleaned_text)

        file_name, extension = os.path.splitext(base_name)

        expected_list_of_words = None
        with open(f"List_Of_Words_In_Cleaned_Version_Of_{file_name}.pickle", 'rb') as file:
            expected_list_of_words = pickle.load(file)

        assert \
            actual_list_of_words == expected_list_of_words, \
            f"For {path}, actual list of words in cleaned version of text is not equal to expected list of words in cleaned version of text."


def test_tokenizing_quote_from_Le_Corbeau(logger):
    '''
    Given a string quote_from_Le_Corbeau of text with words from Le Corbeau,
    when I pass a cleaned version of quote_from_Le_Corbeau to function tokenize,
    I should get a list of the words in the version as return
    Each word should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words from cleaned version of Le Corbeau

    Exceptions raised:
        AssertionError if actual and expected lists are not equal

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing cleaned version of quote from Le Corbeau")

    quote_from_Le_Corbeau = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

    cleaned_text = clean_text(quote_from_Le_Corbeau)

    actual_list_of_words = tokenize(cleaned_text)

    expected_list_of_words = [
        "mais",
        "le",
        "corbeau",
        "perché",
        "solitairement",
        "sur",
        "ce",
        "buste",
        "placide",
        "parla",
        "ce",
        "seul",
        "mot",
        "comme",
        "si",
        "son",
        "âme",
        "en",
        "ce",
        "seul",
        "mot",
        "il",
        "la",
        "répandait",
        "je",
        "ne",
        "proférai",
        "donc",
        "rien",
        "de",
        "plus",
        "il",
        "nagita",
        "donc",
        "pas",
        "de",
        "plumejusquà",
        "ce",
        "que",
        "je",
        "fis",
        "à",
        "peine",
        "davantage",
        "que",
        "marmotter",
        "dautres",
        "amis",
        "déjà",
        "ont",
        "pris",
        "leur",
        "voldemain",
        "il",
        "me",
        "laissera",
        "comme",
        "mes",
        "espérances",
        "déjà",
        "ont",
        "pris",
        "leur",
        "vol",
        "alors",
        "loiseau",
        "dit",
        "jamais",
        "plus"
    ]

    assert \
        actual_list_of_words == expected_list_of_words, \
        "Actual and expected list of words in cleaned version of Le Corbeau are not equal."


def test_tokenizing_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words from cleaned version of quote from The Raven

    Exceptions raised:
        AssertionError if actual list of words does not equal expected list of words

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing cleaned version of a quote from The Raven")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    expected_list_of_words = [
        "but",
        "the",
        "raven",
        "sitting",
        "lonely",
        "on",
        "the",
        "placid",
        "bust",
        "spoke",
        "only",
        "that",
        "one",
        "word",
        "as",
        "if",
        "his",
        "soul",
        "in",
        "that",
        "one",
        "word",
        "he",
        "did",
        "outpour"
    ]

    assert \
        actual_list_of_words == expected_list_of_words, \
        f"Actual list of words in cleaned version of a quote from The Raven is not equal to expected list of words in a cleaned version of a quote from The Raven."


def test_tokenizing_The_Raven(logger):
    '''
    Given a string of text with words from The Raven,
    when I pass a cleaned version of the text to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words from a cleaned version of The Raven

    Exceptions raised:
        AssertionError if actual list of words from a cleaned version of The Raven does not equal expected list of words from a cleaned version of The Raven

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing a cleaned version of The Raven")

    text = None
    with open("The_Raven.txt", 'r') as file:
        text = file.read()

    text_to_tokenize = clean_text(text)

    actual_list_of_words = tokenize(text_to_tokenize)

    with open("List_Of_Words_In_Cleaned_Version_Of_The_Raven.pickle", "rb") as file:
        expected_list_of_words = pickle.load(file)
    
    assert \
        actual_list_of_words == expected_list_of_words, \
        f"Actual list of words from a cleaned version of The Raven is not equal to expected list of words from a cleaned version of The Raven."


def test_tokenizing_The_Raven_using_command_and_function(logger):
    '''
    Given a file with text or a string text with words from The Raven,
    when I pass a cleaned version of text to a command or tokenize,
    I should get a list of words in the version as return
    The string should consist of lowercase characters not in augmentation of string.punctuation.

    Keyword arguments:
        logger: Logger -- a logger

    Return values:
        none

    Side effects:
        Compares lists of words

    Exceptions raised:
        AssertionError if lists of words are not equal

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing text")

    command = "cat The_Raven.txt | gawk '{print tolower($0)}' | tr -d \"!\\\"#$%&'()*+,-./:;<=>?@[\\\\]^_\\`{|}~\" | sed 's/«//g' | sed 's/»//g' | tr '\n\r' ' ' | sed 's/  */ /g' | sed 's/[[:space:]]*$//' | jq -R 'split(\" \")'"

    serialized_list_of_words_from_command = subprocess.run(command, shell = True, capture_output = True, text = True).stdout
    list_of_words_from_command = json.loads(serialized_list_of_words_from_command)

    text = None
    with open("The_Raven_Cleaned.txt", 'r') as file:
        text = file.read()
    list_of_words_from_function = tokenize(text)

    assert \
        list_of_words_from_command == list_of_words_from_function, \
        f"Actual cleaned texts are not equal."


@pytest.mark.xfail
def test_that_a_word_in_cleaned_version_of_quote_from_The_Raven_has_a_hyphen(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in augmentation of string.punctuation.
    The words should not have hyphens; a test that a word has a hyphen should fail.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether a word in a cleaned version of a quote from The Raven has a hyphen

    Exceptions raised:
        AssertionError if no word has a hyphen

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing text")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    there_are_no_hyphens = True
    for word in actual_list_of_words:
        if '-' in word:
            there_are_no_hyphens = False

    assert \
        not there_are_no_hyphens, \
        f"There are no hyphens in the words in a cleaned version of a quote from The Raven."


def test_that_there_are_no_hyphens_in_words_in_cleaned_version_of_quote_from_The_Raven(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words from The Raven,
    when I pass a cleaned version of quote_from_The_Raven to tokenize,
    I should get a list of the words in the version as return.
    The words should consist of lowercase characters not in augmentation of string.punctuation.
    The words should not have hyphens.

    Keyword arguments:
        logger: Logger -- a logger
        quote_from_The_Raven: str -- a quote from The Raven

    Return values:
        none

    Side effects:
        Determines whether there are no hyphens in words in a cleaned version of quote_from_The_Raven

    Exceptions raised:
        AssertionError if there is a hyphen in a word

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that there are no hyphens in words in cleaned version of quote from The Raven")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    there_are_no_hyphens = True
    for word in actual_list_of_words:
        if '-' in word:
            there_are_no_hyphens = False

    assert \
        there_are_no_hyphens, \
        f"There is a hyphen in a word in a cleaned version of a quote from The Raven."
