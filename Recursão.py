import numpy as np

def pesquisa_sequencial(array: np.array, key: int) -> int:
    def pesquisa_sequecial_recursao(array: np.array, key: int, index: int) -> int:
        # caso base
        if len(array) == index:
            return - 1
        if array[index] == key:
            return index
        return pesquisa_sequecial_recursao(array, key, index + 1)
    return pesquisa_sequecial_recursao(array, key, 0)


def pesquisa_binaria(array: np.array, key: int) -> int:
    def pesquisa_binaria_recursiva(array: np.array, key: int, inf: int, sup: int) -> int:
        # caso base
        if inf > sup:
            return -1
        middle = (inf + sup) // 2
        if key == array[middle]:
            return middle
        elif key < array[middle]:
            return pesquisa_binaria_recursiva(array, key, inf, middle - 1)
        else:
            return pesquisa_binaria_recursiva(array, key, middle + 1, sup)
    return pesquisa_binaria_recursiva(array, key, 0, len(array) - 1)


def soma_inteiros_ate_n(n: int) -> int:
    # caso base
    if n <= 1:
        return n
    return n + soma_inteiros_ate_n(n - 1)


def mdc(x: int, y: int) -> int:
    # função recursiva
    def mdc(x: int, y: int) -> int:
        if x >= y and x % y == 0:  # caso base
            return y
        return mdc(y, x % y)  # caso recursivo
    # chamada da função recursiva
    if x < y:
        return mdc(y, x)
    return mdc(x, y)

def soma_elementos_array(array: np.array) -> int:
  def soma_elementos_array_recursivo(array: np.array, valor: int, index: int) -> int:
    if (index > len(array) - 1): #caso base
      return valor
    return soma_elementos_array_recursivo(array, valor + array[index], index + 1)
  return soma_elementos_array_recursivo(array, 0, 0)

def soma_dos_algarismos(number: int) -> int:
    if number < 0:
        raise ValueError('Número inserido não pode ser negativo')
    def soma_dos_algarismos_recursivo(array, soma, index):
        if index > len(array) -1: #caso base
            return soma
        return soma_dos_algarismos_recursivo(array, soma + int(array[index]), index + 1)
    return soma_dos_algarismos_recursivo(list(str(number)), 0, 0)

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(pesquisa_sequencial(array, 6))
    print(pesquisa_binaria(array, 6))
    print(soma_inteiros_ate_n(15))
    print(mdc(20, 24))
    print(soma_elementos_array(array))
    try:
        print(soma_dos_algarismos(-5248))
    except:
        print("Não podemos trabalhar com números negativos")
        
