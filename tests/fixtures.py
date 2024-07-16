'''
Module logger, which has pytest fixture logger 
'''

import copy
from typing import List
import logging
import os
import pathlib
import pickle
import pytest
import requests
from pkg_tsl2b import clean_text, count_words, tokenize


dictionary_of_IDs_and_base_names_of_English_texts = {
    17192: "The_Raven.txt",
    932: "The_Fall_of_the_House_of_Usher.txt",
    1063: "The_Cask_of_Amontillado.txt",
    10031: "The_Complete_Poetical_Works_of_Edgar_Allan_Poe.txt"
}


dictionary_of_IDs_and_base_names_of_texts = copy.deepcopy(
    dictionary_of_IDs_and_base_names_of_English_texts
)
dictionary_of_IDs_and_base_names_of_texts[14082] = "Le_Corbeau.txt"


@pytest.fixture(scope = "session")
def temporary_directory(tmp_path_factory) -> pathlib.PosixPath:
    '''
    Provides a pathlib.PosixPath object for a temporary directory

    Keyword arguments:
        tmp_path_factory

    Return values:
        temporary_directory: pathlib.PosixPath --
        a pathlib.PosixPath object for a temporary directory

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions of when this is called:
        This function is called automatically by pytest.
    '''

    temp_dir = tmp_path_factory.mktemp("temporary_directory")
    return temp_dir


@pytest.fixture(params = [dictionary_of_IDs_and_base_names_of_texts], scope = "session")
def temporary_directory_of_files_with_texts(
    request: pytest.FixtureRequest,
    temporary_directory
) -> pathlib.PosixPath:
    '''
    Provides a pathlib.PosixPath object for a temporary directory of files with texts

    Keyword arguments:
        request: pytest.FixtureRequest -- a request from which to get a specified parameter
        temporary_directory

    Return values:
        temporary_directory

    Side effects:
        Creates files with texts

    Exceptions raised:
        none

    Restrictions on when this is called:
        This function is called automatically by pytest
    '''

    dictionary = request.param
    list_of_english_texts = []
    for text_id, base_name in dictionary.items():
        text = requests.get(
            f"https://www.gutenberg.org/cache/epub/{text_id}/pg{text_id}.txt", timeout = 10
        ).text
        if base_name != "Le_Corbeau.txt":
            list_of_english_texts.append(text)
        (temporary_directory / base_name).write_text(text)
        cleaned_text = clean_text(text)
        file_name, extension = os.path.splitext(base_name)
        (temporary_directory / f"{file_name}_Cleaned{extension}").write_text(cleaned_text)
        list_of_words = tokenize(cleaned_text)
        with open(
            temporary_directory / f"List_Of_Words_In_Cleaned_Version_Of_{file_name}.pickle",
            "wb"
        ) as file:
            pickle.dump(list_of_words, file)
        dictionary = count_words(cleaned_text)
        with open(
            temporary_directory / \
            f"Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_{file_name}.pickle",
        "wb"
        ) as file:
            pickle.dump(dictionary, file)
    anthology_of_english_texts = '\n'.join(list_of_english_texts)
    (temporary_directory / "Anthology_Of_English_Texts.txt").write_text(anthology_of_english_texts)
    anthology_of_english_texts_cleaned = clean_text(anthology_of_english_texts)
    (temporary_directory / "Anthology_Of_English_Texts_Cleaned.txt").write_text(
        anthology_of_english_texts_cleaned
    )
    list_of_words = tokenize(anthology_of_english_texts_cleaned)
    with open(
        temporary_directory /
        "List_Of_Words_In_Cleaned_Version_Of_Anthology_Of_English_Texts.pickle",
        "wb"
    ) as file:
        pickle.dump(list_of_words, file)
    dictionary = count_words(anthology_of_english_texts_cleaned)
    with open(
        temporary_directory /
        "Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_Anthology_Of_English_Texts.pickle",
        "wb"
    ) as file:
        pickle.dump(dictionary, file)
    return temporary_directory


@pytest.fixture(params = [dictionary_of_IDs_and_base_names_of_English_texts], scope = "session")
def list_of_paths_to_files_with_english_texts(
    request: pytest.FixtureRequest,
    temporary_directory
) -> List[str]:
    '''
    Provides a list of paths to existing files with English texts

    Keyword arguments:
        request: FixtureRequest --
        a fixture request with a parameter specified in the above decorator
        temporary_directory

    Return values:
        list_of_paths_to_files_with_english_texts: List[str] --
        a list of paths to existing files with English texts

    Side effects:
        Creates files if they don't already exist

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        pytest only should call this method to provide a list of file names of English texts.
    '''

    dictionary = request.param
    list_of_paths = []
    for base_name in dictionary.values():
        temporary_file = temporary_directory / base_name
        list_of_paths.append(temporary_file)
    return list_of_paths


@pytest.fixture(scope = "session")
def logger():
    '''
    Sets up a logger

    Keyword arguments:
        none

    Return values:
        logger

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        pytest only should call this method to set up logger.
    '''

    lumberjack = logging.getLogger(__name__)
    return lumberjack


@pytest.fixture(
    params = [
        "But the Raven, " +
        "sitting lonely on the placid bust, " +
        "spoke only That one word, " +
        "as if his soul in that one word he did outpour.",
        "But the Raven-- " +
        "sitting lonely on the placid bust --" +
        "spoke only That one word, " +
        "as if his soul in that one word he did outpour."
    ]
)
def quote_from_the_raven(request: pytest.FixtureRequest, scope = "session") -> str:
    '''
    Provides a quote from The Raven

    Keyword arguments:
        request: FixtureRequest --
        a fixture request with a parameter specified in the above decorator

    Return values:
        quote_from_the_raven: str -- a quote from The Raven

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        pytest only should call this method to provide a quote from The Raven.
    '''

    quote = request.param
    return quote
