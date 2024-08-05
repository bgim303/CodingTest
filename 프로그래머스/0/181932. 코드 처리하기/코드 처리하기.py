def solution(code):
    res = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0 : 
            if code[i] != '1' and i % 2 == 0:
                res += code[i]
            elif code[i] == '1':
                mode = 1
        else :
            if code[i] != '1' and i % 2 == 1 :
                res += code[i]
            elif code[i] == '1':
                mode = 0
    if res == '':
        return 'EMPTY'
    return res