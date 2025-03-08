def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        for p in possible:
            if p * 2 not in word: 
                word = word.replace(p, ' ')
        if word.strip() == '':
            count += 1
    
    return count
