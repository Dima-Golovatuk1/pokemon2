def del_file():
    with open("shop.txt", "r") as file:
        for line in file:
            # Розділяємо рядок за роздільником ":"
            parts = line.strip().split(": ")
            print(parts)

del_file()
