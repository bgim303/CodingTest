def solution(myString, pat):
    answer = myString.replace('A', 'temp').replace('B', 'A').replace('temp', 'B')
    if pat in answer:
        return 1
    else:
        return 0