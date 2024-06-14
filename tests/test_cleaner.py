'''
Module test_cleaner, which has functions to test cleaning text 
'''


from tsl2b_DS5111su24_lab_01.word_processors import clean_text
from logger import logger
import pytest


@pytest.mark.parametrize(
    "quote_from_The_Raven",
    [
        ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."),
        ("But the Raven-- sitting lonely on the placid bust --spoke only That one word, as if his soul in that one word he did outpour.")
    ]
)
def test_clean_text(logger, quote_from_The_Raven):
    '''
    Given a string text_to_clean of text with words,
    when I pass text_to_clean to function clean_text,
    I should get a string as return
    representing a cleaned version of that text.
    The string should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        none

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

    actual_cleaned_text = clean_text(quote_from_The_Raven)

    expected_cleaned_text = """but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"""

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        f"Given text {text_to_clean}, actual cleaned text is not equal to expected cleaned text."

