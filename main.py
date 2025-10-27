from stats import *
import sys

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def pretty_print_report(letter_list, book_path, total_words):
    header = f'============ BOOKBOT ============\nAnalyzing book found at {book_path}...'
    word_count = f'----------- Word Count ----------\nFound {total_words} total words'
    char_count = f'--------- Character Count -------'
    print(header)
    print(word_count)
    print(char_count)
    for pair in letter_list:
        print(f'{pair["char"]}: {pair["num"]}')
def main():
    try:
        book_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    total_word_count = total_words(book_text)
    num_letters = letter_count(book_text)
    sorted_letters = letter_sort(num_letters)
    pretty_print_report(sorted_letters, book_path, total_word_count)

main()
