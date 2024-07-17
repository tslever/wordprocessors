import os
import pathlib
import pickle

def dictionary_of_words_and_counts_from_pickle(base_name: str, temporary_directory_of_files_with_texts) -> dict[str, int]:
    expected_dictionary_of_words_and_counts = None
    with open(temporary_directory_of_files_with_texts / base_name, "rb") as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)
    return expected_dictionary_of_words_and_counts

def text_from_file(base_name: str, temporary_directory_of_files_with_texts) -> str:
    text = None
    with open(
        temporary_directory_of_files_with_texts / base_name,
        'r',
        encoding = "utf-8"
    ) as file:
        text = file.read()
    return text
