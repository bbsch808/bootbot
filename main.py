from stats import get_book_text

from stats import get_letters_numbered

from stats import sort_dictionary



#returns the word length of the book
def word_counter(file_contents):

    words_list = file_contents.split()
    words_list_length = len(words_list)
    return words_list_length



def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(text)
    dictionary = get_letters_numbered(f"{text}")
    final_dictionary = sort_dictionary(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in final_dictionary:
        print(f"{letter["char"]}: {letter["num"]}")
    
    print("============= END ===============")
    
main()
