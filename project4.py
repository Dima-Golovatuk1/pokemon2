shop = {}
lst = []


def add(product, num):
    file = open("shop.txt", "a")
    file.write(f"{product}: {num}\n")
    file.close()


def display_file():
    file = open("shop.txt", "r")
    content = file.read()
    print(content)
    file.close()


def remove_item(item_name):
    with open("shop.txt", "r") as file:
        lines = file.readlines()  # Зчитуємо всі рядки з файлу
    with open("shop.txt", "w") as file:
        for line in lines:
            if item_name not in line:
                file.write(line)


while True:
    print(f"1.Подивитися список товорів\n"
          f"2. Додати товар\n"
          f"3. Видалити товар\n"
          f"4. Завершити роботу")
    choice = int(input("ведіть число: "))
    if choice == 1:
        display_file()
    if choice == 2:
        product = input("Ведіть продукт який додасте: ")
        num = int(input("Ведіть його кількість: "))
        add(product, num)
        display_file()
    if choice == 3:
        product = input("Ведіть продукт який хочете видалити: ")
        remove_item(product)
        display_file()
    if choice == 4:
        break
    else:
        print()
