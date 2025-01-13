# Напиши пошаговый алгоритм действий в комментариях для определения, является ли строка палиндромом.
# Напишите по созданному вами алгоритму функцию для проверки, является ли строка палиндромом.


# сохранить исходную строку в первой переменной
# разбить исходную строку на список символов
# запустить цикл создания нового списка с обратной последовательностью символов
# сравить списки, сообщить о результате


def palindrom(line):
    initial_set = []
    for i in line:
        initial_set.append(i)
    print(initial_set)
    reversed_set = []
    for i in range(len(initial_set)):
        reversed_set.append(initial_set[len(initial_set)-1-i])
    print(reversed_set)
    if initial_set == reversed_set:
        print('Это палиндром')
    else:
        print('это не палиндром', '\n')


palindrom('привет привет')
palindrom('прирп прирп')
