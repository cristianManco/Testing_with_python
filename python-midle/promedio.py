# Función para calcular el promedio de tres notas
def prom_notes(note1, note2, note3):
    if note1 is None or note2 is None or note3 is None:
        raise ValueError("Las notas no pueden ser campos vacíos")
    return (note1 + note2 + note3) / 3

print(prom_notes(3.2, 4.5, 5.6))

# Función para sumar los valores de una lista y calcular el promedio
def sum_and_average(notes):
    if not notes:
        raise ValueError("La lista de notas no puede estar vacía")
    return sum(notes) / len(notes)

print(sum_and_average([6,2,3,4,5,-6]))


import unittest

class TestNotes(unittest.TestCase):

    # Pruebas para la función prom_notes
    def test_promedio_positivos(self):
        self.assertAlmostEqual(prom_notes(5, 4, 5), 4.666666666666667, places=7)
        self.assertAlmostEqual(prom_notes(5, 5, 5), 5.0, places=7)

    def test_promedio_decimales_grandes(self):
        self.assertAlmostEqual(prom_notes(123456789.5, 987654321.5, 111111111.5), 407407407.5, places=1)

    def test_promedio_decimales_pequenos(self):
        self.assertAlmostEqual(prom_notes(0.000001, 0.000002, 0.000003), 0.000002, places=6)

    def test_promedio_valores_null(self):
        with self.assertRaises(ValueError):
            prom_notes(None, 5, 5)
        with self.assertRaises(ValueError):
            prom_notes(5, None, 5)
        with self.assertRaises(ValueError):
            prom_notes(5, 5, None)
        with self.assertRaises(ValueError):
            prom_notes(None, None, None)

    # Pruebas para la función sum_and_average
    def test_suma_positivos(self):
        self.assertAlmostEqual(sum_and_average([5, 4, 5]), 4.666666666666667, places=7)
        self.assertAlmostEqual(sum_and_average([5, 5, 5]), 5.0, places=7)

    def test_suma_decimales_grandes(self):
        self.assertAlmostEqual(sum_and_average([123456789.5, 987654321.5, 111111111.5]), 407407407.5, places=1)

    def test_suma_decimales_pequenos(self):
        self.assertAlmostEqual(sum_and_average([0.000001, 0.000002, 0.000003]), 0.000002, places=6)

    def test_suma_valores_null(self):
        with self.assertRaises(ValueError):
            sum_and_average([])



# Ejecutar las pruebas unitarias
if __name__ == '__main__':
    unittest.main()

