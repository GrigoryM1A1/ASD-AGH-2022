"""
Check if there is hamiltonian-path in graph
"""


def gen_all_perm(n):
    all_perms = []
    perm = [0 for i in range(n)]
    for i in range(1, n):
        perm[i] = i
    all_perms.append(tuple(perm))
    all_perms[0] = list(all_perms[0])

    i = n - 2
    while i >= 0 and perm[i] > perm[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while perm[j] < perm[i]:
            j -= 1
        perm[i], perm[j] = perm[j], perm[i]
        k = i + 1
        l = n - 1
        while l > k:
            perm[k], perm[l] = perm[l], perm[k]
            k += 1
            l -= 1

    while i >= 0:
        all_perms.append(tuple(perm))
        all_perms[len(all_perms) - 1] = list(all_perms[len(all_perms) - 1])
        i = n - 2
        while i >= 0 and perm[i] > perm[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while perm[j] < perm[i]:
                j -= 1
            perm[i], perm[j] = perm[j], perm[i]
            k = i + 1
            l = n - 1
            while l > k:
                perm[k], perm[l] = perm[l], perm[k]
                k += 1
                l -= 1

    return all_perms


def is_hamiltonian_path(G):
    V = len(G)
    Possible_paths = gen_all_perm(V)

    exist = False
    for path in Possible_paths:
        for v in range(V - 1):
            if path[v + 1] in G[path[v]]:
                exist = True
            else:
                exist = False
                break
        if exist:
            return True

    return False


Graph1 = [[1, 2],
          [3, 0],
          [0, 3],
          [1, 2]]
print(is_hamiltonian_path(Graph1))

Graph2 = [[1],
          [3, 0, 2],
          [1],
          [1]]
print(is_hamiltonian_path(Graph2))
