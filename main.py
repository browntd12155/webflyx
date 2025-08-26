from stats import get_num_words
from stats import get_char_count
import sys

def main():
    if( len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath_to_book}...")
    print("----------- Word Count ----------")
    get_num_words(filepath_to_book)
    print("--------- Character Count -------")
    char_count = get_char_count(filepath_to_book)
    for key, value in char_count.items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()
