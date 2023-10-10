from menu_handler import *
from time import sleep
from moneymachine import *

MAX_FUNDS = 10
MAX_COINS = 5
MAX_PRICE = 10
MENU_DELAY = 3

print('\x1b[?25l')


def update_menus():
    global flavor_menu_items
    global flavor_menu_dict
    flavor_menu_items = create_product_list(drinks)
    flavor_menu_dict = create_product_dict(drinks, start_menu)


def make_purchase(cost, message):
    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, yes_no, message, MAX_FUNDS, MENU_DELAY)

    if old_choice == 0:
        if enough_money(cost):
            subtract_money(cost)
            print(f"\n ACCEPTED: Thank you for your purchase. ${cost} deducted from your funds.")
            sleep(MENU_DELAY)
        else:
            print("\n DENIED: Insert more coins.")
            sleep(MENU_DELAY)
            insert_coins()
    elif old_choice == 1:
        print("\n CANCELLED: User changed his mind.")
        sleep(MENU_DELAY)

    start_menu()


def start_menu():
    update_menus()
    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, main_menu_items, "", MAX_FUNDS, MENU_DELAY)
    main_menu_dict[old_choice]()


def funds():
    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, funds_menu_items, "", MAX_FUNDS, MENU_DELAY)
    funds_menu_dict[old_choice]()


def flavors():
    update_menus()

    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, flavor_menu_items, "", MAX_FUNDS, MENU_DELAY)

    if old_choice == len(flavor_menu_items) - 1: start_menu()

    cost = price_of_item(flavor_menu_dict[old_choice])
    message = f" Purchase a {flavor_menu_dict[old_choice]} for ${cost}?\n"

    make_purchase(cost, message)


def random_flavor():
    random_item = choice(list(drinks))
    cost = price_of_item(random_item)
    message = f"\n We chose a {random_item} for you. \n Your total is: ${cost}. Purchase?\n"

    make_purchase(cost, message)


def crate():
    crate = []
    total_drinks = 0

    for item in drinks:
        while True:
            opening_print(MAX_FUNDS, MENU_DELAY)
            print(crate_printer(crate))
            print(f" Your Soda-Crate: ({total_drinks}) drinks and a total of ${total_cost(crate)}.\n")

            try:
                user_amount = int(input(f" How many {item}s do you want? (${drinks[item]} each): "))
                if total_drinks + user_amount > 20:
                    print("\n ERROR: A maximum size of 20 for each crate is allowed.")
                    sleep(MENU_DELAY)
                    continue
                else:
                    total_drinks += user_amount
            except ValueError:
                print("\n ERROR: Please enter numbers.")
                sleep(MENU_DELAY)
                continue
            else:
                break

        for n in range(user_amount):
            crate.append(item)

    cost = total_cost(crate)
    message = f"{crate_printer(crate)}\n Your total is: ${cost}. Purchase?\n"

    make_purchase(cost, message)


def random_crate():
    random_crate = []

    while True:
        opening_print(MAX_FUNDS, MENU_DELAY)

        try:
            amount = int(input("\n How many drinks do you want in your randomized soda-crate?: "))
            if amount > 20:
                print("\n ERROR: A maximum size of 20 for each crate is allowed.")
                sleep(MENU_DELAY)
                continue
        except ValueError:
            print("\n ERROR: Please enter numbers.")
            sleep(MENU_DELAY)
            continue
        else:
            break

    for n in range(amount):
        random_crate.append(choice(list(drinks)))

    cost = total_cost(random_crate)
    message = f"{crate_printer(random_crate)}\n Your total is: ${cost}. Purchase?\n"

    make_purchase(cost, message)


