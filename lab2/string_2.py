# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing", 
# если в конце нет уже "ing", иначе добавить "ly".
def v(s):
    if len(s) > 3:
        if str(s).endswith("ing"):
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s


# 2. 
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!

def nb(s):
    nS = str(s).find("not")
    if nS != -1:
        bS = str(s).find("bad", nS)
        if bS != -1: return s[:nS] + "good" + s[bS + 3:]
    return s
