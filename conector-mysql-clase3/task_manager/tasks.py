# Importamos la dependencia
import mysql.connector

# Creamos una clase que nos permite añadir, completar, obtener y eliminar tareas
class TaskManager: # Las clases siempre empiezan en mayúscula
    
    # Creamos el constructor que nos permite inicializar la clase junto a sus atributos (propiedades)
    # En este caso le estamos pasando la conexión y el cursor para la comunicación con la base de datos
    def __init__(self, conn, cursor):
        # El parámetro self hace referencia a la instancia actual
        self.conn = conn
        self.cursor = cursor
    
    # Creamos una función para añadir una tarea y le pasamos como parámetro el título
    def add_task(self, title):
        
        # Creamos una variable indicando la sentencia SQL
        sql = "INSERT INTO tasks (title) VALUES (%s)"
        
        try:
            # Ejecutamos la consulta
            self.cursor.execute(sql, (title,))
            
            # Guardamos en la base de datos
            self.conn.commit()
            
            # Imprimos en la consola
            print(f"Tarea '{title}' agregada")
        
        except mysql.connector.Error as err:
            
            print(f"Error al agregar la tarea: {err}")
    
    # Creamos una función para obtener todas nuestras tareas en la base de datos
    def get_tasks(self):
        
        try:
            # Ejecutamos nuestra query
            self.cursor.execute("SELECT * FROM tasks")
            
            # Nos traemos los resultados si es que hay
            tasks = self.cursor.fetchall()
            
            # Devolvemos las tareas
            return tasks
        
        except mysql.connector.Error as err:
            
            print(f"Error al obtener las tareas: {err}")
            
            # Retornamos una lista vacía
            return []
    
    # Creamos una función para completar las tareas pasándole el id de la task
    def complete_task(self, task_id):
        
        # Sentencia SQL
        sql = "UPDATE tasks SET completed = TRUE WHERE id = %s"
        
        try:
            
            # Ejecutamos la consulta query
            self.cursor.execute(sql, (task_id,))
            
            # La guardamos en la base de datos
            self.conn.commit()
            
            print(f"Tarea con ID {task_id} marcada como completada")
        
        except mysql.connector.Error as err:
            
            print(f"Error al completar la tarea: {err}")
    
    # Creamos una función para eliminar una tarea en donde le pasamos el parámetro id
    def delete_task(self, task_id):
        
        # Query
        sql = "DELETE FORM tasks WHERE id = %s"
        
        try:
            
            # Ejecutamos el comando
            self.cursor.execute(sql, (task_id,))
            
            # Lo guardamos en la base de datos
            self.conn.commit()
            
            print(f'Tarea con ID {task_id} eliminada')
        
        except mysql.connector.Error as err:
            
            print(f"Error al eliminar la tarea: {err}")
    
    # Creamos método para cerrar el cursor y la conexión a la base de datos
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Conexión a la base de datos cerrada")