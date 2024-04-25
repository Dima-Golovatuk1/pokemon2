surname = input("Напишіть ваше прізвище: ").lower()
letter = []
num = []


for i in surname:
    letter.append(i)
    num.append(letter.count(i))

max_num = max(num)
max_lettter = letter[num.index(max_num)]

print(f"Найчастіша літера в прізвищі {surname} є {max_lettter} вона повторюється {max_num} рази")