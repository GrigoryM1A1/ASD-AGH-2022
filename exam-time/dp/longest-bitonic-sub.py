"""
Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic if it is first
increasing, then decreasing. Write a function that takes an array as argument and returns the length of
the longest bitonic subsequence.
A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. Similarly, decreasing
order sequence is considered Bitonic with the increasing part as empty.
"""


# obliczamy longest increasing subsequence
# obliczamy longest decreasing subsequence
# bierzemy maksa z lis[i] + lds[j]
def lbs(A):
    n = len(A)
    lis = [1 for _ in range(n)]
    lds = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if A[i] > A[j] and lds[j] + 1 > lds[i]:
                lds[i] = lds[j] + 1
    print(lis)
    print(lds)
    max_bit = 0
    for i in range(n):
        q = lis[i] + lds[i] - 1
        if q > max_bit:
            max_bit = q
    return max_bit


print(lbs([1, 11, 2, 10, 4, 5, 2, 1]))
print()
print(lbs([12, 11, 40, 5, 3, 1]))
print()
print(lbs([80, 60, 30, 40, 20, 10]))
