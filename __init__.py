from time import sleep
from operator import itemgetter
from random import randint
from datetime import date
from os import system, name
from termcolor import colored
colored('texto', 'blue')

def limpiarPantalla():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def lineaSeparacion(mensaje='', complemento='-', alineacion='^', limite='50'):
    print(f'{mensaje:{complemento}{alineacion}{limite}}')


def leerEntero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
        except(ValueError, TypeError):
            print('\033[31mERROR: Por favor, introduzca un número entero válido.\033[m') 
            continue           
        except(KeyboardInterrupt):
            print('\033[31mERROR: El usuario prefiere no introducir este número.\033[m') 
            return 0
        else:
            return num
    
        
def archivoExiste(archivo):
    try:
        fileRead = open(archivo, 'rt')
        fileRead.close()
    except(FileNotFoundError):
        return False
    else:
        return True
    
    
def crearArchivo(archivo):
    try:
        fileRead = open(archivo, 'wt+')
        fileRead.close()
    except:
        print('Se ha producido un error al crear el archivo.')
    else:
        print('Archivo creado con suceso.')
    
    
def leerArchivo(archivo):
    try:
        fileRead = open(archivo, 'rt')
    except:
        print('ERROR al leer el archivo.')
    else:
        cabecera('Cursos Cadastrados')
        for linea in fileRead:
            dato = linea.split(';')
            dato[3] = dato[3].replace('\n', '')
            print(f'{dato[0]:>4} - {dato[1]:<27}{dato[2]:>3} {dato[3]:>11}')
    finally:
        fileRead.close()
    

def registrar(archivo, title='desconhecido', duration=0, date=date.today):
    try:
        fileRead = open(archivo, 'rt')
        contador = 0
        contenido = fileRead.read()
        contenidoLista = contenido.split('\n')
        for i in contenidoLista:
            if i: contador += 1
        fileRead.close()
        try:
            fileRead = open(archivo, 'at')
        except:
            print('ERROR al abrir el archivo.')
        else:
            try:
                fileRead.write(f'{contador + 1};{title};{duration};{date}\n')
            except:
                print('Se ha producido un ERROR al escribir los datos.')
            else:
                print(f'Nuevo registro de {title} añadido.')      
        finally:
                fileRead.close() 
    except(FileNotFoundError):
        return False


def borrar(archivo, id):
    try:
        with open(archivo, 'r') as fr:
            lineas = fr.readlines()
        with open(archivo, 'w') as fw:
            for linea in lineas:
                dato = linea.split(';')
                if dato[0] != str(id):
                    fw.write(linea)
            fw.close()
        print("Borrado")
    except:
        print("Se ha producido un ERROR al borrar los datos.")
    
    
def cambiar(archivo, id, title, duration, date):
    try:
        with open(archivo, 'r') as fr:
            lineas = fr.readlines()
        with open(archivo, 'w') as fw:
            for linea in lineas:
                dato = linea.split(';')
                if dato[0] != str(id):
                    fw.write(linea)
                else:
                    dato = linea.split(';')
                    if title == '':
                        title = dato[1]
                    if duration == -1:
                        duration = dato[2]
                    if date == '':
                        date = dato[3].replace('\n', '')
                    fw.write(f'{id};{title};{duration};{date}\n')
            fw.close()
        print("Cambiado")
    except:
        print("Se ha producido un ERROR al cambiar los datos.")        
    
    
def cabecera(texto):
    lineaSeparacion('', complemento='-')
    lineaSeparacion(mensaje=texto, complemento='')
    lineaSeparacion('', complemento='-')
    
    
def menu(lista):
    cabecera('MENÚ PRINCIPAL')
    cont = 1
    for itens in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{itens}\033[m')
        cont += 1
    lineaSeparacion()
    opcion = leerEntero('Su opción: ') 
    return opcion   