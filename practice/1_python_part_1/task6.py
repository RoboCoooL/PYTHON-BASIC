"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    with open(filename) as opened_file:
        t_max = None
        t_min = None
        for line in opened_file:
            try:
                num = int(line.strip())
            except Exception:
                #some logging
                continue
            if t_max is None and t_min is None:
                t_max = t_min = num
            else:
                if num > t_max:
                    t_max = num
                if num < t_min:
                    t_min = num
    return t_min, t_max
