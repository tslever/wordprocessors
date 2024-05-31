output_contents_of_Makefile:
	@cat Makefile

get_texts:
	@wget https://www.gutenberg.org/cache/epub/$(text_ID_1)/pg$(text_ID_1).txt
	@wget https://www.gutenberg.org/cache/epub/$(text_ID_2)/pg$(text_ID_2).txt
