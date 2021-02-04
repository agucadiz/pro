"""
Pre:    True
        ord_sel(e: list) -> list
Post:   ord_sel(e) = una lista igual que e, pero con los valores ordenados
"""

pato = [5, 7, 1, 9, 0, 4, 6, 2, 3, 8]

ord_sel = lambda l: [] if l == () else \
                    l[0], l[1] = l[1], l[0] if l[0] > l[1] else \
                        ord_sel(l[1:])

lista = [5, 12]

listilla = [5, 3, 7, 8, 1, 9, 2, 0, 6, 4]


nueva[]
