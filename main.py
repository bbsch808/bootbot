from stats import get_book_text

from stats import get_letters_numbered

def word_counter(file_contents):

    words_list = file_contents.split()
    words_list_length = len(words_list)
    return words_list_length



def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(text)
    print(f"Found {num_words} total words")
    dictionary = get_letters_numbered(f"{text.lower()}")
    print(f"{dictionary}")

main()
