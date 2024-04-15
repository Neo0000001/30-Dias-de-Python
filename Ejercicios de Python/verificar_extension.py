
class VerificarExtension:
    def __init__(self, cadena):
        self.cadena = cadena
        
    def verificar_extension(self):
        if self.cadena[-3:] == '.py':
            print('La cadena termina con la extension .py')
        else:
            print(self.cadena + '.py')
            
cadena_1 = VerificarExtension('archivo.py')
cadena_1.verificar_extension()