'''
Module test_that_fails.py, which contains a function that when tested fails
'''

def test_that_fails():
    '''
    Fails

    Keyword arguments:
        none

    Return values:
        none

    Side effects:
        Fails

    Exceptions raised:
        AssertionError

    Restrictions on when this is called:
        pytest will run this test automatically.
    '''

    assert False, "This test fails."
