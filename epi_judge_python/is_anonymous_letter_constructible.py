from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    req_letters = Counter(letter_text)
    for char_ in magazine_text:
        req_letters[char_] -= 1
    return all(count <= 0 for key, count in req_letters.items())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
