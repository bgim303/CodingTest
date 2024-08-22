import math

def solution(numer1, denom1, numer2, denom2):
    mother = denom1*denom2
    res = denom1*numer2 + denom2*numer1
    c = math.gcd(mother, res)
    answer = [res/c, mother/c]
    return answer