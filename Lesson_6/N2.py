to_do_list = []

while True:
    task = input("Ведіть нове завдання (або \"q\" якщо завдання немає):")
    if task.lower() == "q":
        break
    to_do_list.append(task)
print()
print("Ваші завдання:")
for item, tasks in enumerate(to_do_list, 1):
    print(item,".", tasks)

