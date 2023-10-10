MONEY = 10.0
drinks = {"Coca Cola": 0.6, "Pepsi": 0.5, "Fanta": 0.6, "Monster": 1.1, "Trocadero": 0.4}
coins = {"Penny": 0.01, "Nickel": 0.05, "Dime": 0.1, "Quarter": 0.25, "Half Dollar": 0.5, "Dollar": 1.0}


def get_money():
    """Returns the current available funds."""

    return approx(MONEY, 2)


def subtract_money(num):
    """Subtracts the given amount from remaining funds."""

    global MONEY
    MONEY -= num


def add_money(num):
    """Adds the given amount to remaining funds."""

    global MONEY
    MONEY += num


def reset_money():
    """Sets the remaining funds to 0."""

    global MONEY
    MONEY = 0


def drink_items():
    """Returns the amount of available flavors."""

    return len(drinks)


def price_of_item(item):
    """Returns the price of a requested item."""

    return drinks[item]


def enough_money(num):
    """Checks if a given amount of funds are available."""

    global MONEY
    if MONEY < num:
        return False
    else:
        return True


def total_cost(crate_list):
    """Returns the total cost of a crate of soda."""

    total = 0
    for soda in crate_list:
        if soda in drinks:
            total += drinks[soda]
    return approx(total, 2)


def approx(num, decimals):
    """Rounds a decimal number to given number of decimals."""

    multiplier = 10 ** decimals
    return int(num * multiplier) / multiplier
