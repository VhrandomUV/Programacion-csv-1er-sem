import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv("02-12-2022-CasosConfirmados.csv", header=0)


def Region(region):
    
    datos_filt = datos[datos["Region"] ==  region]
    if datos_filt.shape[0] == 0:
        print("Region no encontrada: ")

    else:

        ejex = datos_filt['Comuna']
        ejey = datos_filt['CasosConfirmados']

        plt.xlabel('Comuna')
        plt.ylabel('Casos Confirmados')
        plt.title(f'Region: {region}')

        plt.barh(ejex, ejey)
        plt.show()


def Region_cod(region):
    
    datos_filt = datos[datos["Codigo region"] ==  region]
    if datos_filt.shape[0] == 0:
        print("Region no encontrada: ")

    else:

        ejex = datos_filt['Comuna']
        ejey = datos_filt['CasosConfirmados']

        plt.xlabel('Comuna')
        plt.ylabel('Casos Confirmados')
        plt.title(f'Region: {region}')

        plt.barh(ejex, ejey)
        plt.show()



def Grafico(ejex, ejey):
    plt.barh(ejex, ejey)
    plt.show()



def Rango(minimo, maximo, columna):
    datos[columna] = datos[columna].astype(float)
    filtro = (datos[columna] >= minimo) & (datos[columna] <= maximo)
    datos_filtrados = datos[filtro]
    print(datos_filtrados)
    return(datos_filtrados)


def interfaz():
    while True:
        print('***--------Menu de Opciones--------***')
        
        print('1. Datos por rango')
        print('2. Desplegar por Region')
        print('3. Desplaegra visualizacion/nes')
        print('4. Exportar subconjunto')
        print('5. Salir')
        opcion = input('Seleccione su opcion: ')

        if opcion == '1':
            print('1. Para Poblacion')
            print('2. Casos Confirmados')
            op_rango = input('Seleccione su opcion: ')
            if op_rango == '1':
                columna = 'Poblacion'
                minimo = float(input('Ingrese numero minimo: '))
                maximo = float(input('Ingrese numero maximo: '))
                Rango(minimo, maximo, columna)
                
            elif op_rango == '2':
                columna = 'CasosConfirmados'
                minimo = float(input('Ingrese numero minimo: '))
                maximo = float(input('Ingrese numero maximo: '))
                Rango(minimo, maximo, columna)
            else:
                print('Opcion no valida')

        elif opcion == '2':
            print('Eliga metodo de filtrado')
            print('1. Nombre')
            print('2. Codigo')
            op_filt = input('Seleccione su opcion: ')

            if op_filt == '1':
                region = input("Ingrese el nombre de la region: ")
                Region(region)
            elif op_filt == '2':
                region = int(input("Ingrese codigo de region: "))
                Region_cod(region)
        elif opcion == '3':
            print('Opcion 3 elegida')
        elif opcion == '4':
            print('Opcion 4 elegida')
        elif opcion == '5':
            break


if __name__ == "__main__":
    interfaz()