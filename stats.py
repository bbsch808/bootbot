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

#sorts dictionary
def sort_on(items):
    return items["num"]

def sort_dictionary(path):

    unsorted_dict = get_letters_numbered(path)
    sorted_dict_keys = []

    for key in unsorted_dict:
        if key.isalpha() == True:
            sorted_dict_keys.append({"char": key, "num": unsorted_dict[key]})
    sorted_dict_keys.sort(reverse=True, key=sort_on)
    return sorted_dict_keys
    


