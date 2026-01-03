import sys

from stats import get_book_text

from stats import get_letters_numbered

from stats import sort_dictionary



#returns the word length of the book
def word_counter(file_contents):

    words_list = file_contents.split()
    words_list_length = len(words_list)
    return words_list_length


#prints report
def main():
    try:
        sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = word_counter(text)
    dictionary = get_letters_numbered(f"{text}")
    final_dictionary = sort_dictionary(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in final_dictionary:
        print(f"{letter["char"]}: {letter["num"]}")
    
    print("============= END ===============")
    
main()
