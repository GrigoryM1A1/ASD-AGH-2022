"""
Knapsack problem

f(i, b) = maksymalna suma cen przedmiotow ze zbioru {0, ... i} nie przekraczajaca wagi b
wynik: f(n-1, B)

f(i, b) = max{ f(i-1, b), f(i-1, b -W[i]) + P[i]) | b - W[i] >= 0

f(0, b) = P[0], W[0] <= b and 0, W[0] > b
"""


def knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    Parent = [[[0, -1, -1] for b in range(B + 1)] for i in range(n)]
    # (gdzie idziemy i, gdzie idziemy b, czy bierzemy)

    # mozemy wziac przedmiot dla kazdej pojemnosci o wiekszej lub rownej wadze niz waga danego przedmiotu
    for b in range(W[0], B + 1):
        F[0][b] = P[0]
        Parent[0][b] = [1, -1, -1]

    for i in range(1, n):
        for b in range(B + 1):
            q = F[i-1][b]
            # nie bierzemy
            Parent[i][b] = [0, i - 1, b]
            if b - W[i] >= 0 and F[i-1][b-W[i]] + P[i] > q:
                # bierzemy jesli mozemy
                q = F[i-1][b-W[i]] + P[i]
                Parent[i][b] = [1, i-1, b - W[i]]
            F[i][b] = q
    # for row in Parent:
    #     print(row)

    res = []
    curr = Parent[n - 1][B]
    i = n - 1
    while i >= 0:
        if curr[0] == 1:
            res.append(i)
            curr = Parent[curr[1]][curr[2]]
            i -= 1
        else:
            curr = Parent[curr[1]][curr[2]]
            i -= 1
    print(res)

    # printing items
    # items = []
    # curr_prof = F[n-1][B]
    # curr_w = B
    # for i in range(n-1, 0, -1):
    #     if curr_prof == F[i-1][curr_w]:
    #         pass
    #     else:
    #         items.append(i)
    #         curr_prof -= P[i]
    #         curr_w -= W[i]
    # if curr_w - W[0] == 0:
    #     items.append(0)
    #     curr_w -= W[0]
    # print(curr_w)
    # print(items)

    return F[n-1][B]


# profits = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50
# print(knapsack(weights, profits, capacity))
# print()
Profits = [10, 5, 15, 7, 6, 18, 3]
Weights = [2, 3, 5, 7, 1, 4, 1]
Capacity = 15
print(knapsack(Weights, Profits, Capacity))
