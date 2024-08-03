'''
Module logger, which has pytest fixture logger 
'''


import logging
import pytest


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


@pytest.fixture(
    params = [
        [
            "The_Raven.txt",
            "The_Fall_Of_The_House_Of_Usher.txt",
            "The_Cask_Of_Amontillado.txt",
            "The_Complete_Poetical_Works_Of_Edgar_Allan_Poe.txt"
        ]
    ]
)

def list_of_paths_to_files_with_English_texts(request: pytest.FixtureRequest) -> list[str]:
    '''
    Provides a list of paths to files with English texts

    Keyword arguments:
        request: FixtureRequest -- a fixture request with a parameter specified in the above decorator

    Return values:
        list_of_paths_to_files_with_English_texts: list[str] -- a list of paths to files with English texts

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        pytest only should call this method to provide a list of file names of English texts.
    '''

    list_of_paths_to_files_with_English_texts = request.param
    return list_of_paths_to_files_with_English_texts
