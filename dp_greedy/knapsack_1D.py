'''
f(i, b) = maksymalna suma cen przedmiotów ze zbioru {0, ... , i} nie przekraczających łącznej wagi b
wynik: f(n-1, B)

f(i, b) = max{ f(i-1, b), f(i-1, b - W[i] + P[i] }
zał: bierzemy i-ty przedmiot o ile b - W[i] > 0
          { P[0], W[0] <= b
f(0, b) = {
          { 0, W[0] > b
'''


def knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    S = [[(-1, -1, -1) for b in range(B+1)] for i in range(n)]

    for b in range(W[0], B+1):
        F[0][b] = P[0]

    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            S[i][b] = i-1, b, 0
            if b - W[i] >= 0:
                # F[i][b] = max(F[i][b], F[i-1][b-W[i]] + P[i])
                if F[i-1][b-W[i]] + P[i] > F[i][b]:
                    F[i][b] = F[i-1][b-W[i]] + P[i]
                    S[i][b] = i-1, b - W[i], 1

    for row in S:
        print(row)
    money = 0
    res = []
    here = n-1, B, S[n-1][B][2]
    while S[here[0]][here[1]][0] != -1:
        if here[2] == 1:
            money += P[here[0]]
            res.append(here[0])
        x = S[here[0]][here[1]][0]
        y = S[here[0]][here[1]][1]
        take = S[x][y][2]
        here = x, y, take
    if P[here[0]] + money == F[n-1][B]:
        res.append(here[0])

    print(res)
    print(F[n-1][B])
    return F[n-1][B]


Profits = [10, 5, 15, 7, 6, 18, 3]
Weights = [2, 3, 5, 7, 1, 4, 1]
Capacity = 15
knapsack(Weights, Profits, Capacity)
