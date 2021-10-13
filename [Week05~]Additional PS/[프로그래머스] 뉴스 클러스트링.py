from collections import Counter
def devided_char(strings):
    return_list = []
    if strings[0].isalpha():
        before_char = strings[0]
    else:
        before_char = ''
        
    for idx in range(1, len(strings)):
        new_string = before_char + strings[idx]

        if strings[idx].isalpha():
            if len(new_string) == 2:
                return_list.append(new_string.lower())
            before_char = strings[idx]
        else:
            before_char = ''
            
    return return_list
        
def solution(str1, str2):
    answer = 0
    str1_list = devided_char(str1)
    str2_list = devided_char(str2)
    counter_str1 = Counter(str1_list)
    counter_str2 = Counter(str2_list)
    if len(str1_list) == len(str2_list) == 0:
        answer = 1
    elif len(str1_list) == 0 or len(str2_list) == 0:
        asnwer = 0
    else:
        intersection = set(str1_list) & set(str2_list)
        union = set(str1_list) | set(str2_list)
        intersection_len = 0
        union_len = 0
        for inter in intersection:
            intersection_len += min(counter_str1[inter], counter_str2[inter])
        for uni in union:
            union_len += max(counter_str1[uni], counter_str2[uni])
        return int((intersection_len / union_len) * 65536)
    return answer * 65536
