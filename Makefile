output_contents_of_Makefile:
	@cat Makefile

get_text:
	@wget https://www.gutenberg.org/cache/epub/$(text_ID)/pg$(text_ID).txt

get_texts:
	@for text_ID in $(shell cat Text_IDs.txt); do \
		$(MAKE) get_text text_ID=$$text_ID; \
		$(MAKE) get_title text_ID=$$text_ID; \
		$(MAKE) rename_text text_ID=$$text_ID; \
		echo "Got $$(tail -n 1 Temporary_File.txt)"; \
		rm Temporary_File.txt; \
	done

get_title:
	@sed -n '/^Title: /{s/^Title: //;s/\r.*//;p;q;}' pg$(text_ID).txt > Temporary_File.txt

rename_text:
	@echo "$$(head -n 1 Temporary_File.txt | tr ' ' '_').txt" >> Temporary_File.txt
	@mv pg$(text_ID).txt $$(tail -n 1 Temporary_File.txt)
