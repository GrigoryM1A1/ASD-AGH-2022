'''Sposob pierwszy O(n) z takimi jakby sumami prefiksowymi
Zał: Wszystkie prostakaty maja nieujemne wspolrzedne, kiedys moze zmienie tak, aby dzialalo na calym R^2
'''
from sys import maxsize as inf


# O(1)
def get_intersect(a, b):
    # Sprawdzam czy, oba przeciecia w ogole istnieja
    if a is None or b is None:
        return None

    if a == inf and b != inf:
        return b

    if a != inf and b == inf:
        return a
    # Jezeli oba przeciecia nie sa puste to sprawdzamy czy w ogole maja czesc wspolna
    x1, y1, x2, y2 = a
    a1, b1, a2, b2 = b

    if y1 >= b2 or b1 >= y2:
        return None

    if x2 <= a1 or a2 <= x1:
        return None

    # Obliczamy przeciecie sie danych prostakatow
    i = max(x1, a1)
    j = max(y1, b1)
    k = min(x2, a2)
    l = min(y2, b2)
    return i, j, k, l


# O(n)
def rect(T):
    n = len(T)
    A = [None for _ in range(n)]
    A[0] = inf
    A[1] = T[0]
    B = [None for _ in range(n)]
    B[n-1] = inf
    B[n-2] = T[n-1]

    for i in range(2, n):
        A[i] = get_intersect(A[i-1], T[i-1])

    for i in range(n-3, -1, -1):
        B[i] = get_intersect(B[i+1], T[i+1])

    ind = 0
    max_area = -inf
    for i in range(n):
        inter = get_intersect(A[i], B[i])
        if inter is None:
            max_area = 0
            ind = i
        else:
            area = (inter[3] - inter[1]) * (inter[2] - inter[0])
            if area > max_area:
                max_area = area
                ind = i
    return ind


Prost = [(2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]
print(rect(Prost))
# print("Potencjalne A[0]: ", inf)
# print("Potencjalne A[1]: ", get_intersect(inf, Prost[0]))
# print("Potencjalne A[2]: ", get_intersect(get_intersect(inf, Prost[0]), Prost[1]))
# print('\n')
# print("Potencjalne B[2]: ", inf)
# print("Potencjalne B[1]: ", get_intersect(inf, Prost[2]))
# print("Potencjalne B[0]: ", get_intersect(get_intersect(inf, Prost[2]), Prost[1]))
# print('\n')
# testting_so_much(Prost)
