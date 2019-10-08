# Задание 2
# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов.


def second_max_arg(*args):
    """Параметры передаваемые должны быть одного типа
    иначе TypeError при сравении"""

    list_sorted = sorted(args)
    k = 1
    while list_sorted[k] == list_sorted[0]:
        k += 1
    return list_sorted[k]


def second_max_arg_set(*args):
    """Параметры передаваемые должны быть одного типа
    иначе TypeError при сравении"""

    list_sorted = sorted(set(args))
    return list_sorted[1]


if __name__ == '__main__':
    l1 = (1, 1, 5, 8, 3, 6, 7, 7, 9, 2)
    l2 = ('a', 'b', 'cc', 'a')
    print(second_max_arg(*l1))
    print(second_max_arg(*l2))
    print(second_max_arg_set(*l1))
    print(second_max_arg_set(*l2))
