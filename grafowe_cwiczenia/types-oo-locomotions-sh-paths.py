"""
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.
"""
import heapq


def islands(G, A, B):
    V = len(G)
    New_V = 3 * V + 2
    inf = float('inf')

    New_Graph = [[-1 for _ in range(New_V)] for _ in range(New_V)]
    for i in range(V):
        for j in range(i, V):
            if G[i][j] > 0:
                if G[i][j] == 1:
                    New_Graph[3 * i][3 * j + 1] = 1
                    New_Graph[3 * i][3 * j + 2] = 1
                    New_Graph[3 * j][3 * i + 1] = 1
                    New_Graph[3 * j][3 * i + 2] = 1

                elif G[i][j] == 5:
                    New_Graph[3 * i + 1][3 * j] = 5
                    New_Graph[3 * i + 1][3 * j + 2] = 5
                    New_Graph[3 * j + 1][3 * i] = 5
                    New_Graph[3 * j + 1][3 * i + 2] = 5

                elif G[i][j] == 8:
                    New_Graph[3 * i + 2][3 * j] = 8
                    New_Graph[3 * i + 2][3 * j + 1] = 8
                    New_Graph[3 * j + 2][3 * i] = 8
                    New_Graph[3 * j + 2][3 * i + 1] = 8

    New_Graph[New_V - 2][3 * A] = 0
    New_Graph[New_V - 2][3 * A + 1] = 0
    New_Graph[New_V - 2][3 * A + 2] = 0
    New_Graph[3 * A][New_V - 2] = 0
    New_Graph[3 * A + 1][New_V - 2] = 0
    New_Graph[3 * A + 2][New_V - 2] = 0

    New_Graph[New_V - 1][3 * B] = 0
    New_Graph[New_V - 1][3 * B + 1] = 0
    New_Graph[New_V - 1][3 * B + 2] = 0
    New_Graph[3 * B][New_V - 1] = 0
    New_Graph[3 * B + 1][New_V - 1] = 0
    New_Graph[3 * B + 2][New_V - 1] = 0

    Dist = [inf for _ in range(New_V)]
    Dist[New_V - 2] = 0
    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, (Dist[New_V - 2], New_V - 2))
    while Q:
        weight, u = heapq.heappop(Q)
        for v in range(New_V):
            if New_Graph[u][v] > -1:
                new_dist = Dist[u] + New_Graph[u][v]
                if new_dist < Dist[v]:
                    Dist[v] = new_dist
                    heapq.heappush(Q, (new_dist, v))

    if Dist[New_V - 1] >= inf:
        return None
    return Dist[New_V - 1]


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]
print(islands(G1, 5, 2))
#
# G2 = [[0, 8, 5, 0, 0, 0, 1, 0],
#       [8, 0, 0, 5, 0, 0, 0, 0],
#       [5, 0, 8, 5, 0, 0, 0, 0],
#       [0, 5, 8, 0, 1, 5, 0, 0],
#       [0, 0, 5, 1, 0, 1, 0, 7],
#       [0, 0, 0, 5, 1, 0, 0, 0],
#       [1, 0, 0, 0, 0, 0, 0, 1],
#       [0, 0, 0, 0, 5, 0, 0, 1]]
# print(islands(G2, 0, 4))

# G3 = [[0, 1, 8, 0],
#       [1, 0, 8, 0],
#       [8, 8, 0, 1],
#       [0, 0, 1, 0]]
# print(islands(G3, 0, 3))


# no i sie wysralo przy tym przykladzie # upadete - juz dziala! :D
G4 = [[0, 8, 8, 0, 0, 0, 0, 0],
      [8, 0, 0, 5, 0, 0, 0, 0],
      [8, 0, 0, 5, 0, 0, 0, 0],
      [0, 5, 5, 0, 8, 1, 0, 0],
      [0, 0, 0, 8, 0, 0, 5, 0],
      [0, 0, 0, 1, 0, 0, 8, 0],
      [0, 0, 0, 0, 5, 8, 0, 8],
      [0, 0, 0, 0, 0, 0, 8, 0]]
print(islands(G4, 0, 7))
