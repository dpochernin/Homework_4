#
# Задание 1. Со значениями по умолчанию
# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
#
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!».
# По умолчанию 0


def song_gen(strings=3, words=3, fin=0) -> str:
    """Функция генерирует песню\n
    strings= - сколько строк будет в песне. По умолчанию 3\n
    words= - сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3\n
    fin= - если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!».
    По умолчанию 0. Если fin не 0 или 1 генерируется
    ! если strings и words отрицательные - берем их по модулю"""
    from math import ceil
    # выполняем выполняем проверки на int, в случае неуспеха генерируется TypeError
    strings = ceil(int(strings))
    words = ceil(int(words))
    assert fin == 0 or fin == 1, "fin={}, must be 0 or 1 only".format(fin)  # переделана проверка на ассерт

    # генерируем песенку
    song_string = ['la'] * words
    song = ('-'.join(song_string) + '\n') * strings
    if fin == 1: song = song[:-1] + '!'
    else: song = song[:-1] + '.'

    return song


if __name__ == '__main__':
    a = 1
    if a != 0:
        print(song_gen(strings=5, words=5, fin=1))
