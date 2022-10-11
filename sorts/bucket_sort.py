"""
Bucket sort
"""


def insertion_sort(L):
    n = len(L)
    for j in range(1, n):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key


def bucket_sort(A):
    # finding max val in list and calculating size of a bucket
    n = len(A)
    max_val = max(A)
    bucket_size = max_val / n

    # creating buckets
    buckets = [[] for _ in range(n)]

    # putting elements in buckets
    for i in range(n):
        j = int(A[i] / bucket_size)
        if j != n:
            buckets[j].append(A[i])
        else:
            # this only happens with the largest number
            buckets[n - 1].append(A[i])

    # sorting buckets
    for bucket in buckets:
        insertion_sort(bucket)

    # concatenating buckets
    i = 0
    for bucket in buckets:
        for j in range(len(bucket)):
            A[i] = bucket[j]
            i += 1


B = [85, 58, 31, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
print(B)
bucket_sort(B)
print(B)
