from stats import count_words
from stats import count_total_each_appears
from stats import bubble_sort
from stats import sort_on
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as read_file:
        file_contents = read_file.read()
    return file_contents

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    num_words = count_words(file_contents)
    dict1 = count_total_each_appears(file_contents)
    lista = bubble_sort(dict1)
    lista.sort(reverse=True, key=sort_on)
    print(f"""
    ============ BOOKBOT ============   
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------
    """)

    for i in lista:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i[f"num"]}')
    
    print("============= END ===============")



main()
