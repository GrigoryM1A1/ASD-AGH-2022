"""#
dp(i, j, k) = minimalny koszt dotarcia do (finish_a, finish_b) zaczynając w polu (i, j),
                       będąc zwróconym w stronę k

side = 'L' = lewo = 0, 'R' = prawo = 1, 'U' = góra = 2, 'D' = dół = 3
k = obroty: 'L' = w przeciwną niż zegar = 0, 'R' = zgodnie z zegarem = 1
    bieg:   'S1' = start biegu = 2, 'S2' = robot troche rozpędzony = 3, 'S3' = robot z maksymalną prędkością = 4
"""


def rec(L, i, j, k, last_speed, dp, n, m):
    inf = float('inf')
    if not (0 <= i < m and 0 <= j < n):
        return inf

    if L[i][j] == 'X':
        dp[i][j][k] = inf
        return dp[i][j][k]

    if dp[i][j][k] is not None:
        return dp[i][j][k][k]

    # calculate curr_speed
    speed = 0
    if last_speed == 0:
        speed = 60

    elif last_speed == 60:
        speed = 40

    elif last_speed == 40:
        speed = 30

    elif last_speed == 30:
        speed = 30

    res = 0
    if k == 0:      # obrot i speed 0                       obrot i speed 0
        res = min(45 + rec(L, i, j, 2, 0, dp, n, m), 45 + rec(L, i, j, 3, 0, dp, n, m),
                  speed + rec(L, i, j + 1, 0, speed, dp, n, m))

    elif k == 1:
        res = min(45 + rec(L, i, j, 2, 0, dp, n, m), 45 + rec(L, i, j, 3, 0, dp, n, m),
                  speed + rec(L, i, j - 1, 1, speed, dp, n, m))

    elif k == 2:
        res = min(45 + rec(L, i, j, 0, 0, dp, n, m), 45 + rec(L, i, j, 1, 0, dp, n, m),
                  speed + rec(L, i - 1, j, 2, speed, dp, n, m))

    elif k == 3:
        res = min(45 + rec(L, i, j, 0, 0, dp, n, m), 45 + rec(L, i, j, 1, 0, dp, n, m),
                  speed + rec(L, i + 1, j, 3, speed, dp, n, m))

    dp[i][j][k] = res
    return res


# wstępnie O(n*n*k*side) == O(n^2), k i side są ustalone
def robot(L, A, B):
    m = len(L)
    n = len(L[0])
    k = 4
    dp = [[[None for _ in range(k)] for _ in range(n)] for _ in range(m)]
    dp[B[0]][B[1]][0] = 0
    rec(L, A[0], A[1], 0, 0, dp, n, m)

    return max(dp[A[0]][A[1]])


Lab = ["XXXXXXXXXX",
       "X X      X",
       "X XXXXXX X",
       "x        X",
       "xxxxxxxxxx"]
Start = (1, 1)
Finish = (3, 8)
print(robot(Lab, Start, Finish))
