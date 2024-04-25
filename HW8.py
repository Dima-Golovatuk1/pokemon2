def file_num():
    file = open("num.txt", "r")
    num = file.read()
    num = num.replace(" ", "")
    num = num.replace("\n", "")
    print(num)
    print(num.isdigit())
    file.close()
file_num()
