def find_characters(matrix):
    lista = list(matrix.replace("\n", ""))
    cuenta = []
    posicion = []
    for char in lista:
        cuenta.append(lista.count(char))
    for pos, num in enumerate(cuenta):
        if num == min(cuenta) and lista[pos] not in posicion:
            posicion.append(lista[pos])
    letras = [char for char in posicion if char.isalpha()]
    numeros = [char for char in posicion if char.isdigit()]
    posicion = sorted(letras) + sorted(numeros)
    resultado = "".join(posicion)
    return resultado
