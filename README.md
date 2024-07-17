# wordprocessors
Contains project for Data Engineering

To get texts from Project Gutenberg, do the following.

1. Navigate to one or more text files (e.g., https://www.gutenberg.org/cache/epub/17192/pg17192.txt).

2. Add text IDs (e.g., 17192 corresponding to The Raven) to file Text_IDs.csv.

3. Run command `make get_texts`.

To test word processors, do the following.

1. Run command `make set_up_virtual_environment_env_upgrade_PIP_and_use_PIP_to_install_Python_packages_specified_in_text_file_requirements`.

2. Run command `source env/bin/activate`.

3. Run command `pytest tests/test_cleaner.py` or `pytest tests/test_tokenizer.py` or `pytest tests/test_word_counter.py`.

Functions in `tests/test_cleaner.py` clean an anthology, individual texts, and quotes from texts. Functions in `tests/test_tokenizer.py` clean an anthology, individual texts, and quotes from texts. Functions in `tests/test_word_counter.py` clean an anthology, individual texts, and quotes from texts. Consider cleaning an anthology by running `pytest tests/test_cleaner.py::test_cleaning_all_English_texts_together`.

To allow GitHub to run tests automatically,

1. See `.github/workflows/validations.yml`.

2. See Actions at `https://github.com/tslever/wordprocessors` or the following badge.

![Status Of Tests On Branch WEEK-08/github_automation](https://github.com/tslever/wordprocessors/actions/workflows/validations.yml/badge.svg?branch=WEEK-08/github_automation)

To use pylint on all appropriate files in a repository while suppressing most pytest-related false positives, install package pylint-pytest and run from the root of the repository

`find . -path ./env -prune -o -name "*.py" -exec pylint --load_plugins pylint_pytest {} +`
