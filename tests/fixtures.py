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
def quote_from_The_Raven(request):
    return request.param
