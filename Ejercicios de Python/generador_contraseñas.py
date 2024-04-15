import random
import string

class PasswordGenerator:
    def __init__(self, length=8, uppercase=True, numbers=True, symbols=True):
        self.length = length
        self.uppercase = uppercase
        self.numbers = numbers
        self.symbols = symbols

    def generate_password(self):
        """Genera una contraseña aleatoria con los parámetros especificados en el constructor."""

        # Definimos los caracteres posibles para cada tipo de carácter
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase if self.uppercase else ''
        digits = string.digits if self.numbers else ''
        symbols_characters = string.punctuation if self.symbols else ''

        # Concatenamos los caracteres posibles
        characters = f'{lowercase_letters}{uppercase_letters}{digits}{symbols_characters}'

        # Verificamos si la longitud solicitada es válida
        if self.length < 8 or self.length > 16:
            raise ValueError('La longitud debe estar entre 8 y 16 caracteres.')

        # Generamos la contraseña aleatoria
        password = ''.join(random.choices(characters, k=self.length))

        return password

# Ejemplo de uso
pg = PasswordGenerator(length=12, uppercase=True, numbers=True, symbols=True)
password = pg.generate_password()
print(password)

"""
Explicación:

La clase PasswordGenerator se define con un constructor que acepta unos parámetros opcionales para especificar la longitud deseada de la 
contraseña, así como si se quieren incluir mayúsculas, números y/o símbolos en la contraseña. Por defecto, estos parámetros están establecidos 
a True, lo que significa que se incluirán en la contraseña.

En el método generate_password, se siguen los mismos pasos que en el ejemplo anterior para generar una contraseña aleatoria con los parámetros 
especificados en el constructor.

El ejemplo de uso es similar al anterior, pero en lugar de llamar a una función, creamos una instancia de la clase PasswordGenerator y llamamos 
al método generate_password de esa instancia.

Espero que este ejemplo te sea útil para entender cómo implementar esta funcionalidad utilizando clases en Python.
"""