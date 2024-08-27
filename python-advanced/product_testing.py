# Librerías a utilizar para las pruebas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from faker import Faker

# Configuración de Faker para generar datos aleatorios de prueba
faker = Faker()

# Definir la clase para insertar los datos aleatorios
class TestInsertarDatos(unittest.TestCase):

    def setUp(self):
        # Establecer opciones de Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Opcional: ejecuta el navegador en modo headless (sin interfaz gráfica)
        self.drive=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        # Ruta al ejecutable de ChromeDriver

    # Método que contiene las pruebas de inserción de datos
    def test_insert_data(self):
        drive = self.drive
        # Navegar al formulario web
        drive.get("http://localhost/python/final/HTML/productos.html")
        
        for _ in range(200):
            # Generar los datos aleatorios de prueba para cada campo del formulario
            nombre = faker.word() 
            cantidad = str(faker.random_number(digits=2))  # Por ejemplo, para generar números con hasta 2 dígitos
            valorventa = faker.random_number(digits=7)  # Ajusta los dígitos según el rango deseado
            proveedor = faker.company()
            
            
            # Completar los campos del formulario
            drive.find_element(By.ID, "nombre").send_keys(nombre)
            drive.find_element(By.ID, "cantidad").send_keys(cantidad)
            drive.find_element(By.ID, "valorventa").send_keys(valorventa)
            drive.find_element(By.ID, "proveedor").send_keys(proveedor)
   
            
            # Enviar el formulario con los atributos
            drive.find_element(By.XPATH, "//button[@type='submit']").click()
            
            # Esperar a que se envíe y procese el formulario y vuelva a la página inicial para repetir el proceso
            time.sleep(3)
            drive.get("http://localhost/python/final/HTML/productos.html")
            time.sleep(1)

    def tearDown(self):
        # Método ejecutable después de cada prueba
        # Cerrar el navegador
        self.drive.quit()

# Ejecutamos el script para ejecutar todas las pruebas unitarias usando la siguiente función
if __name__ == '__main__':
    unittest.main()
