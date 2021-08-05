import os
import platform


def split_list(elements, n):
    # split list by n elements
    return [elements[i: i + n] for i in range(0, len(elements), n)]


def console_input(message) -> bool:
    while True:
        value = input(message + " ")
        if value.lower() == "y":
            return True
        if value.lower() == "n":
            return False
        print("Некорректный ввод")


def console_clear():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")
