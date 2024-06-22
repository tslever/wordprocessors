# public
output_contents_of_Makefile:
	@cat Makefile

# public
clean_texts:
	@python wordprocessors/word_processors.py clean_text The_Raven.txt
	@python wordprocessors/word_processors.py clean_text The_Fall_of_the_House_of_Usher.txt
	@python wordprocessors/word_processors.py clean_text The_Cask_of_Amontillado.txt
	@python wordprocessors/word_processors.py clean_text The_Complete_Poetical_Works_of_Edgar_Allan_Poe.txt

# public
clean_The_Raven_by_command:
	@bash clean_text.sh The_Raven.txt > "The_Raven_Cleaned_By_Command.txt"

# public
create_cleaned_anthology_of_English_texts:
	@cat The_Raven.txt > Anthology_Of_English_Texts.txt
	@printf "\n" >> Anthology_Of_English_Texts.txt
	@cat The_Fall_of_the_House_of_Usher.txt >> Anthology_Of_English_Texts.txt
	@printf "\n" >> Anthology_Of_English_Texts.txt
	@cat The_Cask_of_Amontillado.txt >> Anthology_Of_English_Texts.txt
	@printf "\n" >> Anthology_Of_English_Texts.txt
	@cat The_Complete_Poetical_Works_of_Edgar_Allan_Poe.txt >> Anthology_Of_English_Texts.txt
	#@python wordprocessors/word_processors.py clean_text Anthology_Of_English_Texts.txt
	@bash clean_text.sh Anthology_Of_English_Texts.txt > Anthology_Of_English_Texts_Cleaned.txt"

# public
env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip; pip install --editable .

# private
get_text:
	@wget https://www.gutenberg.org/cache/epub/$(text_ID)/pg$(text_ID).txt

# public
get_texts:
	#@for text_ID in $(shell cat Text_IDs.csv); do \
	#	$(MAKE) get_text text_ID=$$text_ID; \
	#	$(MAKE) get_title text_ID=$$text_ID; \
	#	$(MAKE) rename_text text_ID=$$text_ID; \
	#	echo "Got $$(tail -n 1 Temporary_File.txt)"; \
	#	rm Temporary_File.txt; \
	#done
	@bash get_the_books.sh

# private
get_title:
	@sed -n '/^Title: /{s/^Title: //;s/\r.*//;p;q;}' pg$(text_ID).txt > Temporary_File.txt

# public
set_up_virtual_environment_env_upgrade_PIP_and_use_PIP_to_install_Python_packages_specified_in_text_file_requirements:
	@sudo apt install python3.10-venv
	@python3 -m venv env
	@. env/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	deactivate

# public
raven_counts:
	@grep raven The_Raven.txt | wc --lines
	@grep Raven The_Raven.txt | wc --lines
	@grep --ignore-case raven The_Raven.txt | wc --lines

# public
raven_line_count:
	@wc --lines The_Raven.txt

# public
raven_word_count:
	@wc --words The_Raven.txt

# private
rename_text:
	@echo "$$(head -n 1 Temporary_File.txt | tr ' ' '_').txt" >> Temporary_File.txt
	@mv pg$(text_ID).txt $$(tail -n 1 Temporary_File.txt)

# public
total_lines:
	@find . -type f -name "*.txt" -exec wc --lines {} + | tail -n 1

# public
total_words:
	@find . -type f -name "*.txt" -exec wc --words {} + | tail -n 1
