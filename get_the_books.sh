for text_ID in $(cat Text_IDs.csv); do
    make get_text text_ID=$text_ID;
    make get_title text_ID=$text_ID;
    make rename_text text_ID=$text_ID;
    echo "Got $(tail -n 1 Temporary_File.txt)";
    rm Temporary_File.txt;
done
