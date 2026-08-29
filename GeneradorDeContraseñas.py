import random
import string
import secrets  # Mas seguro que random para contrasenas

class GeneradorContrasenas:
    def __init__(self):
        self.longitud = 16
        self.usar_mayusculas = True
        self.usar_minusculas = True
        self.usar_numeros = True
        self.usar_simbolos = True
    
    def generar(self):
        """Genera una contrasena segura"""
        caracteres = ""
        
        if self.usar_minusculas:
            caracteres += string.ascii_lowercase
        if self.usar_mayusculas:
            caracteres += string.ascii_uppercase
        if self.usar_numeros:
            caracteres += string.digits
        if self.usar_simbolos:
            caracteres += string.punctuation
        
        if not caracteres:
            return "Error: Selecciona al menos un tipo de caracter"
        
        
        contrasena = ''.join(secrets.choice(caracteres) for _ in range(self.longitud))
        return contrasena
    
    def generar_multiple(self, cantidad=5):
        """Genera multiples contrasenas"""
        return [self.generar() for _ in range(cantidad)]
    
    def configurar(self, longitud=None, mayusculas=None, minusculas=None, 
                   numeros=None, simbolos=None):
        """Configura los parametros del generador"""
        if longitud is not None:
            self.longitud = max(4, longitud)  
        if mayusculas is not None:
            self.usar_mayusculas = mayusculas
        if minusculas is not None:
            self.usar_minusculas = minusculas
        if numeros is not None:
            self.usar_numeros = numeros
        if simbolos is not None:
            self.usar_simbolos = simbolos
    
    def pedir_configuracion(self):
        """Pide al usuario que configure los parametros interactivamente"""
        print("\n" + "="*50)
        print("    CONFIGURACION DEL GENERADOR")
        print("="*50)
        
        
        while True:
            try:
                longitud = input("Longitud de la contrasena (minimo 4, default 16): ")
                if longitud == "":
                    longitud = 16
                else:
                    longitud = int(longitud)
                    if longitud < 4:
                        print("La longitud debe ser al menos 4!")
                        continue
                break
            except ValueError:
                print("Por favor, introduce un numero valido")
        
        
        print("\nQue tipos de caracteres quieres incluir?")
        print("(Presiona Enter para mantener el valor por defecto)")
        
        mayusculas = self._preguntar_si_no("Incluir mayusculas? (s/n): ", True)
        minusculas = self._preguntar_si_no("Incluir minusculas? (s/n): ", True)
        numeros = self._preguntar_si_no("Incluir numeros? (s/n): ", True)
        simbolos = self._preguntar_si_no("Incluir simbolos? (s/n): ", True)
        
        
        if not any([mayusculas, minusculas, numeros, simbolos]):
            print("\nERROR! Debes seleccionar al menos un tipo de caracter.")
            print("Se activaran todos los tipos automaticamente.")
            mayusculas = minusculas = numeros = simbolos = True
        
        
        self.configurar(longitud, mayusculas, minusculas, numeros, simbolos)
        
        
        self._mostrar_resumen()
    
    def _preguntar_si_no(self, pregunta, valor_default):
        """Funcion auxiliar para preguntar si/no"""
        respuesta = input(pregunta).lower()
        if respuesta == "":
            return valor_default
        return respuesta in ['s', 'si', 'si', 'yes', 'y']
    
    def _mostrar_resumen(self):
        """Muestra un resumen de la configuracion actual"""
        print("\n" + "="*50)
        print("    RESUMEN DE CONFIGURACION")
        print("="*50)
        print(f"Longitud: {self.longitud} caracteres")
        print(f"Mayusculas: {'Si' if self.usar_mayusculas else 'No'}")
        print(f"Minusculas: {'Si' if self.usar_minusculas else 'No'}")
        print(f"Numeros: {'Si' if self.usar_numeros else 'No'}")
        print(f"Simbolos: {'Si' if self.usar_simbolos else 'No'}")
        print("="*50)


def menu_principal():
    print("\n" + "="*50)
    print("     GENERADOR DE CONTRASENAS")
    print("="*50)
    print("1 - Configurar y generar una contrasena")
    print("2 - Configurar y generar multiples contrasenas")
    print("3 - Usar configuracion actual y generar")
    print("4 - Ver configuracion actual")
    print("5 - Salir")
    print("="*50)


if __name__ == "__main__":
    generador = GeneradorContrasenas()
    
    while True:
        menu_principal()
        opcion = input("\nSelecciona una opcion (1-5): ")
        
        if opcion == "1":
            generador.pedir_configuracion()
            print("\n" + "="*50)
            print("    CONTRASENA GENERADA")
            print("="*50)
            print(f" {generador.generar()}")
            print("="*50)
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "2":
            generador.pedir_configuracion()
            
            while True:
                try:
                    cantidad = input("\nCuantas contrasenas quieres generar? (default 5): ")
                    if cantidad == "":
                        cantidad = 5
                    else:
                        cantidad = int(cantidad)
                        if cantidad <= 0:
                            print("Debe ser un numero positivo!")
                            continue
                    break
                except ValueError:
                    print("Por favor, introduce un numero valido")
            
            print("\n" + "="*50)
            print("    CONTRASENAS GENERADAS")
            print("="*50)
            for i, contra in enumerate(generador.generar_multiple(cantidad), 1):
                print(f"{i}. {contra}")
            print("="*50)
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "3":
            print("\n" + "="*50)
            print("    CONTRASENA GENERADA")
            print("="*50)
            print(f" {generador.generar()}")
            print("="*50)
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "4":
            generador._mostrar_resumen()
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "5":
            print("\nHasta luego, primo! ")
            break
        
        else:
            print("\nOpcion no valida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")