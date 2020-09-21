import random
import math
import numpy as np

###################################################################################
#       Modulo Algoritmo Genetico por: Francisco Javier Duran Lopez               #
#                            15/06/2020                                           #
###################################################################################


longitudMapa=10
pCruza=0.9
pMutacion=0.3
coorFin=[8,8]
coorInicio=[1,1]
llegaron=[]
'''
data5 = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,1,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

data5 = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]


data5 = [
    [1,1,1,1,1,1,1,1],
    [1,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
]
'''
data5 = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

def decimalToBinary(n): # Pasar decimal a binario 
    return bin(n).replace("0b", "")  

def toDecimal(binary, i = 0): # Binario a decimal  
    n = len(binary)  
    if (i == n - 1) : 
        return int(binary[i]) - 0 
    return (((int(binary[i]) - 0) << (n - i - 1)) + 
                        toDecimal(binary, i + 1))

def creaNum(): #Crea gen aleatorio ej. "1011"
    dec = random.randint(0,7)
    if dec<2:
        num='00'+decimalToBinary(dec)
    elif dec<4 and dec>1:
        num='0'+decimalToBinary(dec)
    else:
        num=decimalToBinary(dec)
    ran=str(random.randint(0,1))
    return num+ran


def creaPob(tmnPob,tmnInd): # crea poblacion 
    poblacion=[]
    for i in range(tmnPob):
        newString=[]
        for j in range(tmnInd):
            newString.append(creaNum())
        poblacion.append(newString)
    #print(poblacion)  
    return poblacion

# a=creaPob(10,20) Se debe crear poblacion

def avanceGen(gen): # Obtenemos el avance en coordenadas [avanze en x,avanze en y]
    coor=gen[:-1]
    if(gen[-1]=='1'):  # Si hay avance 
        if (toDecimal(coor)==0):
            return [1,0];
        elif (toDecimal(coor)==1):
            return [1,1];
        elif (toDecimal(coor)==2):
            return [0,1];
        elif (toDecimal(coor)==3):
            return [-1,1];
        elif (toDecimal(coor)==4):
            return [-1,0];
        elif (toDecimal(coor)==5):
            return [-1,-1];
        elif (toDecimal(coor)==6):
            return [0,-1];
        elif (toDecimal(coor)==7):
            return [1,-1];
        else:
            return [0,0];
    else:
        return [0,0]

def decodifica(pob): # Decodifica poblacion
    newPob=[]
    for line in pob:
        linepuntos=[]
        for punto in line:
            linepuntos.append(avanceGen(punto))
        newPob.append(linepuntos)
    return newPob
      
# decoded=decodifica(a)  Se decodifica

def costoNextGen(primer,segundo): # Costo de genes consecutivos
    d=math.sqrt((segundo[0]-primer[0])**2+(segundo[1]-primer[1])**2)
    valorMapa=data5[segundo[0]][segundo[1]]
    peso=0
    if (valorMapa==0):
        if (segundo==coorFin): # Si es punto final
            peso=-0.95
        else:
            peso=0
    elif(valorMapa==1): # Si es un obstaculo
        peso=300
    #print("peso de mapa -> "+str(valorMapa))
    #print(peso)
    #print("distancia-> "+str(d))
    costo=d*(1+peso)
    #print("total-> "+str(costo))
    return costo

def sumaInicio(coorInicio,lista): # Pasa genes a coordenadas reales
    newCoords=[]
    primerPunto=coorInicio # [x,y]
    i=0
    for gen in lista:
        if(len(newCoords)<len(lista)):
            newPosiblePoint=[gen[0]+primerPunto[0],gen[1]+primerPunto[1]]
            if((newPosiblePoint[0]>-1 and newPosiblePoint[0]<longitudMapa) and (newPosiblePoint[1]>-1 and newPosiblePoint[1]<longitudMapa)):
                # Si el punto existe en el mapa
                if(newPosiblePoint==coorFin):
                    #print("SE LLEGOOO")
                    for k in range(i,len(lista)):
                        newCoords.append(newPosiblePoint)
                    llegaron.append(lista)
                else:
                    newCoords.append(newPosiblePoint)
                    primerPunto=newPosiblePoint
            else:
                # Si no existe se deja su punto anterior
                newCoords.append(primerPunto)
                primerPunto=primerPunto    
            i=i+1 
    #print(lista)
    #print(newCoords)
    return newCoords

def funcObjetivo(coorInicio,lineCoor): # Costo de un individuo (Coordenadas de Inicio,Linea de coordenadas (individuo) )
    # pasar todas las coordenadas sumando inicio
    coords=sumaInicio(coorInicio,lineCoor)
    # Obtener costo de cada individuo
    costos=[]
    total=0
    #print(len(lineCoor))
    for i in range(len(lineCoor)-1):
        #print(i)
        costo=costoNextGen(coords[i],coords[i+1])
        costos.append(costo)
        total=total+costo
    total=total+costoNextGen(coorInicio,coords[0])#se suma primer avance

    d2=math.sqrt((coorFin[0]-coords[0][0])**2+(coorFin[1]-coords[0][1])**2) # DIstancia del ultimo punto a la meta
    d2=d2*100
    return total +d2

