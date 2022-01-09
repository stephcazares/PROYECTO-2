# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 11:32:32 2021

@author: Steph
"""
import csv
import pandas as pd
syn_log = []

with open ("synergy_logistics_database.csv","r") as base:
    reader = csv.reader(base)
    
    for linea in reader:
        syn_log.append(linea) 
#%%
#Creare una funcion que itere en el documento y cree una lista en base al tipo de
#movimiento realizado en este caso"Exports" o "Imports", dicha lista tendra la suma
#total de la ruta, especificano de donde sale y a donde llega con"Origen" y "Destino".
def rutas(direction):
    sumarutas = []
    movimientos = []
    contador = 0 
    for ruta in syn_log:
        if ruta[1] == direction:
            rutaexp = [ruta[2],ruta[3]]
    #busca en la base de datos en base al dato que nos interesa que es la 
    #direction" donde iteraremos en si es exportacion o importacion mas delante
            if rutaexp not in movimientos:
                for exp in syn_log:
                    if rutaexp == [exp[2],exp[3]]:
                        contador += 1
                movimientos.append(rutaexp)
                sumarutas.append([ruta[2],ruta[3],contador])
                contador = 0 
                #aqui finalmente obtenemos la inforacion donde nos brinda la ruta
                #y el total de veces que se repitio la misma ruta, ahora lo que
                #procede es ordenarlas de mayor a menor en base a los totales,
                #y para una mejor presentacion se crea una lista en base a la
                #informacion obtenida usando DataFrames, especificando el numero
                #de rutas que nos interesa que son las 10 primeras  y le indicamos el
                #titulo de las columnas
    sumarutas.sort(reverse = True, key = lambda totales:totales[2])
    df =pd.DataFrame(sumarutas[0:10], columns =["Origen","Destino",
                                               "Viajes Realizados"])
    return (print(df))
    
#%%
"""En esta sección  definimos las funciones para obtener el valor total de
importaciones y exportaciones realizadas segun el medio de transporte, para lo
que se busca en el documento syn_log la informacion que esta en las posiciones
7 y 9 y en base a ello creamos sublistas que nos permitirar acumular la
informacion que empate con el mismo medio de transporte, asi como ir sumando el
valor de cada servicio brindado
"""
def tipo_transporte(direccion):
    tipoexportacion = []
    for ruta in syn_log:
        if ruta[1] == "Exports":
            tipoexportacion.append([ruta[7],int(ruta[9])])
    ferreo = []
    terrestre = []
    maritimo = []
    aereo = []
    for tipo in tipoexportacion:
        if tipo[0] == "Sea":
            maritimo.append(tipo[1])
            mar_suma = sum(maritimo)      
        elif tipo[0] == "Air":
            aereo.append(tipo[1])
            aer_suma = sum(aereo)
        elif tipo[0] == "Rail":
            ferreo.append(tipo[1])
            ferr_suma = sum(ferreo)
    
        elif tipo[0] == "Road":
            terrestre.append(tipo[1])
            carr_suma = sum(terrestre)
    
        
    exp_tipo = [["Aereo",aer_suma],["Ferreo",ferr_suma],["Carretero",carr_suma],
                     ["Maritimo",mar_suma]]
    
    exp_tipo.sort(reverse = True, key = lambda totales:totales[1])
    df_tipo =pd.DataFrame(exp_tipo, columns = 
                               ["Tipo de transporte","Total"])
    return(print(df_tipo))

def tipo_transportei(direccion):
    tipoimportacion = []
    for ruta in syn_log:
        if ruta[1] == "Imports":
            tipoimportacion.append([ruta[7],int(ruta[9])])
    ferreo = []
    terrestre = []
    maritimo = []
    aereo = []

    for tipo in tipoimportacion:
        if tipo[0] == "Sea":
            maritimo.append(tipo[1])
            mar_suma = sum(maritimo)      
        elif tipo[0] == "Air":
            aereo.append(tipo[1])
            aer_suma = sum(aereo)
        elif tipo[0] == "Rail":
            ferreo.append(tipo[1])
            ferr_suma = sum(ferreo)
    
        elif tipo[0] == "Road":
            terrestre.append(tipo[1])
            carr_suma = sum(terrestre)
        
    imp_tipo = [["Aereo",aer_suma],["Ferreo",ferr_suma],["Carretero",carr_suma],
                     ["Maritimo",mar_suma]]
    imp_tipo.sort(reverse = True, key = lambda totales:totales[1])
    df_tipo =pd.DataFrame(imp_tipo, columns = 
                           ["Tipo de transporte","Total"])
    return(print(df_tipo))

#%%
"""Finalmente se crea esta funcion que va acumular la informacion referente a
los ingresos obtenidos de los paises, lo veremos dividido entre importaciones y
exportaciones para revisar esta infromacion en conjunto con lo que se obtendra 
de las otras dos funciones
"""
def rutas_pais(direction):
    paises={}
    pais_ordenado = []
    for ruta in syn_log:
        if ruta[1] == direction:
            if ruta[2] not in paises:
                paises[ruta[2]] = int(ruta[9])
            else:
                paises[ruta[2]] += int(ruta[9])
    for valor in paises:
        pais_ordenado.append([valor, paises[valor]])      
    pais_ordenado.sort(reverse=True, key= lambda mayor: mayor [1])
    df=pd.DataFrame(pais_ordenado, columns =["País","Total"])
    return (print(df))


#%%
#Brindamos la orden para obtener la informacion y hacer el analisis realizando
#listas y dentro de ellas incluir las funciones creadas.    


print("\n TOP 10 RUTAS DE EXPORTACIÓN \n")
rutasexp = rutas("Exports")
print("\n TOP 10 RUTAS DE IMPORTACIÓN \n")
rutasimp = rutas("Imports")

print("\n EXPORTACIONES | MEDIOS DE TRANSPORTE UTILIZADOS \n")
medios_exports=tipo_transporte("Exports")
print("\n IMPORTACIONES | MEDIOS DE TRANSPORTE UTILIZADOS \n")
medios_imports=tipo_transportei("Imports")

print("\n PAISES EXPORTADORES \n")
exportaciones=rutas_pais("Exports")
print("\n PAISES IMPORTADORES\n")
importacionrutas=rutas_pais("Imports")