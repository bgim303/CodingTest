def solution(a, b):
    answer = int(str(a)+str(b))
    ans = int(str(b)+str(a))
    if answer < ans:
        return ans
    return answer