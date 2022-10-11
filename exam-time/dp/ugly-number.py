"""Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
shows the first 11 ugly numbers. By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number."""

"""
Here is a time efficient solution with O(n) extra space. The ugly-number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
     because every number can only be divided by 2, 3, 5, one way to look at the sequence is to split
     the sequence to three groups as below: 
     (1) 1×2, 2×2, 3×2, 4×2, 5×2, … 
     (2) 1×3, 2×3, 3×3, 4×3, 5×3, … 
     (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
     We can find that every subsequence is the ugly-sequence itself (1, 2, 3, 4, 5, …) multiply 2, 3, 5. 
     Then we use similar merge method as merge sort, to get every ugly number from the three subsequences. 
     Every step we choose the smallest one, and move one step after.
"""


def ugly_numbers(N):
    F = [1 for _ in range(N+1)]
    a = b = c = 1
    group_2 = 2
    group_3 = 3
    group_5 = 5

    for i in range(2, N+1):
        ith_number = min(group_2, group_3, group_5)
        F[i] = ith_number

        if ith_number == group_2:
            a += 1
            group_2 = F[a] * 2
        if ith_number == group_3:
            b += 1
            group_3 = F[b] * 3
        if ith_number == group_5:
            c += 1
            group_5 = F[c] * 5

    return F[N]


print(ugly_numbers(150))
