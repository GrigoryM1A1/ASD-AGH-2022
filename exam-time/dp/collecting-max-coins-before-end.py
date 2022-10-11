"""
Given a character matrix where every cell has one of the following values.

'C' -->  This cell has coin

'#' -->  This cell is a blocking cell.
         We can not go anywhere from this.

'E' -->  This cell is empty. We don't get
         a coin, but we can move from here.
Initial position is cell (0, 0) and initial direction is right.

Following are rules for movements across cells.

If face is Right, then we can move to below cells
Move one step ahead, i.e., cell (i, j+1) and direction remains right.
Move one step down and face left, i.e., cell (i+1, j) and direction becomes left.

If face is Left, then we can move to below cells
Move one step ahead, i.e., cell (i, j-1) and direction remains left.
Move one step down and face right, i.e., cell (i+1, j) and direction becomes right.

Final position can be anywhere and final direction can also be anything. The target is to collect maximum coins.
"""

"""
dp(i, j, k) = maksymalna liczba zebranych pieniedzy zaczynajac z pola (i, j) bedac zwrocony w strone k
k = 1 == right      k = 0 == left

if Grid[i][j] == "E" or i, j poza tablica:
    return 0
    
res = 1 if Grid[i][j] == "C" else 0
dp(i, j, 0) = max( dp(i+1, j, 1), dp(i, j-1, 0) ) #idziemy w dol albo w lewo

dp(i, j, 1) = max( dp(i+1, j, 0), dp(i, j+1, 1) ) #idziemy w dol albo w prawo 
"""


# left == 0     right == 1
def rec(Grid, dp, i, j, d, m, n):
    if not (0 <= i < m and 0 <= j < n) or Grid[i][j] == '#':
        return 0

    if dp[i][j][d] != -1:
        return dp[i][j][d]

    res = 0
    if Grid[i][j] == 'C':
        res = 1

    if d == 1:          # down                              right
        res = res + max(rec(Grid, dp, i + 1, j, 0, m, n), rec(Grid, dp, i, j + 1, 1, m, n))

    if d == 0:          # down                              left
        res = res + max(rec(Grid, dp, i + 1, j, 1, m, n), rec(Grid, dp, i, j - 1, 0, m, n))

    dp[i][j][d] = res
    return dp[i][j][d]


def getting_rich(Grid):
    m = len(Grid)
    n = len(Grid[0])
    dp = [[[-1 for i in range(2)] for j in range(n)] for k in range(m)]

    rec(Grid, dp, 0, 0, 1, m, n)
    return dp[0][0][1]


A = ['ECCCC',
     'C#C#E',
     '#CC#C',
     'CEECE',
     'CE#CE']
print(getting_rich(A))
