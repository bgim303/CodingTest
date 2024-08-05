import math
def solution(a, b, c):
    answer = 0
    if a == b and b == c and c==a:
        #answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
        answer = (a + b + c) * ((math.pow(a, 2)) + (math.pow(b, 2)) + (math.pow(c, 2))) * ((math.pow(a, 3)) + (math.pow(b, 3)) + (math.pow(c, 3)))
    elif a == b or b == c or a == c:
        #answer = (a + b + c) × (a**2 + b**2 + c**2 )
        answer = (a + b + c) * ((math.pow(a, 2)) + (math.pow(b, 2)) + (math.pow(c, 2)))
    else:
        answer = (a+b+c)
    return answer