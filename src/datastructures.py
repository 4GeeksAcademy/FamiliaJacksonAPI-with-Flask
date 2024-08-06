
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, apellido):
        self.apellido = apellido
        self._siguiente_id = 1
        self._miembros = [
            {"id": self._generar_id(), "primer_nombre": "John", "apellido": apellido, "edad": 33, "numeros_de_suerte": [7, 13, 22]},
            {"id": self._generar_id(), "primer_nombre": "Jane", "apellido": apellido, "edad": 35, "numeros_de_suerte": [10, 14, 3]},
            {"id": self._generar_id(), "primer_nombre": "Jimmy", "apellido": apellido, "edad": 5, "numeros_de_suerte": [1]}
        ]

    def _generar_id(self):
        id_generado = self._siguiente_id
        self._siguiente_id += 1
        return id_generado

    def agregar_miembro(self, miembro):
        if "primer_nombre" in miembro and "edad" in miembro and "numeros_de_suerte" in miembro:
            miembro["id"] = self._generar_id()
            miembro["apellido"] = self.apellido
            self._miembros.append(miembro)
            return miembro
        return None

    def eliminar_miembro(self, id):
        for miembro in self._miembros:
            if miembro["id"] == id:
                self._miembros.remove(miembro)
                return {"done": True}
        return {"error": "Miembro no encontrado"}

    def obtener_miembro(self, id):
        for miembro in self._miembros:
            if miembro["id"] == id:
                return miembro
        return None
    
    def obtener_todos_los_miembros(self):
        return self._miembros
