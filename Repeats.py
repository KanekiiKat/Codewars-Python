def repeats(*arr):
    conteo = {}
    
    for numero in arr:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1

    pasumar = {num: cantidad for num, cantidad in conteo.item() if cantidad == 1}
        
    
    return pasumar
