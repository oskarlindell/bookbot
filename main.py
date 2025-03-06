def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return(file_contents)

from stats import count_words, count_characters, sort_character

def main():
    import sys
    words = None
    args = sys.argv

    if len(args) != 1:
        bookpath = args[1]
        text = get_book_text(bookpath)
        num_words = count_words(text)
        chars = count_characters(text)
        sorted_chars = sort_character(chars)

        print("============ BOOKBOT ============")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sorted_chars:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
