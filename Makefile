# public
output_contents_of_Makefile:
	@cat Makefile

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
