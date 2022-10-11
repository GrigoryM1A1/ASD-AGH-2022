"""
Carol i Max przewoza chemikalia jeden z A do B i drugi z B do A. Nie mogą się zbliżyć do siebie na pewna odleglosc
i nie moga jechac ta sama krawedzia w tej samej jednostce czasu.


1. Floyd-Warshall
2. Budowa grafu - rozdzielamy wierzcholki:
    - pary wierzcholkow spelniajace zalozenie odleglosci
    - krawedzie tylko jezeli w parach miedzy dwoma wierzcholkami mozna przejsc bezposredndio
    - nie ma krawedzi (a,b) - (b,a)
"""