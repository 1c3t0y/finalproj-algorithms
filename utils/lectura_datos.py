def numero_entero(cadena = "Deseado"):
	return int(input("Ingrese el número " + cadena + ": "))

def arreglo(cadena = "el algoritmo seleccionado"):
	print("Ingresando arreglo para " + cadena + ": ")
	len = int(input("¿Qué longitud tiene el arreglo?: "))
	arr = []
	
	for i in range(0, len):
		valor = float(input("Ingrese el valor del arreglo en la posición ["+ str(i) + "]: "))
		arr.append(valor)

	return arr

