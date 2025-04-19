from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)
    
    for i in report:
        poli, coco = i.split()
        user[poli].add(coco)
        cnt[coco] += 1
        
    for j in id_list:
        result = 0
        for t in user[j]:
            if (cnt[t] >= k):
                result +=1
        answer.append(result)
    
    return answer