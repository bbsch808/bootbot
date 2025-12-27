#reads contents of book
def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
        return file_contents

#counts each individual letter
def get_letters_numbered(path):
    letters = {}
    for c in path:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters