"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    print(f"{line = }")
    tmp_str = list()
    for word in line.split():
        if word in tmp_str:
            continue
        else:
            tmp_str.append(word)
    ret_str = " ".join(tmp_str)
    return ret_str
