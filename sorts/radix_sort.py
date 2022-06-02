A = ['kra', 'art', 'kot', 'kit', 'ati', 'kil']
B = ['ala', 'alz', 'kos', 'sok', 'mop', 'tok', 'tik', 'aaa', 'aab', 'aba']


def radix_sort(A):
    def num(ch):
        return ord(ch) - 97

    def counting_sort(A, index):  # k = 26
        n = len(A)
        C = [0] * 26
        B = [0] * n
        for x in A:
            C[num(x[index])] += 1
        for i in range(1, 26):
            C[i] = C[i] + C[i - 1]
        for i in range(n - 1, -1, -1):
            B[C[num(A[i][index])] - 1] = A[i]
            C[num(A[i][index])] -= 1
        for i in range(n):
            A[i] = B[i]

    n = len(A[0])
    for i in range(n - 1, -1, -1):
        counting_sort(A, i)
