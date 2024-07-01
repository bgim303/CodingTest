def solution(n):
    if n == 1:
        return [[1]]
    x = 0
    y = 0

    answer = [[0 for j in range(n)]for i in range(n)]
    offset = 'right'

    for i in range(n*n):
        answer[x][y] = i+1

        if offset == 'right':
            y += 1
            if y == n-1 or answer[x][y+1] != 0:
                offset = 'down'
        elif offset == 'down':
            x += 1
            if x == n-1 or answer[x+1][y] != 0:
                offset = 'left'
        elif offset == 'left':
            y -= 1
            if y == 0 or answer[x][y-1] != 0:
                offset = 'up'
        elif offset == 'up':
            x -= 1
            if x == 0 or answer[x-1][y] != 0:
                offset = 'right'
    return answer