def evaluaPob(poblacion,puntoInicio):
    costosIndividuos=[]
    i=0
    for individuo in poblacion:
        i=i+1
        costoUnIndividuo=funcObjetivo(puntoInicio,individuo)
        costosIndividuos.append(costoUnIndividuo)
    return costosIndividuos
        

def orden(lista): # Regresa los indices de como deben estar ordenados de menor a mayor costo
    n=math.ceil(max(lista))+1
    orden=[]
    for costo in lista:
        number=lista.index(min(lista))
        orden.append(number)
        lista[number]=n
    return orden
        

#listaOrden=orden(listaDeCostos.copy())

#poblacionOriginal=a.copy()
#poblacionOriginal

def cambiaOrden(poblacionACambiar,ordenNuevo): # Regresa la lista de individuos en orden 
    newPob=[]
    #print(poblacionACambiar)
    for i in ordenNuevo:
        newPob.append(poblacionACambiar[i])
    #print(newPob)
    return newPob
    
#poblacionOrdenada=cambiaOrden(poblacionOriginal,listaOrden)

def seleccionRuleta(poblacionOrd): # Obtiene los indices de los individuos seleccionados por el metodo de Ruleta
    decodedPrueba=decodifica(poblacionOrd)
    listaDeCostosPrueba=evaluaPob(decodedPrueba,coorInicio)
    arrayLista= np.array(listaDeCostosPrueba)
    probabilidades=arrayLista/sum(arrayLista)
    probabilidadesAcumuladas=np.cumsum(probabilidades)

    elegidos=[]
    for i in range(len(poblacionOrd)):
        num=random.random()
        j=0
        while(probabilidadesAcumuladas[j]<num):
            j+=1
        camb=len(poblacionOrd)-1-j # ul-14/06  
        elegidos.append(camb)
        

        #aux=find(probabilidades>=num)
    #print(elegidos)
    # Se eligen directamente los mejores cuatro individuos de cada generacion
    elegidos[0]=0
    elegidos[1]=1
    elegidos[3]=3
    elegidos[4]=4
    return elegidos

#ordenSeleccion=seleccionRuleta(poblacionOrdenada) 
#poblacionSeleccionada=cambiaOrden(poblacionOrdenada,ordenSeleccion)

def cruzaXPunto(poblacionACruzar): # Obtiene los indices de los individuos seleccionados
    # Se necesitan obtener pares de individuos
    numACruzar=len(poblacionACruzar)
    par=numACruzar%2
    # Si no es par el ultimo no se cruza
    cruzados=[]
    if(par==0):
        #Si es par
        numParejas=numACruzar/2
    else:
        numParejas=(numACruzar-1)/2
        cruzados.append(poblacionACruzar[-1]) #Si es impar el num de individuos, se agrega el ultimo
    
    for i in range(0,int(numParejas*2),2): 
        #print(i)
        proba=random.random()
        #print("Proba->"+str(proba))
        ind1=poblacionACruzar[i]
        ind2=poblacionACruzar[i+1]
        
        if(proba<=pCruza): 
            # Si hay cruza
            corte= random.randint(0,len(poblacionACruzar[0])-1)# rango ->[0,numGenes]
            #print("corte->"+str(corte))
            ind_nuevo1=ind1[0:corte]+ind2[corte:]
            ind_nuevo2=ind2[0:corte]+ind1[corte:]
        else:
            ind_nuevo1=ind1
            ind_nuevo2=ind2
            
        cruzados.append(ind_nuevo1)
        cruzados.append(ind_nuevo2)
    return cruzados

#pCruza=0.9

#poblaCruz1=poblacionSeleccionada.copy() #
#poblacionCruzada=cruzaXPunto(poblaCruz1)

def muta(poblacionAMutar): # Obtiene los indices de los individuos seleccionados
    mutados=poblacionAMutar.copy()
    
    for i in range(0,len(mutados)): 
        #print(i)
        proba=random.random()
        #print(proba)
        indM=mutados[i]
        if(proba<=pMutacion): 
            # Si hay mutacion
            numGenAMutar=random.randint(0,len(indM)-1)
            #print("en"+str(numGenAMutar))
            nuevoGen=creaNum()
            #print("nuevGen"+str(nuevoGen))
            indM[numGenAMutar]=nuevoGen
            mutados[i]=indM
        
        # Ojo aqui cambia el objeto que mando
    return mutados

#pMutacion=0.3
#poblaMuta1=poblacionCruzada.copy() #
#poblacionMutada=muta(poblaMuta1)