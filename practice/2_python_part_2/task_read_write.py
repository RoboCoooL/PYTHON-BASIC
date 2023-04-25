"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os


def read_files():
    lis = list()
    files = [os.path.join('files', file) for file in os.listdir('files')]
    for file in files:
        with open(file, 'r', encoding='UTF=8') as f:
            for line in f:
                lis.append(line.strip())
    if len(lis) > 0:
        with open("files/result.txt", "w+", encoding='UTF-8') as f:
            f.write(', '.join(lis))
