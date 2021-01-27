import numpy as np

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