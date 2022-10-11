def leader(T):
    n = len(T)
    l = T[0]
    c = 1
    for i in range(1, n):
        if c > 0:
            if l == T[i]:
                c += 1
            else:
                c -= 1
                if c == 0:
                    l = T[i]
    leadership = 0
    for i in T:
        if l == i:
            leadership += 1

    if leadership >= n // 2 + 1:
        print(l, "jest liderem ciagu!")
        return True
    else:
        print("Brak lidera ciagu!")
        return False


T = [2, 1, 1, 3, 1]
leader(T)
T = [1, 2, 1, 3, 4]
leader(T)
T = [3, 3, 3, 5, 2]
leader(T)
