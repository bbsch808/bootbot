def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_letters_numbered(path):
    letters = {}
    for letter in path:
        letter_counter = letters.get(letter, 0)
        letters[letter] = letter_counter + 1
    return letters