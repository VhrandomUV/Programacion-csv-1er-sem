import matplotlib.pyplot as plt
import pandas as pd
import os

datos = pd.read_csv("02-12-2022-CasosConfirmados.csv", header=0)


def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def Region(region):
    
    datos_filt = datos[datos["Region"] ==  region]
    if datos_filt.shape[0] == 0:
        print("Region no encontrada: ")

    else:

        ejex = datos_filt['Comuna']
        ejey = datos_filt['CasosConfirmados']

        plt.ylabel('Comuna')
        plt.xlabel('Casos Confirmados')
        plt.title(f'Region: {region}')
        Grafico(ejex, ejey)


def Region_cod(region):
    
    datos_filt = datos[datos["Codigo region"] ==  region]
    if datos_filt.shape[0] == 0:
        print("Region no encontrada: ")

    else:

        ejex = datos_filt['Comuna']
        ejey = datos_filt['CasosConfirmados']

        plt.ylabel('Comuna')
        plt.xlabel('Casos Confirmados')
        plt.title(f'Region: {region}')
        Grafico(ejex, ejey)



def Grafico(ejex, ejey):
    plt.barh(ejex, ejey)
    plt.show()



def Rango(minimo, maximo, columna):
    datos[columna] = datos[columna].astype(float)
    filtro = (datos[columna] >= minimo) & (datos[columna] <= maximo)
    datos_filt = datos[filtro]
    if datos_filt.shape[0]== 0 :
        print("Error: Rango no valido")
    else:
        return(datos_filt)
    

def exportar(datos_filt, index = False):
    datos_filt.to_csv("prueba.csv")




def interfaz():
    while True:
        print('***--------Menu de Opciones--------***')
        
        print('1. Datos por rango')
        print('2. Desplegar por Region')
        print('3. Desplegar visualizacion/nes')
        print('4. Exportar subconjunto')
        print('5. Salir')
        opcion = input('Seleccione su opcion: ')
        Clear()

        if opcion == '1':
            print('1. Para Poblacion')
            print('2. Casos Confirmados')
            op_rango = input('Seleccione su opcion: ')
            if op_rango == '1':
                columna = 'Poblacion'
                minimo = float(input('Ingrese numero minimo: '))
                maximo = float(input('Ingrese numero maximo: '))
                print(Rango(minimo, maximo, columna))
                input("Presione enter para continuar: ")
                Clear()
            elif op_rango == '2':
                columna = 'CasosConfirmados'
                minimo = float(input('Ingrese numero minimo: '))
                maximo = float(input('Ingrese numero maximo: '))
                print(Rango(minimo, maximo, columna))
                input("Presione enter para continuar: ")
                Clear()
            else:
                print('Opcion no valida')
                input("Presione enter para continuar: ")
                Clear()

        elif opcion == '2':
            print('Eliga metodo de filtrado')
            print('1. Nombre')
            print('2. Codigo')
            op_filt = input('Seleccione su opcion: ')
            Clear()

            if op_filt == '1':
                region = input("Ingrese el nombre de la region: ")
                Region(region)
                Clear()
            elif op_filt == '2':
                region = int(input("Ingrese codigo de region: "))
                Region_cod(region)
                Clear()
        elif opcion == '3':
            print('Opcion 3 elegida')


        elif opcion == '4':
            print('Elija subconjunto')
            print("1. Rango")
            print("2. Region")
            opcion = input("Sellecione su opcion: ")
            if opcion == '1':
                print('1. Para Poblacion')
                print('2. Casos Confirmados')
                op_rango = input('Seleccione su opcion: ')
                if op_rango == '1':
                    columna = 'Poblacion'
                    minimo = float(input('Ingrese numero minimo: '))
                    maximo = float(input('Ingrese numero maximo: '))
                    
                elif op_rango == '2':
                    columna = 'CasosConfirmados'
                    minimo = float(input('Ingrese numero minimo: '))
                    maximo = float(input('Ingrese numero maximo: '))
                    datos_filt = Rango(minimo, maximo, columna)
                    print(Rango(minimo, maximo, columna))
                    exportar(datos_filt)
                else:
                    print('Opcion no valida')
                    input("Presione enter para continuar: ")
                    Clear()
                


            elif opcion == '2':
                print('Eliga metodo de filtrado')
                print('1. Nombre')
                print('2. Codigo')
                op_filt = input('Seleccione su opcion: ')
            
            


        elif opcion == '5':
            Clear()
            break
        


if __name__ == "__main__":
    interfaz()