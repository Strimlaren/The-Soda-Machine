from os import system
from random import choice, uniform
from moneymachine import *
from time import sleep
from readchar import readkey, key


def create_product_list(dict):
    """Creates and returns a menu list based off a product dictionary."""
    menu_list = []

    for item in dict:
        menu_list.append(f" {item}")
    menu_list.append(" Back")

    return menu_list


def create_product_dict(dict, function):
    """Creates and returns a menu dictionary based off a product dictionary."""
    menu_dict = {}
    menu_item_nr = 0

    for item in dict:
        menu_dict[menu_item_nr] = item
        menu_item_nr += 1
    menu_dict[menu_item_nr] = function

    return menu_dict


def update_choice(choice, old_choice, menu_list):
    """Updates the selection of any given menu provided as a list."""

    menu_list[old_choice] = menu_list[old_choice][:0] + " " + menu_list[old_choice][1:]
    user_key = readkey()

    if user_key == key.UP:
        if choice == 0:
            choice = len(menu_list) - 1
        else:
            choice -= 1

    if user_key == key.DOWN:
        if choice == len(menu_list) - 1:
            choice = 0
        else:
            choice += 1

    if user_key == key.ENTER:
        return -1

    return choice


def opening_print(funds, delay):
    """Clears screen and creates the fundamental overlay on top."""
    system("cls")
    print(soda_on)
    print(f"\n Welcome to the Soda-Machine. Your funds: ${get_money()}")
    print(f"\n Max Funds: ${funds} | Menu Delay: {delay}s | Products: {len(drinks)}")
    print(" ______________________________________________\n")


def print_menu(choice, menu_list, message, funds, delay):
    """Prints a list as a menu and facilitates the selection process."""

    opening_print(funds, delay)
    if message: print(message)

    for item in range(len(menu_list)):
        if item == choice:
            menu_list[item] = menu_list[item][:0] + ">" + menu_list[item][1:]
        print(menu_list[item])

    old_choice = choice
    choice = update_choice(choice, old_choice, menu_list)

    return choice


def crate_printer(crate):
    """Takes a list of products and returns crate graphic ready to print."""
    crate_out = ""
    modified_crate = []

    for item in crate:
        chars = len(item)
        missing = 11 - chars
        if chars < 11:
            for x in range(missing):
                item += " "
        modified_crate.append(item)

    while len(modified_crate) != 20:
        modified_crate.append("           ")

    crate_out += f" ---------------------------------------------------------------------- \n|["
    for x in range(1, 20):
        if x % 5 == 0 and x > 0:
            crate_out += f" {modified_crate.pop()}]|\n"
            crate_out += "|----------------------------------------------------------------------|\n|["
        else:
            crate_out += f" {modified_crate.pop()}]["

    crate_out += f" {modified_crate.pop()}]|\n ---------------------------------------------------------------------- \n"

    return crate_out


def loading():
    """Simulates a loading bar."""
    progress = "                                                                      "
    while True:
        print(soda_off)
        print("\n                               LOADING...                              ")
        print(" +----------------------------------------------------------------------+")
        print(f" |{progress}|")
        print(" +----------------------------------------------------------------------+")

        if progress.count("#") != 70:
            progress = "#" + progress[:-1]
            sleep(uniform(0.05, 0.2))
            system("cls")
        else:
            break


soda_on = """                                                            
  _____       _               _____         _   _            _____     
 |   __|___ _| |___    ___   |     |___ ___| |_|_|___ ___   |     |___ 
 |__   | . | . | .'|  |___|  | | | | .'|  _|   | |   | -_|  |  |  |   |
 |_____|___|___|__,|         |_|_|_|__,|___|_|_|_|_|_|___|  |_____|_|_|
"""

soda_off = """
  _____       _               _____         _   _            _____ ___ ___ 
 |   __|___ _| |___    ___   |     |___ ___| |_|_|___ ___   |     |  _|  _|
 |__   | . | . | .'|  |___|  | | | | .'|  _|   | |   | -_|  |  |  |  _|  _|
 |_____|___|___|__,|         |_|_|_|__,|___|_|_|_|_|_|___|  |_____|_| |_| 
"""
