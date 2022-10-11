"""
Robot porusza sie po dwuwymiarowym labiryncie i ma dotrzec z pozycji A = (xa, ya) na
pozycje B = (xb, yb). Robot może wykonac nastepujace ruchy:
1) ruch do przodu na kolejne pole
2) obrot o 90 stopni zgodnie z ruchem wskazowek zegara
3) obrot o 90 stopni przeciwnie do ruchu wskazowek zegara

Obrot zajmuje robotowi 45s. W trakcie ruchu do przedu robot rozpedza sie i pokonanie pierwszego
pola zajmuje 60s, pokonanie drugiego pola 40s, a kolejnych po 30s na pole. Wykonanie obrotu powoduje, ze robot
ponownie musi sie rozpedzic.

Prosze zaimplementowac funkcje, ktora oblicza ile minimalnie sekund potrzebuje na dotarcie z punktu A do punktu B
lub None jesli nie jest to mozliwe.

Labirynt:
Reprezentowany przez tablice w wierszy, z ktorych kazdy jest napisem skladajacym sie z k kolumn. Pustny znak
oznacza pole po ktorym robot moze sie poruszac, a znak 'X' oznacza sciane. Labirynt zawsze otoczony jest
scianami i nie da sie opuscic planszy.

Pozycja robota:
Poczatkowo robot znajduje sie na pozycji A = (xa, ya) i jest obrocony w prawo (tj. znajduje sie w wierszu ya
i kolumnie xa, skierowany w strone rosnacych numerow kolumn).


Pomysl:
1) Budowa fajnego grafu z pomnozonymi wierzcholkami
- mnozenie wierzcholkow - 4 opcje (obrot lewo, oborot prawo, predkosc, wejscie)
                        - 4 opcje (<, >, ^, v)
                        razem 16 opcji

v -> (orientacja, akcja)

2) Dijkstra
"""


def robot(L, A, B):
    return 0


Lab = ["XXXXXXXXXX",
       "X X      X",
       "X XXXXXX X",
       "x        X",
       "xxxxxxxxxx"]
Start = (1, 1)
Finish = (8, 3)
