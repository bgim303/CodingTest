def solution(rank, attendance):
    answer = []
    
    for i in range(len(rank)):
        if attendance[i]:
            answer.append((rank[i], i))
    
    answer.sort()
    
    three = []
    for i in range(3):
        three.append(answer[i][1])
    
    return 10000 * three[0] + 100 * three[1] + three[2]