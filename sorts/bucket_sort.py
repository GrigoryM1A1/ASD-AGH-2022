'''
Bucket sort
'''


def bucket_sort(A):
    def insertion_sort(L):
        n = len(L)
        for j in range(1, n):
            key = L[j]
            i = j - 1
            while i >= 0 and L[i] > key:
                L[i + 1] = L[i]
                i -= 1
            L[i + 1] = key

    n = len(A)
    Buckets = [[] for _ in range(n)]
    a = min(A)
    b = max(A)
    for x in A:
        ind = int((x - a) / (b - a) * (n - 1))
        Buckets[ind].append(x)

    for b in Buckets:
        insertion_sort(b)

    i = k = 0
    while i < n:
        j = 0
        if len(Buckets[k]) == 0:
            k += 1
        else:
            while j < len(Buckets[k]):
                A[i] = Buckets[k][j]
                i += 1
                j += 1
            k += 1


# def bucket_sort(A):
#     def insertion_sort(A):
#         for j in range(1, len(A)):
#             key = A[j]
#             i = j-1
#             while i >= 0 and A[i] > key:
#                 A[i+1] = A[i]
#                 i -= 1
#             A[i+1] = key
#
#     n = len(A)
#     B = [[] for _ in range(n+1)]
#     minimal = min(A)
#     size = (max(A) - minimal)/n
#
#     for i in A:
#         bucket_index = int((i - minimal)//size)
#         B[bucket_index].append(i)
#
#     curr_index = 0
#     for x in B:
#         n = len(x)
#         if n != 0:
#             insertion_sort(x)
#             for i in range(n):
#                 A[curr_index] = x[i]
#                 curr_index += 1


B = [85, 58, 31, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
print(B)
bucket_sort(B)
print(B)
