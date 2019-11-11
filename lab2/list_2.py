# 1. 
# Вх: список чисел, Возвр: список чисел, где 
# повторяющиеся числа урезаны до одного 
# пример [0, 2, 2, 3] returns [0, 2, 3]. 

def rm_adj(nums):
    temp_set = set(nums)
    return list(temp_set)


# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список 

def mrg_lsts(list1, list2):
    counter = 0
    for i in list1:
        while i > list2[counter]:
            counter += 1
        list2.insert(counter, i)

    return list2


if __name__ == '__main__':
    main()
