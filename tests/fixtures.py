'''
Module logger, which has pytest fixture logger 
'''


from typing import List
import logging
import pytest


list_with_list_of_paths_to_files_with_English_texts = [
    [
        "The_Raven.txt",
        "The_Fall_of_the_House_of_Usher.txt",
        "The_Cask_of_Amontillado.txt",
        "The_Complete_Poetical_Works_of_Edgar_Allan_Poe.txt"
    ]
]    


@pytest.fixture(params = list_with_list_of_paths_to_files_with_English_texts)
def list_of_paths_to_files_with_English_texts(request: pytest.FixtureRequest) -> List[str]:
    '''
    Provides a list of paths to files with English texts

    Keyword arguments:
        request: FixtureRequest -- a fixture request with a parameter specified in the above decorator

    Return values:
        list_of_paths_to_files_with_English_texts: List[str] -- a list of paths to files with English texts

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        pytest only should call this method to provide a list of file names of English texts.
    '''

    list_of_paths_to_files_with_English_texts = request.param
    return list_of_paths_to_files_with_English_texts


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
