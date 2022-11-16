def leer_archivo(file_name):
    print(f'Intentas abrir este archivo {file_name}')
    #Abrir open()
    #Procesar read/write
    #Cerrar close()
    #With nos permite agrupar el trabajo con archivos
    with open(file_name, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            print(linea, end='')
        #while(linea):
        #    print(linea)
        #   linea = file.readline()
    #print('Archivo leído y cerrado')

def agregar_equipo(file_name, equipo):
    print(f'Intentas abrir este archivo {file_name}')
    with open(file_name, 'a') as file:
        file.write(f"\n{equipo}")

    print('Equipo Guardado')

def eliminar_equipo(file_name, equipo):
    print(f'Intentas abrir este archivo {file_name}')
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        lista_equipos.remove(equipo)
        print("Equipo Eliminado!")
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print('El equipo que deseas eliminar no existe')
        
def actualiza_equipo(file_name, equipo, new_equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        index_equipo = lista_equipos.index(f'{equipo}\n')
        lista_equipos[index_equipo] = new_equipo
        with open(file_name, 'w') as file:
            file.writelines(f'{lista_equipos}\n')
    except ValueError:
        print('El equipo no se encontro')