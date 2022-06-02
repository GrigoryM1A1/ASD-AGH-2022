def load_the_truck(T, l):
    T.sort()
    count = 0
    for pack in T:
        if l >= pack:
            count += 1
            l -= pack
        else:
            return count
