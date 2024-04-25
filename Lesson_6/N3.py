store = ["apple", "cherry", "banana", "watermelon"]
sold = []
sold__goods = []
history__add = []

while True:
    print("1. Всі товари")
    print("2. Додати новий товар")
    print("3. Продати товар")
    print("4. Заміна проданого товару")
    print("5. Список проданих товарів")
    print("6. Історія проданих тварів")
    print("7. Список доданих тварів")

    choice = int(input("Ведіть цифру:"))
    if choice == 1:
        print("товари в наявності:")
        for i in store:
            print(i)
    elif choice == 2:
        income = input("Які товари ви хочете додати?:").split(" " or ", ")
        store.extend(income)
        history__add.extend(income)
        for x in income:
            print(f"Додано: {x}")
    elif choice == 3:
        while True:
            print("1 продати товар")
            print("2 Продали всі товари які хотіли")
            choice = int(input("Ведіть цифру:"))
            if choice == 2:
                break
            elif choice == 1:
                sell = input(f"Напишіть товар який хочете продати:").split(" " or ", ")
                for i in sell:
                    if i in store:
                        store.remove(i)
                        print(f"Товар {i} було продано")
                        sold__goods.append(i)
                    else: print(f"Товар {i} який вихочете продати, написано не коректно або його немає")
            else: print(f"Ведіть 1 або 2")
    elif choice == 4:
        while True:
            print(f"1 замінити")
            print(f"2 замінено все що хотіли")
            choice = int(input("Ведіть цифру:"))
            if choice == 1:
                replacement = input(f"напишіть товар який хочете додати:")
                replacement1 = input(f"Напишіть товар який потрібно продати і замінити:")
                if replacement1 in store:
                    index = store.index(replacement1)
                    store[index] = replacement
                    sold__goods.append(replacement1)
                    print(f"Товар {replacement1} було замінено на {replacement}")
                else: print(f"Товар {replacement1} який вихочете продати, написано не коректно або його немає")
            elif choice == 2:
                break
            else:
                print(f"Ведіть 1 або 2")
    elif choice == 5:
        print("Продані товари:")
        for i in sold__goods:
            print(i)
    elif choice == 6:
        print("Історія проданих товарі:")
        sold__goods.reverse()
        for i in sold__goods:
            print(i)
    elif choice == 7:
        for i in history__add:
            print(i)