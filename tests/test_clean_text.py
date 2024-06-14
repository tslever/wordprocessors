'''
Module test_clean_text, which has functions to test cleaning text 
'''


from logger import logger
from tsl2b_DS5111su24_lab_01.word_processors import clean_text


def test_clean_text(logger):
    '''
    Tests cleaning text

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

    text_to_clean = """And he looked over at the alarm clock,
    ticking on the chest of drawers. "God in Heaven!" he thought.
    It was half past six and the hands were quietly moving forwards,
    it was even later than half past, more like quarter to seven.
    Had the alarm clock not rung? He could see from the bed that it
    had been set for four o'clock as it should have been; it certainly must have rung.
    Yes, but was it possible to quietly sleep through that furniture-rattling noise?
    True, he had not slept peacefully, but probably all the more deeply because of that"""

    actual_cleaned_text = clean_text(text_to_clean)

    expected_cleaned_text = """and he looked over at the alarm clock
    ticking on the chest of drawers god in heaven he thought
    it was half past six and the hands were quietly moving forwards
    it was even later than half past more like quarter to seven
    had the alarm clock not rung he could see from the bed that it
    had been set for four oclock as it should have been it certainly must have rung
    yes but was it possible to quietly sleep through that furniturerattling noise
    true he had not slept peacefully but probably all the more deeply because of that"""

    assert \
        actual_cleaned_text == expected_cleaned_text, \
        "Actual cleaned text is not equal to expected cleaned text."

