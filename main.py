from stats import word_count
from stats import symb_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def sort_on(dict):
    return dict["num"]


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents






def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    total_words = word_count(text)
    
    
    list_of_dicts = symb_count(text)
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for entry in list_of_dicts:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()    