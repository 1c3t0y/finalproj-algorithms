import os
import utils.lectura_datos as leer
import algorithms.dynamic.matrix_multiply as mm
import algorithms.dynamic.matrix_chain_order as mco
import algorithms.dynamic.cut_rod as cr
import algorithms.dynamic.lcs as lcs

def menu_dynamic():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Algoritmos de programación dinámica: \n")
		print("1) Multiplicación de dos matrices")	
		print("2) Matrix chain order")
		print("3) Rod-cutting")
		print("4) LCS")
		print("q) Regresar al menu anterior")

		opcion = str(input("¿Qué algoritmo desea utilizar?: "))

		if(opcion == '1'):
			A = leer.matriz("multiplicar")
			B = leer.matriz("multiplicar")
			res = mm.matrix_multiply(A, B)
			print("La matriz resultante es: ")
			print(res)
			input("Presione enter para continuar...")

		elif (opcion == '2'):
			p = leer.arreglo_int("Matrix chain order")
			m, s = mco.matrix_chain_order(p)
			print("La matriz de costos es: ")
			print(m)
			print("\nEl orden de multiplicación óptimo de matrices es: ")
			mco.print_optimal_parens(s, 1, len(p) - 1)
			print("")
			input("Presione enter para continuar...")

		elif (opcion == '3'):
			p = leer.arreglo_int("lista de precios para Rod-cutting")
			n = leer.numero_entero("longitud para Rod-cutting")
			costo = cr.cut_rod(p, n)
			print("El costo mínimo con longitud " + str(n) + "es: " + str(costo))
			input("Presione enter para continuar...")

		elif (opcion == '4'):
			X = input("Ingrese la cadena 1 para obtener la LCS")
			Y = input("Ingrese la cadena 1 para obtener la LCS")
			c, b = lcs_length(X, Y)
			print("La LCS es: ")
			print_lcs(b, X, len(X), len(Y))
			print("")
			input("Presione enter para continuar...")

		elif(opcion == 'q'):
			print("Saliendo...")
			break

		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar")