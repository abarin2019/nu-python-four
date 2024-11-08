"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def check_day_of_born():
    correct_day = False

    while not correct_day:
        day_of_born = input('А теперь введите его день рождения: ')
        if day_of_born.lower() == '6 июня':
            correct_day = True
            print('Верно')
        else:
            print('Неверный день рождения\n')


correct_year = False

while not correct_year:
    year_of_born = int(input('\nВведите год рождения А.С Пушкина:  '))

    if year_of_born == 1799:
        correct_year = True
        check_day_of_born()
    else:
        print('Неверный год рождения')
