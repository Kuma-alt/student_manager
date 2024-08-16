import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        # Додавання нового студента
        name = input("Введіть імя студента")
        age = int(input("vvedit vik"))
        major = input("vvedit special student")

        cursor.execute('''INSERT INTO students (name, age, major)
VALUES ?, ?, ?''', (name, age, major))
        
        conn.commit()

    elif choice == "2":
    # Додавання нового курсу
        course = input("vvedit nazva kursu")
        instructor = input("vv")

        cursor.execute('''INSERT INTO course (name, instructor)
                       VAlUES ?,? ''',
                       (course, instructor))
    elif choice == "3":
        # Показати список студентів
    cursor.execute('''SELECT * FROM students ''')
    result = cursor.fetchall()
    if result:
        print(result)
    else:
        print("tablica poroznya")


    elif choice == "4":
        # Показати список курсів
        cursor.execute('''SELECT * FROM courses ''')
    elif choice == "5":
        ...
        # Зареєструвати студента на курс

    elif choice == "6":
        # Показати студентів на конкретному курсі
       ...
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")

conn.commit()
cursor