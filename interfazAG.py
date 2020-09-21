from tkinter import * 
from functools import partial
from itertools import product

## moduloAG.py debe de estar en la misma carpeta que interfazAG.py ###########
import moduloAG as ag


##############################################################################
						# CONFIGURACION DE PARAMETROS:
##############################################################################

# Mapa a mostrar al inicio de programa
mapa = [
    [1,1,1,1,1,1,1,1,1,1],
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

# Punto inicio
puntoInicio=[1,1]
# Punto final
puntoFinal=[8,8]
# Numero de generaciones
numGen=100
# Tamanio poblacion
tmnPob=60 
# Longitud de cromosomas o individuos
tmnInd=80
# Probabilidad de cruza
pCruza=0.9
# Probabilidad de mutacion
pMutacion=0.4



############################################################################

############################################################################
#								Interfaz grafica						   #
############################################################################

root = Tk() 

mapaVars=[]
for i in range(len(mapa)):
	mapaVars.append([])

for x in range(10): 
    for y in range(10):  
        mapaVars[x].append(IntVar())
        mapaVars[x][y].set(mapa[x][y])

mapaVars[puntoInicio[0]][puntoInicio[1]].set(4)
mapaVars[puntoFinal[0]][puntoFinal[1]].set(5)

boole=IntVar()
boole.set(0)

def cambiaMapa(): # Se activa al presionar "Calcular ruta"
	if(boole.get()==0):
		boole.set(1)
	else:
		boole.set(0)

frame=Frame(root) 
frameEsp=Frame(root)
frameRes=Frame(root) #
Grid.rowconfigure(root, 0, weight=1) 
Grid.columnconfigure(root, 0, weight=1) 
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1) #
frame.grid(row=0, column=0, sticky=N+S+E+W) 

frameEsp.grid(row=0, column=1, sticky=N+S+E+W)
gridEsp=Frame(frameEsp)
gridEsp.grid(sticky=N+S+E+W, column=0, row=0, columnspan=1) 
Grid.rowconfigure(frameEsp, 0, weight=1) 
Grid.columnconfigure(frameEsp, 0, weight=1)
btn3 = Button(frameEsp, text="Calcular Ruta",command=cambiaMapa) 
btn3.grid(column=0, row=0, sticky=E+W)
Grid.columnconfigure(frameEsp, 0, weight=1)
Grid.rowconfigure(frameRes, 0, weight=1)  

frameRes.grid(row=0, column=2, sticky=N+S+E+W) #

gridRes=Frame(frameRes) 
gridRes.grid(sticky=N+S+E+W, column=0, row=0, columnspan=1) 
Grid.rowconfigure(frameRes, 0, weight=1) 
Grid.columnconfigure(frameRes, 0, weight=1)

botones2=[]
for i in range(len(mapa)):
	botones2.append([])

for x in range(10): 
    for y in range(10):  
        botones2[x].append(Button(frameRes))

for x in range(10): 
    for y in range(10): 
     botones2[x][y].grid(column=x, row=y, sticky=N+S+E+W)

for x in range(10): 
    Grid.columnconfigure(frameRes, x, weight=1) 

for y in range(10): 
    Grid.rowconfigure(frameRes, y, weight=1) 


grid=Frame(frame) 
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=1) 
Grid.rowconfigure(frame, 7, weight=1) 
Grid.columnconfigure(frame, 0, weight=1) 

def cambia(x1,y1): #funcion aumentar
	if (mapaVars[x1][y1].get()==1):	
		mapaVars[x1][y1].set(0)
		botones[x1][y1].config(bg="white")
	elif(mapaVars[x1][y1].get()==0):
		mapaVars[x1][y1].set(1)
		botones[x1][y1].config(bg="black")
	else:
		botones[x1][y1].config(bg="yellow")

def cambia2(c,d): #funcion aumentar
	bname = (botones[c][d])
	cambia(c,d)


botones=[]
for i in range(len(mapa)):
	botones.append([])

for x in range(10): 
    for y in range(10):  
        botones[x].append(Button(frame))


for x in range(10): 
    for y in range(10): 
        botones[x][y].grid(column=x, row=y, sticky=N+S+E+W) 

for x in range(10): 
    Grid.columnconfigure(frame, x, weight=1) 

for y in range(10): 
    Grid.rowconfigure(frame, y, weight=1) 

a=IntVar()
b=IntVar()
a.set(0)

# Coloreo al inicio del programa de figura izquierda, mapa inicial
for lineBoton in botones:
	b.set(0)
	for boton in lineBoton:
		#print(a.get())
		boton.config(command=partial(cambia2, a.get(),b.get()))
		if (mapaVars[a.get()][b.get()].get()==0):	
			botones[a.get()][b.get()].config(bg="white")
		elif (mapaVars[a.get()][b.get()].get()==1):
			botones[a.get()][b.get()].config(bg="black")
		elif (mapaVars[a.get()][b.get()].get()==5):
			botones[a.get()][b.get()].config(bg="red")
		elif (mapaVars[a.get()][b.get()].get()==4):
			botones[a.get()][b.get()].config(bg="yellow")		
		b.set(b.get()+1)
	a.set(a.get()+1)


#########################################################################################################################




#########################################################################################################################

######### 						ALGORITMO GENETICO																#########

#########################################################################################################################


