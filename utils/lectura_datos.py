import numpy as np

from graph import Graph, Graph3D

def numero_entero(cadena = "Deseado"):
	return int(input("Ingrese el número " + cadena + ": "))

def arreglo(cadena = "el algoritmo seleccionado"):
	print("Ingresando arreglo para " + cadena + ": ")
	lon = int(input("¿Qué longitud tiene el arreglo?: "))
	arr = []
	
	for i in range(0, lon):
		valor = float(input("Ingrese el valor del arreglo en la posición ["+ str(i) + "]: "))
		arr.append(valor)

	return arr

def arreglo_int(cadena = "el algoritmo seleccionado"):
	print("Ingresando arreglo para " + cadena + ": ")
	lon = int(input("¿Qué longitud tiene el arreglo?: "))
	arr = []
	
	for i in range(0, lon):
		valor = int(input("Ingrese el valor del arreglo en la posición ["+ str(i) + "]: "))
		arr.append(valor)

	return arr

def arreglo_digitos(cadena = "el algoritmo seleccionado"):
	print("Ingresando arreglo para " + cadena + ": ")
	lon = int(input("¿Qué longitud tiene el arreglo?: "))
	arr = []
	
	for i in range(0, lon):
		valor = str(input("Ingrese el valor del arreglo en la posición ["+ str(i) + "]: "))
		arr.append(valor)
	
	mat = []

	for i in range(0, len(arr)):
		mat.append([int(j) for j in arr[i]])

	return np.array(mat).T.tolist()


def matriz(cadena = "el algoritmo selecionado"):
	print("Ingresando matriz para " + cadena + ": ")
	n = int(input("Ingrese el número de renglones: "))
	m = int(input("Ingrese el número de columnas: "))

	mat = []

	for i in range(0, n):
		ren = []
		for j in range(0, m):
			valor = float(input("Ingrese el valor de la matriz en ["+ str(i) +"][" + str(j) + "]: "))
			ren.append(valor)
		mat.append(ren)

	return mat

def grafica(cadena = "el algoritmo seleccionado"):
	print("Ingresando la gráfica para " + cadena + ": ")
	n = numero_entero("de nodos")
	g = [[] for i in range(0,n)]

	for i, vertex in enumerate(g):
		adj = numero_entero("de nodos a los que es adyacente el nodo " + str(i))
		for j in range(0, adj):
			adj_vertex = numero_entero("de nodo al que es adyacente el nodo " + str(i))
			vertex.append(adj_vertex)

	return g

def pesos_grafica(G):
	print("Ingresando pesos de la gráfica")
	w = []
	for i, u in enumerate(G):
		pesos = []
		for v in u:
			peso = int(input("Ingrese el peso para la arista que va del nodo " + str(i) + " al nodo " + str(v) + ": "))
			pesos.append(peso)
		w.append(pesos)

	return w

#G = [[1, 3], [2, 3, 4], [], [2, 4], [2]]
#w = [[6, 7], [5, 8, 4], [], [3, 9], [7]]
#print(pesos_grafica(G))
