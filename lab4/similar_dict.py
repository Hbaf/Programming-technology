"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...]

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach


"""

import random
import sys


def read_from_file(file):
    text = file.read().replace('\n', ' ')
    while "  " in text:
        text = text.replace("  ", ' ')
    return text


def mem_dict(text):
    dict = {}
    lst = text.split(' ')
    for i in range(len(lst) - 1):
        if lst[i] in dict:
            dict.get(lst[i]).add(lst[i+1])
        else:
            dict.update({lst[i]: {lst[i+1]}})

    if lst[-1] in dict:
        dict.get(lst[-1]).add(None)
    else:
        dict.update({lst[-1]: {None}})
    lst = []
    for i in dict.keys():
        lst.append(i)
    dict.update({'': lst})

    return dict


def dict_to_text(dict):
    text = ''
    current_word = list(dict[''])[random.randint(0, len(dict['']) - 1)]
    while current_word is not None:
        text += ' ' + current_word
        prev_current_word = current_word
        current_word = list(dict[prev_current_word])[random.randint(0, len(dict[prev_current_word]) - 1)]
    return text


def main():
    print(dict_to_text(mem_dict(read_from_file(open(sys.argv[1], 'r')))))


if __name__ == '__main__':
    main()