def insert_coins():
    money = 0

    for coin in coins:
        while True:
            opening_print(MAX_FUNDS, MENU_DELAY)
            print(f" You have inserted ${approx(money, 2)} so far.\n")

            try:
                user_amount = int(input(f" Insert your {coin}s (${coins[coin]}): "))
                insert_amount = user_amount * coins[coin]

                if user_amount > MAX_COINS:
                    print(f"\n ERROR: A maximum of {MAX_COINS} of each coin type is allowed.")
                    sleep(MENU_DELAY)
                    continue
                if get_money() + insert_amount + money > MAX_FUNDS:
                    print(f"\n ERROR: A maximum total of funds allowed is ${MAX_FUNDS}.")
                    sleep(MENU_DELAY)
                    continue
            except ValueError:
                print("\n ERROR: Please enter numbers.")
                sleep(MENU_DELAY)
                continue
            else:
                break

        money += user_amount * coins[coin]
        opening_print(MAX_FUNDS, MENU_DELAY)
        print(f" You have inserted ${approx(money, 2)} so far.\n")

    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, yes_no, f" Confirm coin insertion. (${approx(money, 2)})\n", MAX_FUNDS,
                                 MENU_DELAY)

    if old_choice == 0:
        print(f"\n ${approx(money, 2)} inserted.")
        add_money(money)
        sleep(MENU_DELAY)
    else:
        print(f"\n No coins added. ${approx(money, 2)} returned as change.")
        sleep(MENU_DELAY)
    start_menu()


def request_change():
    opening_print(MAX_FUNDS, MENU_DELAY)

    print(f"Do you want ${get_money()} returned as change?\n\n")

    menu_choice = 0

    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, yes_no, f" Do you want ${get_money()} returned as change?\n", MAX_FUNDS,
                                 MENU_DELAY)

    if old_choice == 0:
        print(f"\n ${get_money()} returned as change.")
        reset_money()
        sleep(MENU_DELAY)
    else:
        print(f"\n Change request cancelled.")
        sleep(MENU_DELAY)
    start_menu()


def settings():
    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, settings_menu_items, "", MAX_FUNDS, MENU_DELAY)

    if old_choice == len(settings_menu_items) - 1: start_menu()

    settings_menu_dict[old_choice]()


def change_max_funds():
    global MAX_FUNDS

    while True:
        opening_print(MAX_FUNDS, MENU_DELAY)
        print(f" Current max allowed funds: ${MAX_FUNDS}")

        try:
            user_funds = int(input("\n New max allowed funds: $"))
            if user_funds <= get_money():
                print("\n ERROR: Cannot lower max funds below current funds.")
                sleep(MENU_DELAY)
                continue
        except ValueError:
            print("\n ERROR: Please enter numbers.")
            sleep(MENU_DELAY)
            continue
        else:
            break

    MAX_FUNDS = user_funds
    print(f"\n New max: ${MAX_FUNDS}")
    sleep(MENU_DELAY)
    settings()


def change_prices():
    update_menus()

    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, flavor_menu_items, "", MAX_FUNDS, MENU_DELAY)

    if old_choice == len(flavor_menu_items) - 1: settings()

    while True:
        opening_print(MAX_FUNDS, MENU_DELAY)

        try:
            new_price = float(input(
                f" {flavor_menu_dict[old_choice]} current price: ${drinks[flavor_menu_dict[old_choice]]}. \n\n New price: $"))
            if new_price > MAX_PRICE:
                print(f"\n ERROR: A maximum price of ${MAX_PRICE} should be set.")
                sleep(MENU_DELAY)
                continue
            if new_price < 0:
                print(f"\n ERROR: A minimum price of 0 should be set.")
                sleep(MENU_DELAY)
                continue
        except ValueError:
            print("\n ERROR: Please enter numbers.")
            sleep(MENU_DELAY)
            continue
        else:
            break

    drinks[flavor_menu_dict[old_choice]] = new_price
    print(f"\n New price of {flavor_menu_dict[old_choice]} is {new_price}.")
    sleep(MENU_DELAY)
    settings()


