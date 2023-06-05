# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    try:

        symbols_list = list(map(chr, range(97, 123)))  # Создаем список из латинских букв
        length_1, length_2 = random.randint(1, 15), random.randint(1, 15)  # Создаем длину слов от 1 до 15
        word_1_symbols = random.choices(symbols_list, k=length_1)  # Генерируем список символов первого слова
        word_2_symbols = random.choices(symbols_list, k=length_2)  # Генерируем список символов второго слова
        word_1 = ''.join(word_1_symbols)  # Склеиваем строку-слово1
        word_2 = ''.join(word_2_symbols)  # Склеиваем строку-слово2
        string = ' '.join([word_1, word_2])  # Создаем строку слово1, пробел, слово2
        yield string

    finally:
        while len(string) >0:
            yield string


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))



