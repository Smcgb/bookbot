import sys   
from stats import *

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        book_text = f.read()

    return book_text

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book = sys.argv[1]
    wc = word_count(get_book_text(book))
    letter_dict = (letter_char_count(get_book_text(book)))

    sorted_dict = sorted_list_of_char_count(letter_dict)

    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {wc} total words")
    print(f"--------- Character Count -------")
    for letter_dict in sorted_dict:
        print(f"{letter_dict['name']}: {letter_dict['num']}")
if __name__ == "__main__":
    main()
