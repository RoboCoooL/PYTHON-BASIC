"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    num_list = list()
    if n > 0: print(f"Please enter {n} numbers:")
    for i in range(n):
        try:
            num_list.append(int(input()))
        except ValueError:
            continue
    if len(num_list) > 0:
        ret_str = f"Avg: {(sum(num_list) / len(num_list)) :.2f}"
    else:
        ret_str = "No numbers entered"
    return ret_str
