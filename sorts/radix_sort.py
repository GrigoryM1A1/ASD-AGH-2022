# Radix but all words have the same length, all words hve all small letters
def num(ch):
    return ord(ch) - 97


def counting_sort(A, ind):
    n = len(A)
    C = [0 for _ in range(26)]
    B = [0 for _ in range(26)]

    for x in A:
        C[num(x[ind])] += 1

    for i in range(1, 26):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[num(A[i][ind])] - 1] = A[i]
        C[num(A[i][ind])] -= 1

    for i in range(n):
        A[i] = B[i]


def radix_same_sizes(A):
    n = len(A[0])
    for i in range(n - 1, -1, -1):
        counting_sort(A, i)


# Radix but words can have different lengths and all letters in a word are small
def mod_count_sort(A, ind):
    n = len(A)
    C = [0 for _ in range(26)]
    B = [0 for _ in range(26)]

    for x in A:
        if len(x) - 1 >= ind:
            C[num(x[ind])] += 1
        else:
            C[0] += 1

    for i in range(1, 26):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        if len(A[i]) - 1 >= ind:
            B[C[num(A[i][ind])] - 1] = A[i]
            C[num(A[i][ind])] -= 1
        else:
            B[C[0] - 1] = A[i]
            C[0] -= 1

    for i in range(n):
        A[i] = B[i]


def radix_diff_sizes(A):
    n = len(A[0])
    max_len = n
    for i in range(n):
        if len(A[i]) > max_len:
            max_len = len(A[i])

    for i in range(max_len, -1, -1):
        mod_count_sort(A, i)


Arr1 = ['ala', 'alz', 'kos', 'sok', 'mop', 'tok', 'tik', 'aaa', 'aab', 'aba']
Arr2 = ['ala', 'alz', 'kofgfgfs', 'sogk', 'mofap', 'tok', 'tik', 'agaa', 'agab', 'aba']
print(Arr1)
radix_same_sizes(Arr1)
print(Arr1)
print()
print(Arr2)
radix_diff_sizes(Arr2)
print(Arr2)


