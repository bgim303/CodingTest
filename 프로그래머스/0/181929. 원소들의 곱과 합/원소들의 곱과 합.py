def solution(num_list):
    answer = 0
    sum = 0
    mult = 1
    for i in num_list:
        sum += i
        mult *= i
    
    if sum*sum > mult:
        answer = 1
        
    
    return answer