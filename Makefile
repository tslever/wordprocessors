output_contents_of_Makefile:
	@cat Makefile

get_The_Raven:
	@wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
	mv pg17192.txt The_Raven.txt
