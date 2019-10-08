# Задание 3
# Напишите функцию, которая удаляет все небуквенные символы внутри строки
# (ограничимся латинским алфавитом).
# Проверьте, что вы правильно закодили с помощью инструкции assert.


def dell_not_alpha(s: str) -> str:
    """Принимаем строку, возвращаем эту строку содержащую только латинские буквы"""
    s1 = ''
    for char in s:
        if char.isalpha():
            s1 = s1 + char
    # return s1 + '1'
    return s1


if __name__ == '__main__':
    a = ' 1 2l,ol!!=23 '
    assert dell_not_alpha('12dsfdsf').isalpha()
    print(dell_not_alpha(a))
