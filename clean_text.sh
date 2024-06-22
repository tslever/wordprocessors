file_name="$1"
cat "$file_name" | gawk '{print tolower($0)}' | tr -d "\!\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~" > "${file_name%.*}_Cleaned_By_Command.txt"
