def solution(num_list):
    answer = num_list
    i = len(num_list)-1
    if(num_list[i]>num_list[i-1]):
        answer.append(num_list[i]-num_list[i-1])
    else:
        answer.append(num_list[i]*2)
    return answer