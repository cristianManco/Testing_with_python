# La Ley de Ohm es una relación fundamental en la electricidad que establece la relación entre el voltaje, la corriente y la resistencia en un circuito eléctrico. La fórmula general de la Ley de Ohm es:

# V = I * R

# donde:

# V es el voltaje (en voltios, V),

# I es la corriente (en amperios, A),

# R es la resistencia (en ohmios, Ω).

#* Cómo se calcula el voltaje
# Para calcular el voltaje utilizando la Ley de Ohm, necesitas conocer la corriente y la resistencia en el circuito. El voltaje se calcula multiplicando la corriente por la resistencia.


# Función para calcular el voltaje usando la Ley de Ohm
def calcular_voltaje(corriente, resistencia):
    return corriente * resistencia

# Valores de ejemplo
corriente = 2  # en amperios
resistencia = 5  # en ohmios

# Calcular el voltaje
voltaje = calcular_voltaje(corriente, resistencia)

# Mostrar el resultado
print(f"El voltaje en el circuito es: {voltaje} V")


# Esta función toma dos parámetros: corriente y resistencia.
# Retorna el resultado de multiplicar corriente por resistencia, que es el voltaje.
# Valores de ejemplo:





import unittest

class TestCalcularVoltaje(unittest.TestCase):

    def test_voltaje_positivos(self):
        # Valores de entrada: corriente = 2 A, resistencia = 5 Ω
        corriente = 2
        resistencia = 5
        expected_result = 10  # Voltaje = 2 A * 5 Ω
        
        # Ejecutar la función y obtener el resultado
        result = calcular_voltaje(corriente, resistencia)
        
        # Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

    def test_voltaje_negativos(self):
        # Valores de entrada: corriente = -2 A, resistencia = -5 Ω
        corriente = -2
        resistencia = -5
        expected_result = 10  # Voltaje = -2 A * -5 Ω
        
        # Ejecutar la función y obtener el resultado
        result = calcular_voltaje(corriente, resistencia)
        
        # Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

    def test_voltaje_mixto(self):
        # Valores de entrada: corriente = 3 A, resistencia = -4 Ω
        corriente = 3
        resistencia = -4
        expected_result = -12  # Voltaje = 3 A * -4 Ω
        
        # Ejecutar la función y obtener el resultado
        result = calcular_voltaje(corriente, resistencia)
        
        # Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

    def test_voltaje_cero(self):
        # Valores de entrada: corriente = 0 A, resistencia = 5 Ω
        corriente = 0
        resistencia = 5
        expected_result = 0  # Voltaje = 0 A * 5 Ω
        
        # Ejecutar la función y obtener el resultado
        result = calcular_voltaje(corriente, resistencia)
        
        # Comparar el resultado con el esperado
        self.assertEqual(result, expected_result)

# Ejecutar las pruebas unitarias
if __name__ == '__main__':
    unittest.main()


