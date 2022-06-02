'''
Tablica MxN
f(x, y) = najdłuższa ścieżka do punktu (x, y)
Na starcie mamy dany punkt startowy, czyli dla ułatwienia oznaczmy punkt (x0, y0) jak punkt koncowy
i wykonujmy ruch tylko jeżeli skaczemy na pole o wartosci mniejszej niż ta na której stoimy
'''


def longest_path_in_grid(A, x0, y0):
    def available_moves(i, j):
        nonlocal A, n, m
        move_tab = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        res = []
        for move in move_tab:
            if 0 <= move[0] < m and 0 <= move[1] < n:
                if A[move[0]][move[1]] > A[i][j]:
                    res.append(move)
        return res

    def rec(i, j):
        #print(i, j)
        nonlocal A, F, n, m, inf
        moves = available_moves(i, j)
        #print(moves)
        if len(moves) == 0:
            F[i][j] = 1
            return F[i][j]

        longest = -inf
        for x in moves:
            longest = max(longest, rec(x[0], x[1]) + 1)
        F[i][j] = longest
        return F[i][j]

    m = len(A)
    n = len(A[0])
    inf = float('inf')
    F = [[None for i in range(n)] for j in range(m)]
    F[x0][y0] = 1
    rec(x0, y0)

    print(F[x0][y0])
    return F[x0][y0]


Arr = [[0, 2, 7, 10],
       [7, 4, 3, 2],
       [2, 5, 0, 1]]
longest_path_in_grid(Arr, 0, 0)
