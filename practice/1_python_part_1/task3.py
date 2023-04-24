"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    print(f"{lines = }")
    print(f"{word_number = }")
    ret_str = str()
    uniq_words = list()
    for ln in lines:
        words = "".join(ln).split()
        uniq_words.clear()
        for v in words:
            if v not in uniq_words:
                uniq_words.append(v)
        if len(uniq_words) - 1 >= word_number:
            if len(ret_str) > 0:
                ret_str = ret_str + " " + uniq_words[word_number]
            else:
                ret_str = uniq_words[word_number]

    return ret_str
