def sort_array(source_array):
    resultado = source_array[:]
    impares_ordenados = [num for num in source_array if num % 2 != 0]
    
    impares_ordenados.sort()
    
    indice_impar = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            resultado[i] = impares_ordenados[indice_impar]
            indice_impar += 1
    
    return resultado
    
