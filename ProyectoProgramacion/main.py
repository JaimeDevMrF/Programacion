from clases import Estudiante, Credito, Administrador, Notificacion, Programa
from persistencia import Persistencia

def menu_administrador(admin, persistencia, estudiantes):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Crear nuevo estudiante")
        print("2. Asignar crédito a estudiante")
        print("3. Ver todos los estudiantes")
        print("4. Enviar notificación")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            id_estudiante = input("Ingrese el ID del estudiante: ")
            contrasena = input("Ingrese la contraseña del estudiante: ")
            estudiante = admin.crear_estudiante(nombre, id_estudiante, contrasena)
            estudiantes.append(estudiante)
            persistencia.guardar_estudiantes(estudiantes)
            print(f"Estudiante {nombre} creado exitosamente.")

        elif opcion == '2':
            id_estudiante = input("Ingrese el ID del estudiante: ")
            for estudiante in estudiantes:
                if estudiante.id_estudiante == id_estudiante:
                    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
                    codigo_asignatura = input("Ingrese el código de la asignatura: ")
                    creditos = int(input("Ingrese la cantidad de créditos: "))
                    credito = Credito(nombre_asignatura, codigo_asignatura, creditos)
                    admin.asignar_credito(estudiante, credito)
                    persistencia.guardar_estudiantes(estudiantes)
                    print(f"Crédito {nombre_asignatura} asignado a {estudiante.nombre}.")
                    break
            else:
                print("Estudiante no encontrado.")

        elif opcion == '3':
            print("\n--- Estudiantes ---")
            for estudiante in estudiantes:
                print(f"Nombre: {estudiante.nombre}, ID: {estudiante.id_estudiante}, Créditos: {estudiante.creditos}")

        elif opcion == '4':
            mensaje = input("Ingrese el mensaje de la notificación: ")
            notificacion = Notificacion(mensaje)
            notificacion.enviar()

        elif opcion == '5':
            break

        else:
            print("Opción inválida. Intente de nuevo.")

def menu_estudiante(estudiante):
    while True:
        print("\n--- Menú Estudiante ---")
        print(f"Bienvenido, {estudiante.nombre}")
        print("1. Ver información personal")
        print("2. Ver créditos cursados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print(f"Nombre: {estudiante.nombre}, ID: {estudiante.id_estudiante}, Créditos: {estudiante.creditos}")
        
        elif opcion == '2':
            print(f"Créditos cursados: {', '.join(str(credito) for credito in estudiante.creditos)}")

        elif opcion == '3':
            break

        else:
            print("Opción inválida. Intente de nuevo.")

def iniciar_sesion(estudiantes):
    id_estudiante = input("Ingrese su ID: ")
    contrasena = input("Ingrese su contraseña: ")
    for estudiante in estudiantes:
        if estudiante.id_estudiante == id_estudiante and estudiante.contrasena == contrasena:
            return estudiante
    print("ID o contraseña incorrectos.")
    return None

# Carga de datos inicial
archivo_estudiantes = 'estudiantes.json'
archivo_creditos = 'creditos.json'
persistencia = Persistencia(archivo_estudiantes, archivo_creditos)
estudiantes = persistencia.cargar_estudiantes()

# Crear un administrador
admin = Administrador("Admin", "admin001")

# Menú principal
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión como administrador")
        print("2. Iniciar sesión como estudiante")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_administrador(admin, persistencia, estudiantes)

        elif opcion == '2':
            estudiante = iniciar_sesion(estudiantes)
            if estudiante:
                menu_estudiante(estudiante)

        elif opcion == '3':
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
