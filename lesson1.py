import random
# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы
        5. Вывести средний балл по каждому предмету для конкретного ученика
        6. Вывести все оценки по конкретному ученику
        7. Удалить данные по ученикам
        8. Добавление нового ученика
        9. Добавление нового предмета
        10. Удаление предмета
        11. Изменение оценок учеников''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предметуч
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Выход из программы')
        break
    elif command == 5:
        print('5. Вывести средний балл по каждому предмету для конкретного ученика')
        for student in students:
            print(student)
        student = input('Введите имя студента:')
        if student in students:
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
        else:
            print('Данного ученика нету в списках')
    elif command == 6:
        print('6. Вывести все оценки по конкретному ученику')
        for student in students:
            print(student)
        student = input('Введите имя ученика:')
        if student in students:
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        else:
            print('Данного ученика нету в списках')
    elif command == 7:
        print('7. Удалить данные по ученикам')
        for student in students:
            print(student)
        student = input('Введите имя ученика которого нужно удалить: ')
        if student in students:
            students.remove(student)
            print('Ученик удален из списка')
        else:
            print('Ученика нету в списке')
    elif command == 8:
        print('8. Добавление нового ученика')
        student = input('Введите имя нового ученика:')
        if student in students:
            print('Ученик уже в списках')
        else:
            students.append(student)
            for student in students:
                print(student)
    elif command == 9:
        print('9. Добавление нового предмета')
        class_ = input('Введите название нового предмета:')
        if class_ in classes:
            print('Предмет уже в списках')
        else:
            classes.append(class_)
            for class_ in classes:
                print(class_)
    elif command == 10:
        print('10. Удаление предмета')
        class_ = input('Введите назнвание предмета, который стоит удалить:')
        if class_ in classes:
            classes.remove(class_)
            print('Предмет удален')
            print()
            print('Список предметов:')
            for class_ in classes:
                print(class_)
        else:
            print('Предмета нет в списках')
    elif command == 11:
        print('11. Изменение оценок учеников')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            marks = input('Введите новые оценки: ')
        students_marks[student][class_] = [marks]
        print(f'Оценки {student}:')
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')











