def solution(my_string):
    answer = [my_string.count(alphabet) 
              for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()
              + 'abcdefghijklmnopqrstuvwxyz']
    return answer