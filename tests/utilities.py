import os
import pathlib
import pickle


def anthology(list_of_paths_to_files_with_english_texts) -> str:
    list_of_texts = []
    for path in list_of_paths_to_files_with_english_texts:
        with open(path, 'r', encoding = "utf-8") as file:
            text = file.read()
            list_of_texts.append(text)
    anthology_of_english_texts = '\n'.join(list_of_texts)
    return anthology_of_english_texts

dictionary_of_ids_and_base_names_of_english_texts = {
    17192: "The_Raven.txt",
    932: "The_Fall_of_the_House_of_Usher.txt",
    1063: "The_Cask_of_Amontillado.txt",
    10031: "The_Complete_Poetical_Works_of_Edgar_Allan_Poe.txt"
}

def dictionary_of_words_and_counts_from_pickle(base_name: str, temporary_directory_of_files_with_texts) -> dict[str, int]:
    expected_dictionary_of_words_and_counts = None
    with open(temporary_directory_of_files_with_texts / base_name, "rb") as file:
        expected_dictionary_of_words_and_counts = pickle.load(file)
    return expected_dictionary_of_words_and_counts

def list_of_words_from_pickle(base_name, temporary_directory_of_files_with_texts):
    expected_list_of_words = None
    with open(temporary_directory_of_files_with_texts / base_name, "rb") as file:
        expected_list_of_words = pickle.load(file)
    return expected_list_of_words

quote_from_le_corbeau = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

def text_from_file(base_name: str, temporary_directory_of_files_with_texts) -> str:
    text = None
    with open(
        temporary_directory_of_files_with_texts / base_name,
        'r',
        encoding = "utf-8"
    ) as file:
        text = file.read()
    return text
