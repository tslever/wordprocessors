import os
import pathlib

def text_from_file(base_name: str, temporary_directory_of_files_with_texts) -> str:
    text = None
    with open(
        temporary_directory_of_files_with_texts / base_name,
        'r',
        encoding = "utf-8"
    ) as file:
        text = file.read()
    return text
