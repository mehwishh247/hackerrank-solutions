if __name__ == '__main__':
    records = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
        score_list.append(score)
        
    score_list = list(set(score_list))
    score_list.sort()
    
    low = score_list[1]
    
    result = [i[0] for i in records if i[1] == low]
    result.sort()
    
    [print(i) for i in result]