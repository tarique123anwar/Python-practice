if __name__ == '__main__':
    scores = set()
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        records.append([name, score])
    scores.remove(min(scores))
    result = sorted([records[i][0] for i in range(len(records)) if min(scores) == records[i][1]])
    print(*result, sep='\n')