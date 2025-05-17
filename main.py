import sys

from stats import (
    get_num_words,
    get_chars_distribution,
    get_stats_list
)

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():

    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    input_file = args[-1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input_file}...")
    contents = get_book_text(input_file)
    
    print("----------- Word Count ----------")
    num_words = get_num_words(contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    chars_stats = get_chars_distribution(contents)
    summary = get_stats_list(chars_stats)
    for elem in summary:
        char = elem["char"]
        if char.isalpha():
            print(f"{char}: {elem['num']}")

main()