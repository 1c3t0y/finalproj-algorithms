import os

from algorithms.numeric.menu_numeric import menu_numeric
from algorithms.sorting.menu_sorting import menu_sorting
from algorithms.searching.menu_searching import menu_searching
from algorithms.backtracking.menu_backtracking import menu_backtracking
from algorithms.greedy.menu_greedy import menu_greedy
from algorithms.dynamic.menu_dynamic import menu_dynamic
from algorithms.graphs.menu_graphs import menu_graphs

def portada():
	os.system("clear")
	print("Universidad Nacional Autónoma de México")
	print("Facultad de Estudios Superiores Acatlán")
	print("Matemáticas Aplicadas y Computación")
	print("Proyecto Final de Análisis de algoritmos")
	print("Alumno: Mejía Maldonado José Fernando")
	print("Profesor: Rubio Montiel Christian")

def menu_principal():
	opcion = '0'
	while(opcion != 'q'):
		os.system("clear")
		print("Menu principal\n\n")
		print("1) Numérico")
		print("2) Ordenamiento")
		print("3) Búsqueda")
		print("4) Backtracking")
		print("5) Greedy")
		print("6) Programación dinámica")
		print("7) Gráficas")
		print("q) Salir")
		opcion = str(input("¿Qué tipo de algoritmo desea utilizar?: "))

		if(opcion == '1'):
			menu_numeric()

		elif(opcion == '2'):
			menu_sorting()

		elif(opcion == '3'):
			menu_searching()

		elif(opcion == '4'):
			menu_backtracking()

		elif(opcion == '5'):
			menu_greedy()

		elif(opcion == '6'):
			menu_dynamic()

		elif(opcion == '7'):
			menu_graphs()

		elif(opcion == 'q'):
			print("Saliendo...")
			os.system("clear")
			break
		else:
			print("Opcion incorrecta, intente de de nuevo")
			input("Presione enter para continuar...")



def main():
	portada()
	input("Presione enter para continuar...")
	menu_principal()

if __name__ == "__main__":
	main()


