p = []

dst = ["Польща", "Швейцарія", "Швеція", "Перу", "Бразилія"]

print(f"привіт виберіть місце призначення:")
for x, city in zip(range(len(dst)), dst):
    print(f"{x}-{dst [x]}")
i = int(input("Enter index:"))
print("Вітаємо на борту!")
p.append(dst[i])

print("Сьогодні відбудуться рейси у країни:")
for i in p:
    print(i)


#while True:
    #print(f"привіт виберіть місце призначення {dst}")

