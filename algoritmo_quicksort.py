#1.Caso base
#2.Elección del pivote
#3.Partición
#4.Recursión
#5.Concatenación

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]#Elementos mayores
        greater = [x for x in arr[1:] if x > pivot]#Elementos menores
        return quicksort(less) + [pivot] + quicksort(greater)

# Ejemplo 
mi_lista = [3, 6, 8, 10, 1, 2, 1]
resultado = quicksort(mi_lista)
print("Lista original:", mi_lista)
print("Lista ordenada:", resultado)
