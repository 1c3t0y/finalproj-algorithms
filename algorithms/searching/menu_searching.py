import os
import utils.lectura_datos as leer
import algorithms.searching.binary_search as bs
import algorithms.searching.linear_search as ls

def menu_searching():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Algoritmos de búsqueda: \n")
		print("1) Binary Search (recursivo)")
		print("2) Linear Search")
		print("q) Regresar al menu anterior")

		opcion = str(input("¿Qué algoritmo desea utilizar?: "))

		if(opcion == '1'):
			numero = leer.numero_entero("a buscar mediante Binary Search")
			arr = leer.arreglo("donde buscar mediante Binary Search")
			pos = bs.binary_search_r(arr, numero, 0, len(arr) - 1)
			print("El número " + str(numero) + " se encuentra en la posición: " + str(pos))			
			input("Presione enter para continuar...")

		elif(opcion == '2'):
			numero = leer.numero_entero("a buscar mediante Linear Search")
			arr = leer.arreglo("donde buscar mediante Linear Search")
			pos = ls.linear_search(arr, numero)
			print("El número " + str(numero) + " se encuentra en la posición: " + str(pos))			
			input("Presione enter para continuar...")

		elif(opcion == 'q'):
			print("Saliendo...")
			break
		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar")