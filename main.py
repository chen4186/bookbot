from stats import count_words
from stats import count_characters
from stats import create_dict_list

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict_list = create_dict_list(count_characters(text))
    for dict in dict_list:
        print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")

main()
