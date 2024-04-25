employee = {
    "Андрій": {
        "salary": "5000",
        "city": "Київ",
        "date of birth": "08.11.2000",
        "date of employment": "06.09.2021"
    },

    "Олег": {
        "salary": "6000",
        "city": "Київ",
        "date of birth": "04.12.1995",
        "date of employment": "09.09.2020"
    },

    "Антон": {
        "salary": "5500",
        "city": "Київ",
        "date of birth": "03.05.1994",
        "date of employment": "01.04.2019"
    }
}


while True:
    print("1.додати працівника\n"
          "2.видалити працівника\n"
          "3.переглянути список працівників\n"
          "4.змінити зарплату працівника")
    choice = int(input(f"виберіть дію:"))
    if choice == 1:
        name = input("ведіть ім'я працівника")
        salary = input("ведіть зарплату працівника")
        city = input("ведіть місто працівника")
        date_of_birth = input("ведіть дату народження працівника")
        date_of_employment = input("ведіть дату прийняття працівника на роботу працівника")
        employee.update({name: {"salary": salary,
                                  "city": city,
                                  "date_of_birth": date_of_birth,
                                  "date_of_employment": date_of_employment,}})
    if choice == 2:
        print("список працівників:")
        for i in employee:
            print(i)
        name = input("ведіть ім'я працівника якого хочете видалити: ")
        employee.pop(name)
    if choice == 3:
        print("список працівників:")
        for i in employee:
            print(i)
    if choice == 4:
        print("список працівників:")
        for i in employee:
            print(i)
        name = input("ведіть ім'я працівника: ")
        salary = input("ведіть зарплату працівника: ")
        employee[name]["salary"] = salary
        print(employee[name])
