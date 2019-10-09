# Задание 4 (на генераторы списков)
# Создайте список 2 в степени N, где N от 0 до 20.

s1 = ([2**n for n in range(20)])
print(s1)

# У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из исходного списка.
s2 = [s % 3 for s in s1]
print(s2)

# У вас есть список, в котором могут быть разные типы данных. Создайте новый список только чисел из этого списка.
l1 = ['lol', 1, 5, [1, 'a', [1, '17', 23, 'a', [100, 1.234]]], 1.5, '6']
print(l1)
# переделано из "непонятно чего" на рекурсивный проход по массиву массивов


def digit_try(mas, result=[]):
    for val in mas:
        if type(val) is int or type(val) is float:
            result.append(val)
        else:
            try: result.append(int(val))
            except TypeError: digit_try(val, result)
            except ValueError:
                try: result.append(float(val))
                except TypeError: digit_try(val, result)
                except ValueError: pass
    return result


print(digit_try(l1))


# У вас есть список, в котором могут быть разные типы данных.
# Создайте новый список только строк, при этом удалите усе небуквенные символы из них.
# Воспользуйтесь функцией из предыдущего задания (импортируйте её из другого своего файла)
from homework_4_3 import dell_not_alpha  # импорт указан здесь для наглядности

l3 = [dell_not_alpha(str_in) for str_in in l1 if type(str_in) is str]
print(l3)

# У вас есть словарь – характеристик человека.
# Ключи например: “name”, “surname”, “age”, “position”, “address”, “skills”.
my_dict = {'name': 'Homer', 'surname': 'Simpson', 'age': 45, 'position': 'Security engineer',
           'address': '742 Evergreen Terrace Springfield', 'skills': ['doh', 'drink beer', 'sleep']}
# - Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.
dict_words = {k: type(my_dict.get(k)) for k in my_dict}
print(dict_words)
# - Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного словаря было строкой.
dict_words = {k: my_dict.get(k) for k in my_dict if type(my_dict.get(k)) is str}
print(dict_words)
# Значения нового словаря должны быть переведены в нижний регистр и удалены всё небуквенные символы из них.
dict_words = {k: dell_not_alpha(dict_words.get(k)).lower() for k in dict_words}
print(dict_words)
