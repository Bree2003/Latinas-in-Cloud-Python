# Importamos de nuestro paquete todo los módulos que estaremos ocupando
from task_manager import DB_CONFIG, create_connection, TaskManager

# Crearemos un programa con un menú en donde le pregunte al usuario qué quiere hacer
def mostrar_menu():
    print("\nOpciones:")
    print("1. Crear una tarea")
    print("2. Ver todas las tareas")
    print("3. Completar una tarea")
    print("4. Eliminar una tarea")
    print("5. Salir")

# Nuestra función principal
def main():
    
    # Creamos conexión a la base de datos, con los ** estamos indicando que se pasen cada parámetro de nuestro diccionario a los que pide
    conn, cursor = create_connection(**DB_CONFIG)
    
    # Creamos una instancia de TaskManager
    task_manager = TaskManager(conn, cursor)
    
    # Empezamos nuestro programa
    while True:
        
        # Mostramos el menú
        mostrar_menu()
        
        # Le pedimos al usuario que escoga una opción
        opcion = input("Seleccionar una opción (1-5): ")
        
        # Validamos la opción dada
        if opcion == '1':
            # Crear una tarea
            title = input("Ingresa el título de la tarea: ")
            task_manager.add_task(title)

        elif opcion == '2':
            # Ver todas las tareas
            print("Lista de tareas:")
            tasks = task_manager.get_tasks()
            if tasks:
                for task in tasks:
                    status = "Completada" if task[2] else "Pendiente"
                    print(f"ID: {task[0]}, Título: {task[1]}, Estado: {status}")
            else:
                print("No hay tareas.")

        elif opcion == '3':
            # Completar una tarea
            task_id = input("Ingresa el ID de la tarea a completar: ")
            task_manager.complete_task(task_id)

        elif opcion == '4':
            # Eliminar una tarea
            task_id = input("Ingresa el ID de la tarea a eliminar: ")
            task_manager.delete_task(task_id)

        elif opcion == '5':
            # Salir
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
    
    # Cerrar la conexión a la base de datos
    task_manager.close()

# Ejecutamos el programa
main()