import os
import matplotlib.pyplot as plt
import pandas as pd

#lee el archivo csv usnado la libreria panada
datos = pd.read_csv("02-12-2022-CasosConfirmados.csv", header=0)

#limpia la pantalla (un comando diferente dependiendo del sistema operativo)
def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#Sirve para filtrar por el nombre de la region
def Region(region):
    datos_filt = datos[datos["Region"] ==  region]
    
    if datos_filt.shape[0] == 0:
        print("Region no encontrada: ")

    else:        
        return(datos_filt)

#silve para filtrar por el codigo dela region
def Region_cod(region):
    datos_filt = datos[datos["Codigo region"] ==  region]
    if datos_filt.shape[0] == 0:
        print("Region no encontrada: ")

    else:
        return(datos_filt)

#desplega el grafico
def Grafico(ejex, ejey):
    plt.barh(ejex, ejey)
    plt.show()

#filtra por rango
def Rango(minimo, maximo, columna):
    datos[columna] = datos[columna].astype(float)
    filtro = (datos[columna] >= minimo) & (datos[columna] <= maximo)
    datos_filt = datos[filtro]
    if datos_filt.shape[0]== 0 :
        print("Error: Rango no valido")
    else:
        return(datos_filt)
    
#exporta los datos a un archivo, la extension depende del usuario
def exportar(datos_filt):
    print('1. CSV')
    print('2. XLSX')
    print('3. TXT')
    opcion = input('Como quiere guardar los datos?:')
    if opcion == '1':
        datos_filt.to_csv("Datos_Filtrados.csv", index = False)
    elif opcion == '2':
        datos_filt.to_excel("Datos_Filtrados.xlsx", index = False)
    elif opcion == '3':
        datos_filt.to_csv("Datos_Filtrados.txt", index = False)

#sirve para desplegar multiples visualizaciones
def subplotgraf(x, y):
    contplot = 221  
    #genera un grafico por cada dato en las listas
    for i in range(0, len(x)) :
        ejex = x[i]
        ejey = y[i]
        
        plt.subplot(contplot)
        plt.barh(ejex, ejey)
        contplot += 1
    plt.tight_layout()
    plt.show()
    

#Es lainterfaz de usuraio
def interfaz():
    while True:#se ejecuta hasta que el usuario lo decida
        print('***--------Menu de Opciones--------***')#opciones 
        print('1. Datos por rango')
        print('2. Desplegar por Region')
        print('3. Desplegar visualizacion/nes')
        print('4. Exportar subconjunto')
        print('5. Salir')
        opcion = input('Seleccione su opcion: ')
        Clear()
        #Esta parte del codigo verifica laopcion del usuario y llama a la funcion correspondiente
        if opcion == '1':
            print('1. Para Poblacion')
            print('2. Casos Confirmados')
            op_rango = input('Seleccione su opcion: ')
            if op_rango == '1':
                columna = 'Poblacion'
                minimo = float(input('Ingrese numero minimo: '))
                maximo = float(input('Ingrese numero maximo: '))
                
                Grafico(Rango(minimo, maximo, columna)['Comuna'], Rango(minimo, maximo, columna)[columna])
                
                Clear()
            elif op_rango == '2':
                columna = 'CasosConfirmados'
                minimo = float(input('Ingrese numero minimo: '))
                maximo = float(input('Ingrese numero maximo: '))
                
                Grafico(Rango(minimo, maximo, columna)['Comuna'], Rango(minimo, maximo, columna)[columna])
                
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
            print('**---Desplegar visualizacion/nes---**')
            print('(Maxima cantidad de Visulizaaaciones =4)')
            respuesta = input('Quieres hacer un grafico?: (y/n) ')
            contador = 0
            x = []
            y = []

            while respuesta.lower() == 'y':
                contador += 1
                
                print('Como quieres que sea el grafico')
                print('1. Datos por rango')
                print('2. Desplegar por Region')

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
                        #agrega los datos filtrados a una lista p
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
                    
                if contador == 4: # el maximo es 4 porque es la manera de que queden bien distribuidos los graficos 
                    break
                
                respuesta = input('Quieres hacer otro grafico?: (y/n) ')
                Clear()
            subplotgraf(x , y)
            
                
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