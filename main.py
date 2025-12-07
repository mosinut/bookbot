from stats import get_num_words
from stats import get_count_characters

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()
    

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count = get_count_characters(book_text)
    print(f'Found {word_count} total words.')
    print(char_count)

if __name__ == "__main__":
    main()