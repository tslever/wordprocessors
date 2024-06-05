from collections import Counter
import string


def clean_text(text: str) -> str:
    assert type(text) == str

    translation_table = str.maketrans('', '', string.punctuation)
    cleaned_text = text.lower().translate(translation_table)

    assert type(cleaned_text) == str
    assert not cleaned_text is None

    return cleaned_text


def tokenize(text: str) -> list[str]:
    assert type(text) == str

    list_of_words = text.split()

    assert type(list_of_words) == list
    assert not list_of_words is None

    return list_of_words


def count_words(text: str) -> dict[str, int]:
    assert type(text) == str

    list_of_words = tokenize(text)
    the_counter = Counter(list_of_words)
    dictionary_of_words_and_counts = dict(the_counter)

    assert type(dictionary_of_words_and_counts) == dict
    assert not dictionary_of_words_and_counts is None
    
    return dictionary_of_words_and_counts