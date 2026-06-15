import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

MENU = {
"P1": {"name": "Phin Sữa Đá", "price": 35000},
"F1": {"name": "Freeze Trà Xanh", "price": 55000},
"T1": {"name": "Trà Sen Vàng", "price": 45000}
}

cart = []


class ItemNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


def show_menu():
    print("MENU")
    for i in MENU:
        print(i, MENU[i]["name"], MENU[i]["price"])


def add():
    global cart

    c = input("code: ")
    q = input("qty: ")

    try:
        q = int(q)
    except:
        print("qty sai")
        logging.error("ValueError qty")
        return

    c = c.strip().upper()

    if c not in MENU:
        print("khong co mon")
        logging.warning("ItemNotFoundError %s", c)
        return

    if q <= 0:
        print("qty <= 0")
        logging.warning("InvalidQuantityError %s", q)
        return

    cart.append((c, q))

    logging.info("Added %s %s", q, c)
    print("added")


def view():
    if len(cart) == 0:
        print("empty")
        return

    total = 0

    for x in cart:
        code = x[0]
        qty = x[1]

        price = MENU[code]["price"]

        total += price * qty
        print(code, qty, price)

    print("TOTAL", total)


def checkout():
    global cart

    if not cart:
        print("empty cart")
        return

    total = 0
    for x in cart:
        total += MENU[x[0]]["price"] * x[1]

    ok = input("pay " + str(total) + " y/n: ")

    if ok == "y":
        print("ok done")
        logging.info("checkout done")
        cart = []
    else:
        print("cancel")


while True:
    print("1.menu 2.add 3.view 4.pay 5.exit")

    c = input(">> ")

    if c == "1":
        show_menu()

    elif c == "2":
        add()

    elif c == "3":
        view()

    elif c == "4":
        checkout()

    elif c == "5":
        logging.info("exit")
        break

    else:
        print("???")