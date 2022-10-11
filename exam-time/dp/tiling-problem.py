"""Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board
using the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e.,
as 2 x 1 tile. """


def tiles(n):
    F = [0 for _ in range(n+1)]
    F[1] = F[0] = 1
    # f(i) = liczba mozliwych ulozen plytek
    # f(i) = f(i-1) + f(i-2)
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]


print(tiles(4))
