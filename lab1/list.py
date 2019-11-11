# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему


def me(words):
    count = 0
    for i in words:
        if len(i) > 2 and i[0] == i[-1]:
            count += 1
    return count


# 2. 
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
    temp_list = []
    words.sort()
    for word in words:
        if word[0] == 'x':
            temp_list.append(word)

    for word in temp_list:
        words.remove(word)

    temp_list.extend(words)
    return temp_list


# 3. 
# Вх: список непустых кортежей, 
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def fs(list_of_tuples):
    list_of_tuples.sort(key=lambda tuple: tuple[-1])
    return list_of_tuples

if __name__ == '__main__':
    main()
