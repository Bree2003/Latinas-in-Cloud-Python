# En este archivo crearemos la conexión a la base de datos

# Primero importamos la dependencia instalada
import mysql.connector as mysql_conn

# Creamos una función para hacer la conexión y le pasamos parámetros con los datos de configuración
def create_connection(host, user, password, database):
    # Creamos bloque try-except para que en caso de error nos lo muestre en consola
    try:
        # Creamos nuestra variable conexión
        conn = mysql_conn.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        # Creamos la variable cursor que nos permite ejecutar nuestras consultas SQL y manejar resultados
        cursor = conn.cursor()
        
        # Imprimos en la consola un mensaje de éxito
        print("Se ha conectado exitosamente a la base de datos")
        
        # Retornamos la conexión y el cursor para usar fuera de este contexto (en el archivo tasks.py)
        return conn, cursor
    except mysql_conn.Error as err:
        # Imprimimos en la consola el error
        print(f"Error al conectar a la base de datos: {err}")
        # Le indicamos que finalice porque hubo un error
        exit(1)