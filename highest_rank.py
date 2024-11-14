def highest_rank(arr):
    arr_reverso = sorted(arr, reverse=True)
    resultado = []
    for num in arr_reverso:
        cuenta = arr_reverso.count(num)
        resultado.append(cuenta)
        posicion = resultado.index(max(resultado))
        solucion = arr_reverso[posicion]
    return solucion
