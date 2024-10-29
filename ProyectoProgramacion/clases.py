class Credito:
    def __init__(self, nombre_asignatura, codigo_asignatura, cantidad):
        self.nombre_asignatura = nombre_asignatura
        self.codigo_asignatura = codigo_asignatura
        self.cantidad = cantidad

    def to_dict(self):
        return {
            'nombre_asignatura': self.nombre_asignatura,
            'codigo_asignatura': self.codigo_asignatura,
            'cantidad': self.cantidad
        }
    
    def __str__(self):
        return f"{self.nombre_asignatura} (Código: {self.codigo_asignatura}, Créditos: {self.cantidad})"



class Estudiante:
    def __init__(self, nombre, id_estudiante, contrasena, creditos=None):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.contrasena = contrasena
        self.creditos = creditos if creditos is not None else []

    def agregar_credito(self, credito):
        self.creditos.append(credito)

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'id_estudiante': self.id_estudiante,
            'contrasena': self.contrasena,
            'creditos': [credito.to_dict() for credito in self.creditos]
        }


class Administrador:
    def __init__(self, nombre, id_administrador):
        self.nombre = nombre
        self.id_administrador = id_administrador

    def crear_estudiante(self, nombre, id_estudiante, contrasena):
        return Estudiante(nombre, id_estudiante, contrasena)

    def asignar_credito(self, estudiante, credito):
        estudiante.agregar_credito(credito)


class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def enviar(self):
        print(f"Notificación enviada: {self.mensaje}")


class Programa:
    def __init__(self, nombre, creditos_requeridos):
        self.nombre = nombre
        self.creditos_requeridos = creditos_requeridos

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'creditos_requeridos': self.creditos_requeridos
        }
