"""Super ugly numbers are positive numbers whose all prime factors are in the given prime list. Given a number n,
the task is to find the nth Super Ugly number.
It may be assumed that a given set of primes is sorted. Also, the first Super Ugly number is 1 by convention."""


def super_ugly(n, primes):
    m = len(primes)
    groups = [primes[i] for i in range(m)]
    inds = [1 for _ in range(m)]

    F = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        ith_number = min(groups)
        F[i] = ith_number

        for j in range(m):
            if ith_number == groups[j]:
                inds[j] += 1
                groups[j] = F[inds[j]] * primes[j]
    return F[n]


print(super_ugly(5, [2, 5]))
print(super_ugly(9, [3, 5, 7, 11, 13]))

