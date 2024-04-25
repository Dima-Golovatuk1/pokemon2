#1 завдання
mark = {
    "Андрій": "3",
    "Марк": "2",
    "Поліна": "5",
    "Настя": "4",
    "Максим": "3",
    "Назар": "4",
    "Антон": "3",
}
mark_plus = {}

for i, value in mark.items():
    if int(value) == 4 or int(value) == 5:
        mark_plus.update({i: value})
print(mark_plus)

#2завдвння
temperatore = {
    "Київ": "+1",
    "Львів": "+1",
    "Одеса": "+7",
    "Житомир": "+2",
    "Суми": "-2",
    "Харків": "-1",
}
sum = int(0)
for i in temperatore.values():
    sum += int(i)
print(sum/len(temperatore))


