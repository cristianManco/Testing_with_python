# Función para convertir texto a binario
def texto_a_binario(texto):
    # Convertir cada carácter en su representación binaria y unirlos en una sola cadena
    binario = ''.join(format(ord(caracter), '08b') for caracter in texto)
    return binario

# Función para convertir binario a texto
def binario_a_texto(binario):
    # Dividir la cadena binaria en bloques de 8 bits y convertir cada bloque en un carácter
    caracteres = [chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8)]
    return ''.join(caracteres)

# Ejemplo de uso
texto = "El suave"
print("Texto original:", texto)

# Convertir texto a binario
binario = texto_a_binario(texto)
print("Texto en binario:", binario)

# Convertir binario de vuelta a texto
texto_convertido = binario_a_texto(binario)
print("Texto convertido de binario:", texto_convertido)
