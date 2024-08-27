#* repaso python 

num=int(input("ingresa un numero:  "))

if num % 2 != 0:
    print(f"El numero, {num} es impar  ")
    print(f"La raiz cuadrada de,  {num} es:  {num**0.5}")
 

if num % 2 == 0:
    print(f"El numero, {num} es par  ")
    print(f"La raiz cuadrada de,  {num} es:  {num**0.5}")
    

# Step 1: Definir una función que toma dos parámetros a y b y retorna el resultado c
def suma(a, b):
    return a + b
   
# Step 2: Ejecutar la función con los valores 5.2 y 7.3 para obtener el resultado
resultado = suma(5325.2, 7124.3)
   
# Step 3: Mostrar el resultado en pantalla
print(f"El resultado de 5.2 + 7.3 es: {resultado}")

# Step 4: Importar el módulo 'unittest', que es un framework de Python para realizar pruebas unitarias
import unittest

# Step 5: Definir una clase que hereda de unittest.TestCase
# Esta clase contendrá los métodos básicos y los resultados para la función suma
class TestSuma(unittest.TestCase):

    # Step 6: Definir un método que realiza una prueba unitaria
    def test_suma_positivos(self):
        # Step 7: Establecer los valores de entrada y esperado
        a = 5325.2
        b = 7124.3
        expected_result = 12449.5

        # Step 8: Ejecutar la función y obtener el resultado
        result = suma(a, b)

        # Step 9: Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

    def test_suma_negativos(self):
        # Step 10: Establecer los valores de entrada y esperado
        a = -500000.2
        b = -700000.3
        expected_result = -1200000.5
    
        # Step 11: Ejecutar la función y obtener el resultado
        result = suma(a, b)
    
        # Step 12: Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

    def test_suma_mixta(self):
        # Step 13: Establecer los valores de entrada y esperado
        a = 500000
        b = -700000
        expected_result = -200000
    
        # Step 14: Ejecutar la función y obtener el resultado
        result = suma(a, b)
    
        # Step 15: Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

    def test_suma_cero(self):
        # Step 16: Establecer los valores de entrada y esperado
        a = 0.0
        b = 0.0
        expected_result = 0.0
    
        # Step 17: Ejecutar la función y obtener el resultado
        result = suma(a, b)
    
        # Step 18: Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

# Step 19: Ejecutar las pruebas unitarias
#* ejecutamos el script para ejecutar todas las pruebas unitarias usando la siguiente funcion
if __name__ == '__main__':
    unittest.main()







# investigar como se calcula voltaje en la ley de ohm