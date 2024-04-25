num = input("Введіть числа, розділені пробілами: ").split()
num_counts = {}

for i in num:
    if i in num_counts:
        num_counts[i] += 1
    else:
        num_counts[i] = 1

for key, value in num_counts.items():
    print(f"{key}: {value}")
