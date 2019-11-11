# 1.
# ��: ������ �����, �����: ���-�� �����
# ��� ������ > 2 �������� � ������ ������ == ����������


def me(words):
    count = 0
    for i in words:
        if len(i) > 2 and i[0] == i[-1]:
            count += 1
    return count


# 2. 
# ��: ������ �����, �����: ������ �� �������� (�����������)
# �� ���� ���� ����� ������������ � 'x', ������� �������� � ������ ������.
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
# ��: ������ �������� ��������, 
# �����: ������ ������ �� ����������� ���������� �������� � ������ ����.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def fs(list_of_tuples):
    list_of_tuples.sort(key=lambda tuple: tuple[-1])
    return list_of_tuples

if __name__ == '__main__':
    main()
