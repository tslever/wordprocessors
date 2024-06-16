'''
Module word_processors, which has functions to clean, tokenize, and count words in text
'''


import argparse
from collections import Counter
import logging
import os
import pickle
import string


logger = logging.getLogger(__name__)


def clean_text(text: str) -> str:
    '''
    Cleans text by lowercasing and removing characters in an augmentation of string.punctuation
        
    Keyword arguments:
        text: str -- text

    Return values:
        cleaned_text: str -- cleaned text

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        none
    '''

    assert isinstance(text, str)

    translation_table = str.maketrans('', '', string.punctuation + "«»")
    cleaned_text = text.lower().translate(translation_table)

    #logger.info("Cleaned text: %s", cleaned_text)

    assert not cleaned_text is None
    assert isinstance(cleaned_text, str)

    return cleaned_text


def tokenize(text: str) -> list[str]:
    '''
    Tokenizes text of words separated by spaces into a list of those words

    Keyword arguments:
        text: str -- text

    Return values:
        list_of_words: list[str] -- list of words

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        text should be cleanish.
    '''

    assert isinstance(text, str)

    list_of_words = text.split()

    #logger.info("Tokenized text: %s", list_of_words)

    assert not list_of_words is None
    assert isinstance(list_of_words, list)

    return list_of_words


def count_words(text: str) -> dict[str, int]:
    '''
    Provides a dictionary of the words in specified text and the counts of those words

    Keyword arguments:
        text: str -- text

    Return values:
        dictionary_of_words_and_counts: str -- dictionary of words in specified text and counts

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        text should be cleanish.
    '''

    assert isinstance(text, str)

    list_of_words = tokenize(text)
    the_counter = Counter(list_of_words)
    dictionary_of_words_and_counts = dict(the_counter)

    #logger.info("Counted words: %s", dictionary_of_words_and_counts)

    assert not dictionary_of_words_and_counts is None
    assert isinstance(dictionary_of_words_and_counts, dict)

    return dictionary_of_words_and_counts


def parse_arguments():
    dictionary_of_arguments = {}
    parser = argparse.ArgumentParser(prog = "Word Processors", description = "This program processes text.")
    parser.add_argument("name_of_function", help = "name of function")
    parser.add_argument("path_to_file_of_text", help = "path to file of text")
    args = parser.parse_args()
    name_of_function = args.name_of_function
    path_to_file_of_text = args.path_to_file_of_text
    print(f"name of function: {name_of_function}")
    print(f"path to file of text: {path_to_file_of_text}")
    dictionary_of_arguments["name_of_function"] = name_of_function
    dictionary_of_arguments["path_to_file_of_text"] = path_to_file_of_text
    return dictionary_of_arguments

if __name__ == "__main__":
    dictionary_of_arguments = parse_arguments()
    name_of_function = dictionary_of_arguments["name_of_function"]
    path_to_file_of_text = dictionary_of_arguments["path_to_file_of_text"]
    text = None
    with open(path_to_file_of_text, 'r') as file:
        text = file.read()
    base_name = os.path.basename(path_to_file_of_text)
    file_name, extension = os.path.splitext(base_name)
    if name_of_function == "clean_text":
        cleaned_text = clean_text(text)
        with open(f"{file_name}_Cleaned{extension}", 'w') as file:
            file.write(cleaned_text)
    elif name_of_function == "tokenize":
        cleaned_text = clean_text(text)
        list_of_words = tokenize(cleaned_text)
        with open(f"List_Of_Words_In_Cleaned_Version_Of_{file_name}.pickle", "wb") as file:
            pickle.dump(list_of_words, file)
    elif name_of_function == "count_words":
        cleaned_text = clean_text(text)
        dictionary_of_words_and_counts = count_words(cleaned_text)
        with open(f"Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_{file_name}.pickle", "wb") as file:
            pickle.dump(dictionary_of_words_and_counts, file)
    else:
        raise ValueError(f"Name of function \"{name_of_function}\" is invalid.")
