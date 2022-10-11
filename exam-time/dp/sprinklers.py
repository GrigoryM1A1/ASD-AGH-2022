"""
https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/sprinklers-7153515e/

To raczej zle zrobione ale nie rozumiem rozwiazania na stronie
"""


# N - num of sprinklers
# Q - num of queries
def sprinklers(N, Q, Cords, Ranges, Queries):
    max_ranges = [[0, 0] for _ in range(N)]
    for i in range(N):
        left = Cords[i] - Ranges[i]
        right = Cords[i] + Ranges[i]
        if Cords[i] > 0 and left <= 0:
            max_ranges[i][0] = 0
            max_ranges[i][1] = right
        elif Cords[i] < 0 and right >= 0:
            max_ranges[i][0] = left
            max_ranges[i][1] = 0
        else:
            max_ranges[i][0] = left
            max_ranges[i][1] = right

    res = []
    for q in Queries:
        cnt = 0
        for x, y in max_ranges:
            if x <= q <= y:
                cnt += 1
        res.append(cnt)
    return res


cor = [-2, -1, -3, 1, 2]
ranges = [5, 5, 5, 5, 5]
qers = [-3, -2, -6, 5, 10]
print(sprinklers(5, 5, cor, ranges, qers))
