import mysql.connector
from mysql.connector import Error

def check_login(username, password):
    try:
        # Conecta a la base de datos MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='tu_usuario',  # Reemplaza con tu usuario de MySQL
            password='tu_contrasena',  # Reemplaza con tu contraseña de MySQL
            database='sistema_login'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Verifica las credenciales del usuario
            sql_select_query = """SELECT * FROM usuarios WHERE username = %s AND password = %s"""
            cursor.execute(sql_select_query, (username, password))
            record = cursor.fetchone()
            if record:
                print("Login exitoso")
            else:
                print("Nombre de usuario o contraseña incorrectos")
    
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    user = input("Introduce el nombre de usuario: ")
    pwd = input("Introduce la contraseña: ")
    check_login(user, pwd)
