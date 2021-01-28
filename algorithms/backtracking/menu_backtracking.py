import os
import utils.lectura_datos as leer
import algorithms.backtracking.n_queens as nq
import algorithms.backtracking.subset_sum as ss
import algorithms.backtracking.construct_subset as cs

def menu_backtracking():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Algoritmos de backtracking: \n")
		print("1) N reinas")
		print("2) Subset sum")
		print("3) Construct Subset Sum")
		print("q) Regresar al menu anterior")

		opcion = str(input("¿Qué algoritmo desea utilizar?: "))

		if(opcion == '1'):
			numero = leer.numero_entero("que indica el número de renglones del tablero de ajedrez")
			Q = [0 for i in range(0, numero)]
			print("Todas las soluciones para el problema de las " + str(numero) + " reinas son: ")
			nq.n_queens_r(Q, 0)
			input("Presione enter para continuar...")

		elif(opcion == '2'):
			conjunto = leer.arreglo_int("Subset Sum")
			numero = leer.numero_entero("el número del cual desea saber si hay subconjunto que lo sume")
			if ss.subset_sum(conjunto, numero):
				print("Sí hay un subconjunto cuya suma de: " + str(numero))
			else:
				print("No hay un subconjunto cuya suma de: " + str(numero))
			input("Presione enter para continuar...")

		elif(opcion == '3'):
			conjunto = leer.arreglo_int("Construct Subset Sum")
			numero = leer.numero_entero("el número del cual desea obtener un subconjunto que lo sume")
			subconjunto = cs.construct_subset(conjunto, numero)
			if subconjunto != None:
				print("El subconjunto que da como suma "+ str(numero) + " es:")
				print(subconjunto)
			else:
				print("No hay un subconjunto cuya suma de: " + str(numero))
			input("Presione enter para continuar...")

		elif(opcion == 'q'):
			print("Saliendo...")
			break

		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar")