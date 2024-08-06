'''
Module word_processors, which has functions to clean, tokenize, and count words in text
'''


import argparse
from collections import Counter
from typing import Dict, List
import logging
import os
import pickle
import string


logger = logging.getLogger(__name__)


def clean_text(text_to_clean: str) -> str:
    '''
    Cleans text by lowercasing and removing characters in an augmentation of string.punctuation
        
    Keyword arguments:
        text_to_clean: str -- text to clean

    Return values:
        cleaned_text: str -- cleaned text

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        none
    '''

    assert isinstance(text_to_clean, str)

    translation_table = str.maketrans('', '', string.punctuation + "\r«»")
    cleaned_text = text_to_clean.lower().translate(translation_table)

    #logger.info("Cleaned text: %s", cleaned_text)

    assert not cleaned_text is None
    assert isinstance(cleaned_text, str)

    return cleaned_text


def tokenize(text_to_tokenize: str) -> List[str]:
    '''
    Tokenizes text of words separated by spaces into a list of those words

    Keyword arguments:
        text_to_tokenize: str -- text to tokenize

    Return values:
        list_of_words: List[str] -- list of words

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        text to tokenize should be cleanish.
    '''

    assert isinstance(text_to_tokenize, str)

    list_of_words = text_to_tokenize.split()

    #logger.info("Tokenized text: %s", list_of_words)

    assert not list_of_words is None
    assert isinstance(list_of_words, list)

    return list_of_words


def count_words(text_for_counting_words: str) -> Dict[str, int]:
    '''
    Provides a dictionary of the words in specified text and the counts of those words

    Keyword arguments:
        text_for_counting_words: str -- text

    Return values:
        dictionary_of_words_and_counts: Dict[str, int] -- dictionary of words in text and counts

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        text for counting words should be cleanish.
    '''

    assert isinstance(text_for_counting_words, str)

    list_of_words = tokenize(text_for_counting_words)
    the_counter = Counter(list_of_words)
    dictionary = dict(the_counter)

    #logger.info("Counted words: %s", dictionary)

    assert not dictionary is None
    assert isinstance(dictionary, dict)

    return dictionary


def parse_arguments():
    '''
    Parses command line arguments into a dictionary of argument names and values

    Keyword arguments:
        none

    Return values:
        dictionary_of_arguments: Dict[str, int] -- dictionary of argument names and values

    Side effects:
        none

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        first when this script is executed
    '''

    parser = argparse.ArgumentParser(
        prog = "Word Processors",
        description = "This program processes text."
    )
    parser.add_argument("name_of_function", help = "name of function")
    parser.add_argument("path_to_file_of_text", help = "path to file of text")
    args = parser.parse_args()

    function_name = args.name_of_function
    path_to_text_file = args.path_to_file_of_text
    print(f"name of function: {function_name}")
    print(f"path to file of text: {path_to_text_file}")

    dictionary = {}
    dictionary["name_of_function"] = function_name
    dictionary["path_to_file_of_text"] = path_to_text_file

    return dictionary


if __name__ == "__main__":
    dictionary_of_arguments = parse_arguments()
    name_of_function = dictionary_of_arguments["name_of_function"]
    path_to_file_of_text = dictionary_of_arguments["path_to_file_of_text"]
    TEXT = None
    with open(path_to_file_of_text, 'r', encoding = "utf-8") as file:
        TEXT = file.read()
    base_name = os.path.basename(path_to_file_of_text)
    file_name, extension = os.path.splitext(base_name)
    if name_of_function == "clean_text":
        clean_text = clean_text(TEXT)
        with open(f"{file_name}_Cleaned{extension}", 'w', encoding = "utf-8") as file:
            file.write(clean_text)
    elif name_of_function == "tokenize":
        clean_text = clean_text(TEXT)
        list_of_tokenized_words = tokenize(clean_text)
        with open(f"List_Of_Words_In_Cleaned_Version_Of_{file_name}.pickle", "wb") as file:
            pickle.dump(list_of_tokenized_words, file)
    elif name_of_function == "count_words":
        clean_text = clean_text(TEXT)
        dictionary_of_words_and_counts = count_words(clean_text)
        with open(
            f"Dictionary_Of_Words_And_Counts_For_Cleaned_Version_Of_{file_name}.pickle",
            "wb"
        ) as file:
            pickle.dump(dictionary_of_words_and_counts, file)
    else:
        raise ValueError(f"Name of function \"{name_of_function}\" is invalid.")
