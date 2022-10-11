def fill(n):
    L = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(2, n):
        for i in range(n - j):
            ind = i + j
            L[i][ind] = j
            print(i, ind)
            print(i, ind - 1)
            print(i + 1, ind)
            print()

    for row in L:
        print(row)


fill(6)
