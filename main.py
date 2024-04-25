import my_geometry

while True:
    print(f"1.обчислити площу кола\n"
          f"2.обчислити площу прямокутника")
    choice = int(input(f"Зробіть вибір: "))
    if choice == 1:
        radius = int(input(f"Ведіть радіус кола: "))
        my_geometry.circle_area(radius)
    elif choice == 2:
        width = int(input(f"Ведіть ширину прямокутника: "))
        height = int(input(f"Ведіть висоту прямокутника: "))
        my_geometry.rectangle_area(width, height)
    else: print(f"виберіть цифру із запропонованих")






