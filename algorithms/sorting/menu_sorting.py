import os
import utils.lectura_datos as leer
import algorithms.sorting.insertion_sort as ins
import algorithms.sorting.merge_sort as merge

def menu_sorting():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Algoritmos de ordenación: \n")
		print("1)Insertion sort (ascendente)")
		print("2)Insertion sort (descendente)")
		print("3)Merge sort")
		print("q)Regresar al menu anterior")

		opcion = str(input("¿Qué algoritmo desea utilizar?: "))

		if(opcion == '1'):
			arr = leer.arreglo("Insertion sort (ascendente)")
			print("El arreglo a ordenar es:")
			print(arr)
			arr_sort = ins.insertion_sort_increasing(arr)
			print("El arreglo ordenado es:")
			print(arr_sort)
			input("Presione enter para continuar...")

		elif(opcion == '2'):
			arr = leer.arreglo("Insertion sort (descendente)")
			print("El arreglo a ordenar es:")
			print(arr)
			arr_sort = ins.insertion_sort_decreasing(arr)
			print("El arreglo ordenado es:")
			print(arr_sort)
			input("Presione enter para continuar...")

		elif(opcion == '3'):
			arr = leer.arreglo("Merge Sort")
			print("El arreglo a ordenar es:")
			print(arr)
			arr_sort = merge.merge_sort(arr, 0, len(arr)-1)
			print("El arreglo ordenado es:")
			print(arr_sort)
			input("Presione enter para continuar...")

		elif(opcion == 'q'):
			print("Saliendo...")
			break
		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar")