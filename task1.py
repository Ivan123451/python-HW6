# Задача 30:
# Заполните список элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_element = int(input('введите первый элемент: '))
diff = int(input('введите разность: '))
number_of_elrment = int(input('введите количество элементов:'))

new_list = []

for i in range(number_of_elrment):
    new_list.append(first_element + (i)*diff)

print(new_list)
