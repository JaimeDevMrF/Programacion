import json
import os
from clases import Estudiante, Credito  # Asegúrate de importar todas las clases necesarias

class Persistencia:
    def __init__(self, estudiantes_file, creditos_file):
        self.estudiantes_file = estudiantes_file
        self.creditos_file = creditos_file

    def guardar_estudiantes(self, estudiantes):
        with open(self.estudiantes_file, 'w') as file:
            json.dump([estudiante.to_dict() for estudiante in estudiantes], file)

    def cargar_estudiantes(self):
        if not os.path.exists(self.estudiantes_file):
            return []
        with open(self.estudiantes_file, 'r') as file:
            estudiantes_data = json.load(file)
            return [Estudiante(**data) for data in estudiantes_data]

    def guardar_creditos(self, creditos):
        with open(self.creditos_file, 'w') as file:
            json.dump([credito.to_dict() for credito in creditos], file)

    def cargar_creditos(self):
        if not os.path.exists(self.creditos_file):
            return []
        with open(self.creditos_file, 'r') as file:
            creditos_data = json.load(file)
            return [Credito(**data) for data in creditos_data]
