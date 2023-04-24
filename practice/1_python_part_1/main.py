from task1 import delete_from_list
from task2 import set_to_dict
from task3 import build_from_unique_words
from task4 import calculate_power_with_difference
from task5 import remove_duplicated_words
from task6 import get_min_max


def run_task1():
    ret_list = delete_from_list([1, 2, 3, 4, 3], 3)
    print(f"{ret_list = }\n")
    ret_list = delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    print(f"{ret_list = }\n")
    ret_list = delete_from_list([1, 2, 3], 'b')
    print(f"{ret_list = }\n")
    ret_list = delete_from_list([], 'b')
    print(f"{ret_list = }\n")


def run_task2():
    ret_dict = set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
    print(f"{ret_dict = }\n")
    ret_dict = set_to_dict({}, a=0)
    print(f"{ret_dict = }\n")
    ret_dict = set_to_dict({'a': 5})
    print(f"{ret_dict = }\n")


def run_task3():
    ret_str = build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    print(f"{ret_str = }\n")
    ret_str = build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    print(f"{ret_str = }\n")
    ret_str = build_from_unique_words('1 2', '1 2 3', word_number=10)
    print(f"{ret_str = }\n")
    ret_str = build_from_unique_words(word_number=10)
    print(f"{ret_str = }\n")


def run_task4():
    ret_list = calculate_power_with_difference([1, 2, 3])
    print(f"{ret_list = }\n")
    ret_list = calculate_power_with_difference([-1, 0, 99])
    print(f"{ret_list = }\n")
    ret_list = calculate_power_with_difference([14, 59, -2 ** 63, 2 ** 63])
    print(f"{ret_list = }\n")


def run_task5():
    ret_str = remove_duplicated_words('cat cat dog 1 dog 2')
    print(f"{ret_str = }\n")
    ret_str = remove_duplicated_words('cat cat cat')
    print(f"{ret_str = }\n")
    ret_str = remove_duplicated_words('1 2 3')
    print(f"{ret_str = }\n")


def run_task6():
    ret_tup = get_min_max(r"C:\Users\Coool\PycharmProjects\PYTHON-BASIC\practice\1_python_part_1\files\file1.txt")
    print(f"{ret_tup = }\n")


def main():
    # run_task1()
    # run_task2()
    # run_task3()
    # run_task4()
    # run_task5()
    run_task6()


if __name__ == '__main__':
    main()
