cat "$1" | gawk '{print tolower($0)}' | tr -d "\!\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~" > "${$1%.*}_Cleaned_By_Command.txt"
