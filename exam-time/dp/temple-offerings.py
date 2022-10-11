"""
Consider a devotee wishing to give offerings to temples along with a mountain range.
The temples are located in a row at different heights. Each temple should receive at least one offer.
If two adjacent temples are at different altitudes, then the temple that is higher up should receive more offerings
than the one that is lower down.
If two adjacent temples are at the same height, then their offerings relative to each other do not matter.
Given the number of temples and the heights of the temples in order, find the minimum number of offerings to bring.
"""


# O(n^2)
def temple_offerings(n, Heights):
    sum_ = 0

    for i in range(n):
        left = 0
        right = 0

        for j in range(i - 1, -1, -1):
            if Heights[j] < Heights[j+1]:
                left += 1
            else:
                break

        for j in range(i + 1, n):
            if Heights[j] < Heights[j-1]:
                right += 1
            else:
                break
        sum_ += (max(left, right) + 1)

    return sum_


def lin_temple_offering(n, Heights):
    # chcemy zrobic to samo ale zeby szybciej dostawac left i right
    lefts = [-1 for _ in range(n)]
    rights = [-1 for _ in range(n)]

    lefts[0] = rights[-1] = 1

    for i in range(1, n):
        if Heights[i-1] < Heights[i]:
            lefts[i] = lefts[i-1] + 1
        else:
            lefts[i] = 1

    for i in range(n-2, -1, -1):
        if Heights[i+1] < Heights[i]:
            rights[i] = rights[i+1] + 1
        else:
            rights[i] = 1

    sum_ = 0
    for i in range(n):
        sum_ += max(lefts[i], rights[i])
    return sum_


print(temple_offerings(6, [1, 4, 3, 6, 2, 1]))
print(lin_temple_offering(6, [1, 4, 3, 6, 2, 1]))

