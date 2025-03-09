def solution(dots):
    def get_slope(a, b):
        if dots[b][0] - dots[a][0] == 0:
            return float('inf')
        else:
            return (dots[b][1] - dots[a][1]) / (dots[b][0] - dots[a][0])
    
    if get_slope(0, 1) == get_slope(2, 3):
        return 1
    if get_slope(0, 2) == get_slope(1, 3):
        return 1
    if get_slope(0, 3) == get_slope(1, 2):
        return 1
    
    return 0