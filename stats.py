def count_words(book_text):
    word_list = book_text.split()
    number_of_words = len(word_list)
    return number_of_words


def count_characters(book_text):
    chars = {}
    text = book_text.lower()
    for i in range(len(text)):
        current_char = text[i]
        # print(current_char)
        if not current_char in chars:
            chars[current_char] = 0
        chars[current_char] += 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_character(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char" : char, "num" : char_dict[char]})
        #print (char_dict[char])
    char_list.sort(reverse=True, key = sort_on)
    return char_list
