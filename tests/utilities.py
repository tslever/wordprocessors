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

quote_from_le_corbeau = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
