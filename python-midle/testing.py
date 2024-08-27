import mysql.connector
from mysql.connector import Error

def insert_user(username, password):
    try:
        # Conecta a la base de datos MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='tu_usuario',  # Reemplaza con el usuario de MySQL
            password='tu_contrasena',  # Reemplaza con tu contraseña de MySQL
            database='sistema_login'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Inserta un nuevo usuario en la tabla
            sql_insert_query = """INSERT INTO usuarios (username, password) VALUES (%s, %s)"""
            record = (username, password)
            cursor.execute(sql_insert_query, record)
            connection.commit()  # Guarda los cambios
            print("Usuario insertado con éxito")
    
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
    insert_user(user, pwd)
