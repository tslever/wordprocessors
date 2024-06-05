from collections import Counter
import string

def clean_text(text: str) -> str:
    translation_table = str.maketrans('', '', string.punctuation)
    cleaned_text = text.lower().translate(translation_table)
    return cleaned_text

def tokenize(text: str) -> list[str]:
    list_of_words = text.split()
    return list_of_words

def count_words(text: str) -> dict[str, int]:
    list_of_words = tokenize(text)
    the_counter = Counter(list_of_words)
    dictionary_of_words_and_counts = dict(the_counter)
    return dictionary_of_words_and_counts