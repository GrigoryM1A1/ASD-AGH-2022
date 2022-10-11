"""
Link to the problem
https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/palindrome-change-3e337ebf/
"""


def palindromic_changes(Word, Changes_cost):
    # a...z == 97...122
    # 0 = ord('a') - 97
    # 25 = ord('z') - 97
    V = 26
    Graph_changes = [[float('inf') for _ in range(V)] for _ in range(V)]
    Positions_to_change = []
    for fr, to, cost in Changes_cost:
        u = ord(fr) - 97
        v = ord(to) - 97
        Graph_changes[u][v] = cost

    for i in range(V):
        Graph_changes[i][i] = 0

    n = len(Word)
    for i in range(n // 2 + 1):
        if i < n-i-1 and Word[i] != Word[n-i-1]:
            Positions_to_change.append((Word[i], Word[n-i-1]))

    for k in range(V):
        for u in range(V):
            for v in range(V):
                Graph_changes[u][v] = min(Graph_changes[u][v], Graph_changes[u][k] + Graph_changes[k][v])

    min_cost = 0
    for char1, char2 in Positions_to_change:
        u = ord(char1) - 97
        v = ord(char2) - 97
        min_ = float('inf')
        for i in range(V):
            min_ = min(min_, Graph_changes[u][i] + Graph_changes[v][i])
        min_cost += min_
    return min_cost


S = 'abcd'
Changes = [('a', 'b', 2), ('c', 'b', 2), ('d', 'b', 1)]
print(palindromic_changes(S, Changes))
