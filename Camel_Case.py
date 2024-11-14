def to_camel_case(text):
    if not text:
        return ""
    
    nueva_cadena = ""
    convertirmayus = True

    for caracter in text:
        if convertirmayus:
            nueva_cadena += caracter.upper()
            convertirmayus = False
        elif caracter in "_-":
            convertirmayus = True
        else:
            nueva_cadena += caracter

    if text[0].islower():
        nueva_cadena = nueva_cadena[0].lower() + nueva_cadena[1:]
    
    return nueva_cadena.replace("-", "").replace("_", "")
