def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_counts_list = [{"character": char, "count": count} for char, count in get_chars_dict(text).items()]
    char_counts_list.sort(reverse=True,key=sort_on)
    for item in char_counts_list:
        character = item["character"]
        count = item["count"]
        print(f"The '{character}' character was found {count} times")
    

def sort_on(dict):
    return dict["count"]
    
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():  
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars







main()