def cambiaMapa1():
	
	# Se obtiene configuracion de mapa 
	for x in range(10): 
	    for y in range(10):  
	        mapa[x][y]=mapaVars[x][y].get()

	# Pasamos valores al moduloAG
	ag.data5=mapa
	ag.longitudMapa=len(mapa)
	ag.pCruza=pCruza
	ag.pMutacion=pMutacion
	ag.coorFin=puntoFinal
	ag.coorInicio=puntoInicio


	######    AG      ######

	#Crea Poblacion Inicial
	poblacion = ag.creaPob(tmnPob, tmnInd)

	# Mapeo genotipo a fenotipo: decodificacion
	poblacionDecodificada = ag.decodifica(poblacion)

	# Evalua poblacion
	valoresPoblacion = ag.evaluaPob(poblacionDecodificada,puntoInicio)
	listaOrden=ag.orden(valoresPoblacion.copy())
	poblacionOriginal=poblacion.copy()
	poblacionOrdenada=ag.cambiaOrden(poblacionOriginal,listaOrden)

	promedios=[]
	minimos=[] # Guarda el costo del mejor individuo de cada generacion, para graficar
	
	# Ciclo de evolucion
	generaciones = 1;
	while generaciones <= numGen:
	    print("===================== Generacion",generaciones,"===================")
	    poblacionDecodificada1 = ag.decodifica(poblacionOrdenada.copy())

	    costosP=ag.evaluaPob(poblacionDecodificada1,puntoInicio)
	    #print(costosP)
	    #promedio=sum(costosP)/(len(costosP))---------------------------
	    #promedios.append(promedio)-----------------------------------
	    #print("Promedio: "+str(promedio))
	    minimo=min(costosP)#-------------------------------------------------
	    minimos.append(minimo)#---------------------------------- Agrega minimo de generacion
	    #print("Minimo: "+str(minimo))

	    
	    # Realiza seleccion
	    ordenSeleccion=ag.seleccionRuleta(poblacionOrdenada) 
	    poblacionSeleccionada=ag.cambiaOrden(poblacionOrdenada,ordenSeleccion)
	    #nuevaPob = seleccionRuleta(poblacion, valoresPob);
	    
	    # Aplica operador de cruzamiento
	    poblaCruz1=poblacionSeleccionada.copy() #
	    poblacionCruzada=ag.cruzaXPunto(poblaCruz1)
	    #nuevaPob = cruzaXPunto(nuevaPob, pCruza);

	    # Aplica operador de mutacion
	    #nuevaPob = muta(nuevaPob, pMutacion);
	    poblaMuta1=poblacionCruzada.copy() #
	    poblacionEvolucionada=ag.muta(poblaMuta1)

	    # Mapeo genotipo a fenotipo: decodificacion
	    poblacionDecodificada = ag.decodifica(poblacionEvolucionada)

	    # Evalua poblacion
	    #valoresPob = evaluaPob(pobDecodificada);
	    # Ordenar individuos
	    valoresPoblacion = ag.evaluaPob(poblacionDecodificada,puntoInicio)
	    #print(valoresPoblacion)
	    listaOrden=ag.orden(valoresPoblacion.copy())
	    poblacionOriginal=poblacionEvolucionada.copy()
	    poblacionOrdenada=ag.cambiaOrden(poblacionEvolucionada,listaOrden)
	    
	    # Asigna nueva poblacion
	    #poblacion = nuevaPob;

	    # Incrementa contador de generaciones
	    generaciones = generaciones+1

	    ag.llegaron=[] # Reinicia lista de individuos de la generacion que llegarona  meta
	    
	#print("promedios")
	#print(promedios)
	print("minimos")
	print(minimos)


	# Decodifica poblacion obtenida final
	poblacionDecodificada3 = ag.decodifica(poblacionOrdenada.copy())


	valoresPoblacion3 = ag.evaluaPob(poblacionDecodificada3,puntoInicio)
	#print(valoresPoblacion3)
	#print(poblacionDecodificada[-1])
	ag.sumaInicio(puntoInicio,poblacionDecodificada[0])

	
	# Si se llega a una solucion
	if(len(ag.llegaron)>0):
		#print(len(ag.llegaron))
		res=ag.sumaInicio([puntoInicio[0],puntoInicio[1]],ag.llegaron[0]) # Se obtiene las coordenadas del mejor individuo despues de las generaciones
		for gen in res:
		    #print (gen)
		    # Colocamos 3 en cada casilla de ruta
		    mapa[gen[0]][gen[1]]=3

		mapa[puntoInicio[0]][puntoInicio[1]]=4
		mapa[puntoFinal[0]][puntoFinal[1]]=5

		# Colorea mapa derecha
		for x in range(10): 
		    for y in range(10):  
		        if(mapa[x][y]==0):
		        	botones2[x][y].config(bg="white")
		        elif(mapa[x][y]==1):
		        	botones2[x][y].config(bg="black")
		        elif(mapa[x][y]==4):
		        	botones2[x][y].config(bg="yellow")
		        elif(mapa[x][y]==5):
		        	botones2[x][y].config(bg="green")
		        else:
		        	botones2[x][y].config(bg="green")
	else:
		print("\n\nPRESIONA DE NUEVO EL BOTON DE CALCULAR RUTA, NO SE LOGRO LLEGAR A LA META :C")
		print("O talvez el mapa esta muy complejo")


	
	#print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
	#print(mapa)


btn3.config(command=cambiaMapa1)



root.mainloop() 
