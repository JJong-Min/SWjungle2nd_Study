def solution(files):
    new_files = []
    for file in files:
        head, number, tail = '', '', ''
        check = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                check = True
            
            elif not check:
                head += file[i]
            
            else:
                tail = file[i:]
                break
        new_files.append((head, number, tail))
    
    new_files.sort(key=lambda x : (x[0].upper(), int(x[1])))
    answer = [''.join(i) for i in new_files]    
                
            
    return answer
