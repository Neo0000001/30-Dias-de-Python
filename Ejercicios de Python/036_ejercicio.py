# Ejercicio 36: Crear una clase para representar los datos de una persona.

class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, edad: {self.edad}, correo: {self.correo}'
    
persona_1 = Persona('Enrique', 47, 'enrique.secilla@gmail.com')

print(persona_1)