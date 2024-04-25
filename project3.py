text = input("Ведіть текст").split()
pronoun = ["я", "ти", "він", "вона", "воно", "вони", "ви"]
preposition = ["в", "до", "за", "на", "під", "поза", "без", "для",
"по", "понад", "через", "крім", "поміж", "з-за", "з-під"]
fraction = ["й", "і", "а", "ні", "як", "он", "це", "он", "ген", "нібито", "мовби", "авжеж", "атож",
"аякже", "ото", "онде", "навряд чи", "ледве чи", "що за", "ну й", "куди там", "де й", "хоча б"]

word = []

for i in text:
    if i in pronoun:
        pass
    elif i in preposition:
        pass
    elif i in fraction:
        pass
    elif "," in i:
        word.append(i.replace(",", "").lower())
    else:
        word.append(i.lower())

print(word)

max_word = ""
max_num = 0
not_word = []

for n in range(10):
    for w in word:
        if w.isalpha() and w not in not_word:
            count_w = word.count(w)
            if count_w > max_num:
                max_num = count_w
                max_word = w
    not_word.append(max_word)
    if max_num > 0:
        print(f"Найчастіше повторюване слово в тексті: '{max_word}' зустрічається {max_num} разів")
    else:
        print("У тексті немає повторень слів.")
    max_num = 0
