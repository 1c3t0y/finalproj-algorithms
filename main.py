import os

from algorithms.numeric.menu_numeric import menu_numeric

def portada():
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
		opcion = str(input("¿Qué tipo de algoritmo desea utilizar?"))

		if(opcion == '1'):
			menu_numeric()



def main():
	portada()
	input("Presione enter para continuar")
	menu_principal()

if __name__ == "__main__":
	main()


