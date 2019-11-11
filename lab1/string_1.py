# 1.
# �������� ���������: int <count> , 
# ���������: string � �����
# "Number of: <count>", ��� <count> ����� �� ����.�����.
#  ���� ����� ����� 10 ��� �����, ���������� "many"
#  ������ <count>
#  ������: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'


def num_of_items(count):
    return 'Number of: ' + str(count) if count < 10 else 'Number of: many'


# 2. 
# �������� ���������: string s,
# ���������: string �� 2� ������ � 2� ��������� �������� s
# ������ 'welcome' -> 'weme'.
def start_end_symbols(s):
    return s[:2]+s[-2:]


# 3. 
# �������� ���������: string s,
# ���������: string ��� ��� ��������� 1�� ������� ���������� �� '*'
# (����� ������ 1�� �������)
# ������: 'bibble' -> 'bi**le'
# s.replace(stra, strb) 

def replace_char(s):
    return s[0] + s[1:].replace(s[0], '*')


# 4
# �������� ���������: string a � b, 
# ���������: string ��� <a> � <b> ��������� �������� 
# � ������ 2 ���� ����� ����� �������� ���� �� �����
# �.�. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    return b[0:1] + a[2:] + ' ' + a[0:1] + b[2:]


# return


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(res, expt):
    # return

    test(start_end_symbols('welcome'), 'weme')

    test(replace_char('bibble'), 'bi**le')


if __name__ == '__main__':
    main()
