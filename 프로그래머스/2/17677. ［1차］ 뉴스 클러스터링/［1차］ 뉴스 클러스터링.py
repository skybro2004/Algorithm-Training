def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
        
    str1_dict = {}
    for i in range(len(str1) - 1):
        s = str1[i:i+2]
        if not(s.isalpha()):
            continue
        try:
            str1_dict[s] += 1
        except KeyError:
            str1_dict[s] = 1
    
    str2_dict = {}
    for i in range(len(str2) - 1):
        s = str2[i:i+2]
        if not(s.isalpha()):
            continue
        try:
            str2_dict[s] += 1
        except KeyError:
            str2_dict[s] = 1
    
    str_int = {}
    str_uni = str1_dict
    for key in str2_dict:
        if key in str1_dict:
            str_int[key] = min(str1_dict[key], str2_dict[key])
            str_uni[key] = max(str_uni[key], str2_dict[key])
        else:
            str_uni[key] = str2_dict[key]
    
    str_int_v = sum([str_int[k] for k in str_int])
    str_uni_v = sum([str_uni[k] for k in str_uni])
    try:
        return int(65536*str_int_v/str_uni_v)
    except ZeroDivisionError:
        return 65536