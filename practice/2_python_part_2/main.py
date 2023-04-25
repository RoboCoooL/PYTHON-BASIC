from task_exceptions import division
from task_input_output import read_numbers
from task_read_write import read_files
from task_read_write_2 import write_files

def run_task_exceptions():
    print(division(1, 0))
    print(division(1, 1))
    print(division(1, 2))


def run_read_numbers():
    print(read_numbers(5))


def run_task_read_write():
    read_files()


def run_task_read_write_2():
    write_files()


def main():
    # run_task_exceptions()
    # run_read_numbers()
    # run_task_read_write()
    run_task_read_write_2()


if __name__ == '__main__':
    main()
