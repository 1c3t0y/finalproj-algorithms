import os
import utils.lectura_datos as leer
import algorithms.greedy.activity_selector as gas

def menu_greedy():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Algoritmos greedy: \n")
		print("1)Selección de actividades recursivo")
		print("2)Selección de actividades greedy")		
		print("q)Regresar al menu anterior")

		opcion = str(input("¿Qué algoritmo desea utilizar?: "))

		if(opcion == '1'):
			s = leer.arreglo_int("los inicios de las actividades")
			f = leer.arreglo_int("los finales de las actividades")
			n = len(s)
			actividades = gas.activity_selector_r([0] + s, [0] + f, 0, n)
			print(actividades)
			input("Presione enter para continuar...")

		elif(opcion == '2'):
			s = leer.arreglo_int("los inicios de las actividades")
			f = leer.arreglo_int("los finales de las actividades")
			actividades = gas.activity_selector_i([0] + s, [0] + f)
			print(actividades)
			input("Presione enter para continuar...")

		elif(opcion == 'q'):
			print("Saliendo...")
			break

		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar")