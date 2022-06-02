# O(n^2)
def depth_ale_wolno(L):
    n = len(L)
    max_c_tab = [0] * n
    for i in range(n):
        for j in range(n):
            if j != i:
                if L[i][0] <= L[j][0] and L[i][1] >= L[j][1]:
                    max_c_tab[i] += 1
    max_c = max_c_tab[0]
    for i in range(1, n):
        if max_c_tab[i] > max_c:
            max_c = max_c_tab[i]
    return max_c
