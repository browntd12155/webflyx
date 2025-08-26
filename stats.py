def get_book_text( filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(filepath_to_book: str):
    the_book = get_book_text(filepath_to_book)
    the_words = the_book.split()
    num_words = len(the_words)
    print(f"Found {num_words} total words")

def sort_on_num(items):
    return items["num"]

def get_char_count(filepath_to_book: str):
    the_book = get_book_text(filepath_to_book)
    char_count = {}
    for char in the_book:
        if( char.isalpha() == False ):
            continue
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    if( len(char_count) > 0 ):
        sorted_char_count = dict(reversed(sorted(char_count.items(), key=lambda item: item[1])))
        return sorted_char_count
    else:
        return char_count
