import sys

from stats import get_num_words, get_char_freq, to_sorted_list_of_dicts


def get_book_text(file_path: str) -> str:
    with open(file_path, "rt") as f:
        file_content = f.read()
    return file_content


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])

    num_words = get_num_words(text)
    char_freq = get_char_freq(text)
    sorted_list = to_sorted_list_of_dicts(char_freq)
    print(f"Found {num_words} total words")
    for el in sorted_list:
        if el["char"].isalpha():
            print(el["char"] + ": " + str(el["num"]))

main()