def add_new_product():
    while True:
        opening_print(MAX_FUNDS, MENU_DELAY)

        try:
            new_product_name = str(input(" New product name: ")).title()
            if len(new_product_name) > 11:
                print("\n ERROR: Max name length is 11 characters.")
                sleep(MENU_DELAY)
                continue
            if new_product_name in drinks:
                print(f"\n ERROR: {new_product_name} already exists.")
                sleep(MENU_DELAY)
                continue
        except ValueError:
            print("\n ERROR: Please enter text.")
            sleep(MENU_DELAY)
            continue
        else:
            break

    while True:
        try:
            opening_print(MAX_FUNDS, MENU_DELAY)
            new_product_price = float(input(" New product price: "))
            if new_product_price > MAX_PRICE:
                print(f"\n ERROR: Price should be no higher than {MAX_PRICE}.")
                sleep(MENU_DELAY)
                continue
            if new_product_price < 0:
                print(f"\n ERROR: A minimum price of 0 should be set.")
                sleep(MENU_DELAY)
                continue
        except ValueError:
            print("\n ERROR: Please enter numbers.")
            sleep(MENU_DELAY)
            continue
        else:
            break

    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, yes_no, f" Add {new_product_name} for ${new_product_price}?\n", MAX_FUNDS,
                                 MENU_DELAY)

    if old_choice == 0:
        drinks[new_product_name] = new_product_price
        update_menus()

        print(
            f"\n {new_product_name} added. Price set at {new_product_price}.")
        sleep(MENU_DELAY)
    else:
        print("\n CANCELLED. No new product added.")
        sleep(MENU_DELAY)
    settings()


def remove_product():
    update_menus()

    menu_choice = 0
    while menu_choice != -1:
        removal_choice = menu_choice
        menu_choice = print_menu(menu_choice, flavor_menu_items, " Choose product to remove:\n", MAX_FUNDS, MENU_DELAY)
    if removal_choice == len(flavor_menu_items) - 1: settings()

    menu_choice = 0
    while menu_choice != -1:
        old_choice = menu_choice
        menu_choice = print_menu(menu_choice, yes_no, f" Confirm removal of{flavor_menu_items[removal_choice]}\n",
                                 MAX_FUNDS, MENU_DELAY)

    if old_choice == 0:
        print(f"\n{flavor_menu_items[removal_choice]} was removed from product list.")
        drinks.pop(flavor_menu_items[removal_choice].strip())
    else:
        print("\n CANCELLED. No products were removed.")
    sleep(MENU_DELAY)
    settings()


def change_delay():
    global MENU_DELAY

    while True:
        opening_print(MAX_FUNDS, MENU_DELAY)
        print(f" Current menu delay: {MENU_DELAY}s.\n")

        try:
            new_delay = int(input(" New menu delay: "))
            if new_delay > 10 or new_delay < 0:
                print("\n ERROR: Please enter a number between 0 and 10.")
                sleep(MENU_DELAY)
                continue
        except ValueError:
            print("\n ERROR: Please enter numbers.")
            sleep(MENU_DELAY)
            continue
        else:
            break

    MENU_DELAY = new_delay
    print(f" \n New menu delay set at {MENU_DELAY}.")
    sleep(MENU_DELAY)
    settings()


def end():
    update_menus()
    system("cls")
    print(soda_off)


main_menu_items = [" Coins / Change", " Choose Flavor", " Random Flavor", " Soda-Crate", " Random Soda-Crate",
                   " Settings", " End"]
main_menu_dict = {
    0: funds,
    1: flavors,
    2: random_flavor,
    3: crate,
    4: random_crate,
    5: settings,
    6: end}

funds_menu_items = [" Insert Coins", " Request Change", " Back"]
funds_menu_dict = {0: insert_coins,
                   1: request_change,
                   2: start_menu}

settings_menu_items = [" Max Allowed Funds", " Menu Delay", " Edit Product Prices", " Add New Product",
                       " Remove Product", " Back"]
settings_menu_dict = {
    0: change_max_funds,
    1: change_delay,
    2: change_prices,
    3: add_new_product,
    4: remove_product,
    5: start_menu}

yes_no = [" Yes", " No"]

loading()
update_menus()
start_menu()
