'''
Module logger, which has pytest fixture logger 
'''


from typing import List
import logging
import pytest
import requests


dictionary_of_IDs_and_base_names_of_English_texts = {
    17192: "The_Raven.txt",
    932: "The_Fall_of_the_House_of_Usher.txt",
    1063: "The_Cask_of_Amontillado.txt",
    10031: "The_Complete_Poetical_Works_of_Edgar_Allan_Poe.txt"
}


@pytest.fixture(params = [dictionary_of_IDs_and_base_names_of_English_texts])
def list_of_paths_to_existing_files_with_English_texts(request: pytest.FixtureRequest, tmp_path) -> List[str]:
    '''
    Provides a list of paths to existing files with English texts

    Keyword arguments:
        request: FixtureRequest -- a fixture request with a parameter specified in the above decorator

    Return values:
        list_of_paths_to_existing_files_with_English_texts: List[str] -- a list of paths to existing files with English texts

    Side effects:
        Creates files if they don't already exist

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        pytest only should call this method to provide a list of file names of English texts.
    '''

    
    dictionary_of_IDs_and_base_names_of_English_texts = request.param
    list_of_paths_to_existing_files_with_English_texts = list(dictionary_of_IDs_and_base_names_of_English_texts.values())
    for ID, base_name in dictionary_of_IDs_and_base_names_of_English_texts.items():
        URL = f"https://www.gutenberg.org/cache/epub/{ID}/pg{ID}.txt"
        response = requests.get(URL)
        text = response.text
        temporary_file = tmp_path / base_name
        temporary_file.write_text(text)
    return list_of_paths_to_existing_files_with_English_texts


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

    logger = logging.getLogger(__name__)
    return logger


@pytest.fixture(
    params = [
        "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.",
        "But the Raven-- sitting lonely on the placid bust --spoke only That one word, as if his soul in that one word he did outpour."
    ]
)
def quote_from_The_Raven(request: pytest.FixtureRequest) -> str:
    '''
    Provides a quote from The Raven

    Keyword arguments:
        request: FixtureRequest -- a fixture request with a parameter specified in the above decorator

    Return values:
        quote_from_The_Raven: str -- a quote from The Raven

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        pytest only should call this method to provide a quote from The Raven.
    '''

    quote_from_The_Raven = request.param
    return quote_from_The_Raven
