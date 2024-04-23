import os

def fnt_limpiarpantalla():
    os.system('cls')
    print('Velocidad promedio')
    print('Autor: Valentina Arias Raigosa')
    print('Universidad Catolica Luis Amigó')
    print('\n\n')

def fnt_valores(repetir):
    while repetir == True:
        fnt_limpiarpantalla()
        distancia = int(input('¿Cuantos km hicieron? -> '))
        tiempo = int(input('¿Cuantas horas hicieron? -> '))
        fnt_velocidad(distancia,tiempo)
        
        enter = input('\n<ENTER> Para repetir\n<F> Para salir\n\n')
        if enter == 'f' or enter == 'F':
            repetir = False
    
def fnt_velocidad(distancia,tiempo):
    velocidad = distancia/tiempo
    print(f'La velocidad es de {velocidad} km/h')
    
fnt_valores(True)