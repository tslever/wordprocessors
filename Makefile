output_contents_of_Makefile:
	@cat Makefile

get_text:
	@wget https://www.gutenberg.org/cache/epub/$(text_ID)/pg$(text_ID).txt

get_texts:
	$(MAKE) get_text text_ID=17192
	$(MAKE) get_title text_ID=17192
	$(MAKE) rename_text text_ID=17192
	@echo "Got $$(tail -n 1 Temporary_File.txt)"
	@rm Temporary_File.txt

get_title:
	@sed -n '/^Title: /{s/^Title: //;s/\r.*//;p;q;}' pg$(text_ID).txt > Temporary_File.txt

rename_text:
	@echo "$$(head -n 1 Temporary_File.txt | tr ' ' '_').txt" >> Temporary_File.txt
	@mv pg$(text_ID).txt $$(tail -n 1 Temporary_File.txt)
