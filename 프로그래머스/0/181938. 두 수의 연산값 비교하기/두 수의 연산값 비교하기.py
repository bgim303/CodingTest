def solution(a, b):
    answer = int(str(a)+str(b))
    ans2 = 2 * a * b
    if answer > ans2:
        return answer
    elif answer < ans2:
        return ans2
    else:
        return answer