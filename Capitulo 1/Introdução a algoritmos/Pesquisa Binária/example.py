from math import *

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1

    return None

minha_lista = [1, 3, 5, 7, 9]

indice_resultado1 = pesquisa_binaria(minha_lista, 3)

indice_resultado2 = pesquisa_binaria(minha_lista, -1) ## TODO resolver

print(1)
print(2)