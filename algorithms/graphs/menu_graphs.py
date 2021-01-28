import os
import utils.lectura_datos as leer
import algorithms.graphs.bfs as bfs
import algorithms.graphs.dfs as dfs
import algorithms.graphs.bellman_ford as bf


def menu_graphs():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Algoritmos para gráficas: \n")
		print("1) BFS")
		print("2) Camino más corto usando BFS")
		print("3) DFS")
		print("4) Bellman-Ford")

		print("q)Regresar al menu anterior")

		opcion = str(input("¿Qué algoritmo desea utilizar?: "))

		if(opcion == '1'):
			G = leer.grafica("el algoritmo BFS")
			s = leer.numero_entero("para indicar la fuente de la gráfica")
			d, predecesores =  bfs.bfs(G, s - 1)
			print("El vector de distancias es: ")
			print(d)
			print("El vector de predecesores es: ")
			print(predecesores)
			input("Presione enter para continuar...")

		elif(opcion == '2'):
			G = leer.grafica("el camino más corto usando bfs")
			s = leer.numero_entero("para indicar la fuente de la gráfica")
			v = leer.numero_entero("para indicar el nodo destino de la gráfica")
			d, predecesores =  bfs.bfs(G, s)
			print("El camino más corto de " + str(s) + " a " + str(v) + " es: ")
			bfs.print_path(predecesores, s, v)
			input("\nPresione enter para continuar...")			

		elif(opcion == '3'):
			G = leer.grafica("el algoritmo DFS")
			predecesores, d, f  =  dfs.dfs(G)
			print("El vector de predecesores es: ")
			print(predecesores)
			print("El vector discovery time es: ")
			print(d)
			print("El vector finishing time es: ")
			print(f)
			input("Presione enter para continuar...")

		elif(opcion == '4'):
			G = leer.grafica("el algoritmo Bellman-Ford")
			w = leer.pesos_grafica(G)
			s = leer.numero_entero("para indicar la fuente de la gráfica")
			if bf.bellman_ford(G, w, s):
				print("No hay ciclos negativos en la gráfica")
			else:
				print("Hay ciclos negativos en la gráfica")
			input("Presione enter para continuar...")

		elif(opcion == 'q'):
			print("Saliendo...")
			break

		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar")