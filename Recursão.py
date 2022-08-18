#pesquisa sequencial recursiva
def pesquisa_sequencial(array, key):
  def pesquisa_sequecial_recursao(array, key, index):
    if len(array) == index:
      return - 1
    if array[index] == key:
      return index
    return pesquisa_sequecial_recursao(array, key, index + 1)
  return pesquisa_sequecial_recursao(array, key, 0)

#pesquisa binaria recursiva
def pesquisa_binaria(array, key):
  def pesquisa_binaria_recursiva(array, key, inf, sup):
    #caso base
    if inf > sup:
      return -1
      
    middle = (inf + sup) // 2 
    
    if key == array[middle]:
      return middle
    elif key < array[middle]:
      return pesquisa_binaria_recursiva(array, key, inf, middle - 1)
    else:
      return pesquisa_binaria_recursiva(array, key, middle + 1, sup)pesquisa_binaria_recursiva(array, key, 0, len(array) - 1)

if __name__ == "__main__":
  array = [1,2,3,4,5,6,7,8,9,10]
  print(pesquisa_sequencial(array, 6))
  print(pesquisa_binaria(array, 9))
  return 
  
