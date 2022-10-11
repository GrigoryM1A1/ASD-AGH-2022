"""
You are a secret agent of S.C.R.E.E.N., who infiltrated the evil organization called Hyena.
You have discovered a vital information and want to send it from city s to city e via unidirectional telegraphs.

Unfortunately, you can't trust anyone, so to be sure that the message was delivered and it is correct,
you want to receive an acknowledgement message from city e. So if the message was sent through cities ,
then city e sends an acknowledgement message to , then  sends an acknowledgement message to  and so on,
until s receives acknowledgement message.

However, the telegraph lines only work in one direction, thus, the acknowledgement message may be sent back
through any other cities. Moreover, for each telegraph line that can send messages from city u to city v
there is an information about delivery cost for a single message.

Your task is to find the minimal cost it takes to send message from city s to city e and get an acknowledgement message,
or output -1, if it's impossible.
"""
import heapq


# niby jakis podwojny floyd-warshall
# imo dijkstra(s -> e) + dijkstra(r -> s)
def dijkstra(G, s):
    V = len(G)
    dist = [float('inf') for _ in range(V)]
    dist[s] = 0

    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, (dist[s], s))
    while Q:
        _, u = heapq.heappop(Q)

        for v, cost in G[u]:
            new_dist = dist[u] + cost
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(Q, (new_dist, v))

    return dist


def minimal_cost(n, edges, start, end):
    G = [[] for _ in range(n)]
    for u, v, cost in edges:
        G[u].append((v, cost))

    dist_to = dijkstra(G, start)
    dist_back = dijkstra(G, end)

    return dist_to[end] + dist_back[start]


graph = [(0, 1, 10), (1, 2, 5), (1, 3, 7), (2, 1, 1), (3, 0, 2)]
print(minimal_cost(4, graph, 0, 2))
