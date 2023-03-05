
from lib.interface import *
archivo = 'archivos_txt\sistema1.txt'
if not archivoExiste(archivo):
    crearArchivo(archivo)

primeraVez = True
while True:
    if primeraVez: limpiarPantalla()
    respuesta = menu(['Lista de Cursos', 'Registrar Cursos', 'Borrar Registro', 'Cambiar Registro', 'SALIR'])
    if respuesta == 1:
        #cabecera('Opción 1')
        #Leer archivo y listar contenido
        leerArchivo(archivo)
        primeraVez = False
    elif respuesta == 2:
        #cabecera('Nuevo Registro')
        #Crear un nuevo registro 
        title = input('Title: ')
        duration = leerEntero('Duration: ')
        date = input('Date: ')
        registrar(archivo, title, duration, date)
        primeraVez = False
    elif respuesta == 3:
        #Borrar el registro selecionado
        cabecera('Borrar Registro')
        id = leerEntero('Id: ')
        borrar(archivo, id)
        primeraVez = False
    elif respuesta == 4:
        #Cambiar el registro selecionado
        cabecera('Cambiar Registro')
        codigo = leerEntero('codigo: ')
        nombre = str(input('Nombre: '))
        edad = leerEntero('Edad: ')
        cambiar(archivo, codigo, nombre, edad)
        primeraVez = False
    elif respuesta == 5:
        cabecera('Salindo del sistema... Hasta luego!')
        break
    else:
        print('\33[31mERROR: Introduzca una opción válida.\033[m')

print('\n\n\n')