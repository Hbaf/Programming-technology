# 1.
# ��: ������. ���� ����� > 3, �������� � ����� "ing", 
# ���� � ����� ��� ��� "ing", ����� �������� "ly".
def v(s):
    if len(s) > 3:
        if str(s).endswith("ing"):
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s


# 2. 
# ��: ������. �������� ��������� �� 'not' �� 'bad'. ('bad' ����� 'not')
# �� 'good'.
# ������: So 'This music is not so bad!' -> This music is good!

def nb(s):
    nS = str(s).find("not")
    if nS != -1:
        bS = str(s).find("bad", nS)
        if bS != -1: return s[:nS] + "good" + s[bS + 3:]
    return s
