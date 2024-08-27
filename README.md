
---

# Python Testing Repository

## Introducción

Este repositorio contiene una serie de pruebas unitarias y de integración en Python, que van desde ejemplos simples hasta casos más avanzados. El propósito de este repositorio es proporcionar una base sólida para asegurar la fiabilidad y corrección de las aplicaciones en Python mediante el uso de varias herramientas de pruebas ampliamente reconocidas en la comunidad.

## Librerías Utilizadas

### 1. **unittest**
   - **Descripción:** `unittest` es el marco de pruebas estándar incluido en la biblioteca estándar de Python. Permite crear pruebas automatizadas para asegurar que las funciones y módulos de tu aplicación funcionan como se espera.
   - **Documentación Oficial:** [unittest Documentation](https://docs.python.org/3/library/unittest.html)

### 2. **Selenium**
   - **Descripción:** Selenium es una herramienta de automatización de navegadores que permite realizar pruebas funcionales en aplicaciones web. Con Selenium, puedes interactuar con un navegador como si fueras un usuario real, lo que permite pruebas end-to-end robustas.
   - **Documentación Oficial:** [Selenium Documentation](https://www.selenium.dev/documentation/)

### 3. **Faker**
   - **Descripción:** Faker es una biblioteca para generar datos falsos. Es extremadamente útil para pruebas automatizadas donde se requiere un gran volumen de datos dinámicos y variados.
   - **Documentación Oficial:** [Faker Documentation](https://faker.readthedocs.io/en/master/)

### 4. **webdriver_manager**
   - **Descripción:** `webdriver_manager` se encarga de la instalación y gestión automática de los binarios de WebDriver (como ChromeDriver) para Selenium, eliminando la necesidad de instalar manualmente el controlador del navegador.
   - **Documentación Oficial:** [webdriver_manager Documentation](https://pypi.org/project/webdriver-manager/)

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **`tests/`:** Contiene todos los archivos de prueba, organizados en diferentes módulos.
- **`requirements.txt`:** Archivo de dependencias que incluye todas las bibliotecas necesarias para ejecutar las pruebas.
- **`README.md`:** Documentación del repositorio (este archivo).
  
## Instalación

Para empezar a usar este repositorio, sigue estos pasos:

1. Clona el repositorio a tu máquina local:
    ```bash
    git clone https://github.com/cristianManco/Testing_with_python/
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd Testing_with_python
    ```
3. Instala las dependencias requeridas:
    ```bash
    pip install -r requirements.txt
    ```

## Uso del Repositorio

Una vez que las dependencias estén instaladas, puedes ejecutar las pruebas de la siguiente manera:

1. **Ejecución de todas las pruebas:**
    ```bash
    python -m unittest discover
    ```

2. **Ejecución de una prueba específica:**
    ```bash
    python -m unittest tests.test_module_name
    ```

3. **Ejecución de pruebas en modo verboso:**
    ```bash
    python -m unittest discover -v
    ```

## Ejemplos de Pruebas

Este repositorio contiene una variedad de pruebas que incluyen:

- **Pruebas de lógica básica:** Ejemplos sencillos que prueban funciones matemáticas y lógicas.
- **Pruebas de integración:** Pruebas que verifican la interacción entre varios componentes del sistema.
- **Pruebas de automatización web:** Usando Selenium para interactuar y validar el comportamiento en aplicaciones web.


## Recursos Adicionales

Para aquellos interesados en seguir practicando con ejercicios de lógica de programación, te recomiendo visitar el siguiente enlace, donde podrás encontrar una variedad de ejercicios de diferentes niveles de dificultad:

[Recursos de Ejercicios de Lógica](https://rojastobias.blogspot.com/p/algoritmos-i_20.html)

## Contribuciones

Si deseas contribuir a este repositorio, siéntete libre de hacer un fork del proyecto y enviar un pull request con tus mejoras. Cualquier tipo de colaboración es bienvenida.

---
