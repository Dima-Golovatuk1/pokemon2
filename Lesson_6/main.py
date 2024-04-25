num3 = int(1)
for num in range(1, 11):
    print(f"таблиця множення на {num3}:")
    num3 += 1
    for num2 in range(1, 11):
        result = num * num2
        print(f"{num} * {num2} = {num * num2}")


# 2 Завдання
print (f"завдання номер 2:")
numbers = 0
for i in range(1, 101, 2):
    numbers += i
print(numbers)