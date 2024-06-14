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
