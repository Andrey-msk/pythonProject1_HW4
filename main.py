'''
1. Реализовать скрипт,
 в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
  В расчете необходимо использовать формулу:
   (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
def cash():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка '))
        bonus = int(input('Премия '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
cash()


#2

my_list = [2, 3, 4, 5, 6, 8, 9, 7]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

#3

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

#4

my_list = [1, 5, 5, 7, 3, 7, 6, 25, 8, 25]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

#5

from functools import reduce

def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

#6

from itertools import count
from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
my_count_func(start_number = int(input("Введите стартовое число: ")), stop_number = int(input("Введите конечное число: ")))
my_cycle_func(my_list = ['Pyton'], iteration = int(input("Введите число повторений слова 'Pyton' : ")))

#7

def fibo_gen(n):
    el = 1
    count = 1
    for i in range(1,n+1):
        el = el*i
        count += 1
        if count != 15:
            yield el

for el in fibo_gen(20):
    print(el)





