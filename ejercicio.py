import os

def fnt_limpiarpantalla():
    os.system('cls')
    print('Saludo')
    print('Autor: Valentina Arias Raigosa')
    print('Universidad Catolica Luis Amigó')
    print('\n\n')
    
def fnt_mostrarMensaje(mensaje):
    print(f'Bienvenido a Python {mensaje}')

def fnt_saludo():
    fnt_limpiarpantalla()
    nombre = input('Por favor ingresa tu nombre: ')
    fnt_mostrarMensaje(nombre)
    
fnt_saludo()