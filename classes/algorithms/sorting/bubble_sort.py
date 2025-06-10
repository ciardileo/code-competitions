"""
bubble sort
itere o array e para cada elemento, troque com o adjascente caso este for menor que o atual (no caso de ordem crescente)
"""

def bubble_sort(array):
    
  # loop through each element of array
  for i in range(len(array)):
    swapped = False
    
    # loop to compare array elements
    for j in range(len(array) - 1 - i):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:
        array[j], array[j+1] = array[j+1], array[j]

        swapped = True
        
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

lista = [2, 1, 23, 555, 3, 56, 12]
bubble_sort(lista)
print(lista)
