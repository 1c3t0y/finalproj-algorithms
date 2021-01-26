import os
import utils.lectura_datos as leer
import algorithms.numeric.fibonacci as fib
import algorithms.numeric.factorial as fac

def menu_numeric():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Algoritmos numéricos: \n")
		print("1)Factorial de un número (recursivo)")
		print("2)Factorial de un número (iterativo)")
		print("3)i-ésimo número de Fibonacci (recursivo)")
		print("4)i-ésimo número de Fibonacci (iterativo)")
		print("q)Regresar al menu anterior")

		opcion = str(input("¿Qué algoritmo desea utilizar?: "))

		if(opcion == '1'):
			numero = leer.numero_entero("Del que desea obtener su factorial")
			res = fac.factorial_r(numero)
			print("El factorial de "+ str(numero) + " es: " + str(res))
			input("Presione enter para continuar...")

		elif(opcion == '2'):
			numero = leer.numero_entero("Del que desea obtener su factorial")
			res = fac.factorial_i(numero)
			print("El factorial de "+ str(numero) + " es: " + str(res))
			input("Presione enter para continuar...")
		
		elif(opcion == '3'):
			numero = leer.numero_entero("de fibonacci que desea obtener")
			res = fib.fibonacci_r(numero)
			print("El "+ str(numero) + " de fibonacci es: " + str(res))
			input("Presione enter para continuar...")

		elif(opcion == '4'):
			numero = leer.numero_entero("de fibonacci que desea obtener")
			res = fib.fibonacci_i(numero)
			print("El "+ str(numero) + " de fibonacci es: " + str(res))
			input("Presione enter para continuar...")

		elif(opcion == 'q'):
			print("Saliendo...")
			break
		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar")