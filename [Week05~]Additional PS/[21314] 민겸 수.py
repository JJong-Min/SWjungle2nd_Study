import sys

strings = list(sys.stdin.readline().rstrip())

max_val = ''
min_val = ''
now_string = ''
m_num = 0
# max_val 구하기
for s in strings:
    if now_string == '':
        if s == 'K':
            max_val += '5'
        else:
            m_num += 1
            now_string += 'M'
    else:
        if s == 'K':
            max_val += str(5 * (10 ** m_num))
            now_string = ''
            m_num = 0
        else:
            m_num += 1
            now_string += 'M'
if m_num != 0:
    max_val += '1' * m_num

now_string = ''
m_num = 0
#min_val 구하기
for s in strings:
    if now_string == '':
        if s== 'K':
            min_val += '5'
        else:
            m_num += 1
            now_string += 'M'

    else:
        if s == 'K':
            min_val += str(10 ** (m_num - 1))
            min_val += '5'
            now_string = ''
            m_num = 0
        else:
            m_num += 1
            now_string += 'M'

if m_num != 0:
    min_val += str(10 ** (m_num - 1))

print(max_val)
print(min_val)
