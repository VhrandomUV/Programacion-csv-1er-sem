import os
import matplotlib.pyplot as plt
import pandas as pd


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
        return(datos_filt)


def Region_cod(region):
    datos_filt = datos[datos["Codigo region"] ==  region]
    if datos_filt.shape[0] == 0:
        print("Region no encontrada: ")

    else:
        return(datos_filt)


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
    

def exportar(datos_filt):
    datos_filt.to_csv("Datos_Filtrados.csv", index = False)


def subplotgraf(x, y):
    contplot = 221
    for i in x:
        contplot = 221
        plt.subplot(contplot)
        plt.barh(x[i], y[i])
        contplot += 1
    plt.show()
    



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
                Grafico(Rango(minimo, maximo, columna)['Comuna'], Rango(minimo, maximo, columna)[columna])
                #input("Presione enter para continuar: ")
                Clear()
            elif op_rango == '2':
                columna = 'CasosConfirmados'
                minimo = float(input('Ingrese numero minimo: '))
                maximo = float(input('Ingrese numero maximo: '))
                print(Rango(minimo, maximo, columna))
                Grafico(Rango(minimo, maximo, columna)['Comuna'], Rango(minimo, maximo, columna)[columna])
                #input("Presione enter para continuar: ")
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
                plt.ylabel('Comuna')
                plt.xlabel('Casos Confirmados')
                plt.title(f'Region: {region}')
                Grafico(Region(region)['Comuna'], Region(region)['CasosConfirmados'])
                Clear()
            elif op_filt == '2':
                region = int(input("Ingrese codigo de region: "))
                plt.ylabel('Comuna')
                plt.xlabel('Casos Confirmados')
                plt.title(f'Region: {region}')
                Grafico(Region_cod(region)['Comuna'], Region_cod(region)['CasosConfirmados'])
                Clear()



   
                
        elif opcion == '3':
            print('**Desplegar visualizacion/nes**')
            respuesta = input('Quieres hacer un grafico?: (y/n) ')
            contador = 0
            x = []
            y = []

            while respuesta.lower() == 'y' and contador != 5:
                contador += 1
                
                print('Como quieres que sea el grafico')
                print('1. Datos por rango')
                print('2. Desplegar por Region')

                opcion = input('Seleccione su opcion: ')

                if opcion == '1':
                    print('1. Para Poblacion')
                    print('2. Casos Confirmados')
                    op_rango = input('Seleccione su opcion: ')
                    if op_rango == '1':
                        columna = 'Poblacion'
                        minimo = float(input('Ingrese numero minimo: '))
                        maximo = float(input('Ingrese numero maximo: '))
                        
                        x.append(Rango(minimo, maximo, columna)['Comuna'])
                        y.append(Rango(minimo, maximo, columna)[columna])
                        
                    elif op_rango == '2':
                        columna = 'CasosConfirmados'
                        minimo = float(input('Ingrese numero minimo: '))
                        maximo = float(input('Ingrese numero maximo: '))
                        x.append(Rango(minimo, maximo, columna)['Comuna'])
                        y.append(Rango(minimo, maximo, columna)[columna])
                        
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
                        x.append(Region(region)['Comuna'])
                        y.append(Region(region)['CasosConfirmados'])
                        
                    elif op_filt == '2':
                        region = int(input("Ingrese codigo de region: "))
                        x.append(Region_cod(region)['Comuna'])
                        y.append(Region_cod(region)['CasosConfirmados'])


                
                
                respuesta = input('Quieres hacer otro grafico?: (y/n) ')
            Grafico(x,y)
            
                

            





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
                    datos_filt = Rango(minimo, maximo, columna)
                    exportar(datos_filt)
                    Clear()
                    
                elif op_rango == '2':
                    columna = 'CasosConfirmados'
                    minimo = float(input('Ingrese numero minimo: '))
                    maximo = float(input('Ingrese numero maximo: '))
                    datos_filt = Rango(minimo, maximo, columna)
                    exportar(datos_filt)
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

                if op_filt == '1':
                    region = input("Ingrese el nombre de la region: ")
                    exportar(Region(region))
                    
                    Clear()
                elif op_filt == '2':
                    region = int(input("Ingrese codigo de region: "))
                    exportar(Region_cod(region))

                    
                    Clear()


        elif opcion == '5':
            Clear()
            break
        

if __name__ == "__main__":
    interfaz()