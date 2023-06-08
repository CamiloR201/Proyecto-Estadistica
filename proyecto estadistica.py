import matplotlib.pyplot as plt
import csv
import statistics

# Función para cargar datos desde un archivo CSV
def cargar_datos_csv(archivo):
    datos = []
    with open(archivo, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i, linea in enumerate(reader):
            if i > 0:  # Omitir la primera línea
                for dato in linea:
                    dato = dato.strip()
                    if dato:
                        datos.append(float(dato))
    return datos


# Función para cargar datos desde un archivo TXT (un dato por línea)
def cargar_datos_txt(archivo):
    datos = []
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if linea:
                datos.append(float(linea))
    return datos

# Función para generar un histograma
def generar_histograma(datos):
    plt.hist(datos, bins='auto')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

# Función para generar un gráfico de dispersión
def generar_grafico_dispercion(datos):
    indices = list(range(1, len(datos) + 1))
    plt.scatter(indices, datos)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfico de Dispersión')
    plt.show()

# Función para generar un diagrama de círculo (pie chart)
def generar_diagrama_circulo(datos):
    conteo = {}
    for dato in datos:
        if dato in conteo:
            conteo[dato] += 1
        else:
            conteo[dato] = 1

    etiquetas = [str(dato) + ' (' + str(conteo[dato]) + ')' for dato in conteo]
    plt.pie(conteo.values(), labels=etiquetas, autopct='%1.1f%%')
    plt.title('Diagrama de Círculo')
    plt.show()

# Función para calcular estadísticas
def calcular_estadisticas(datos):
    resultados = {}
    resultados['Cantidad de datos'] = len(datos)
    resultados['Suma'] = sum(datos)
    resultados['Media'] = statistics.mean(datos)
    resultados['Mediana'] = statistics.median(datos)
    resultados['Desviación estándar'] = statistics.stdev(datos)
    resultados['Varianza'] = statistics.variance(datos)
    return resultados

# Función principal para el menú de opciones
def menu_principal():
    datos = []
    while True:
        print("------ Aplicativo Estadístico ------")
        print("1. Cargar datos desde un archivo CSV")
        print("2. Cargar datos desde un archivo TXT")
        print("3. Generar histograma")
        print("4. Generar gráfico de dispersión")
        print("5. Generar diagrama de círculo")
        print("6. Calcular estadísticas")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo CSV: ")
            datos = cargar_datos_csv(archivo)
            print("¡Datos cargados con éxito!")
        elif opcion == "2":
            archivo = input("Ingrese el nombre del archivo TXT: ")
            datos = cargar_datos_txt(archivo)
            print("¡Datos cargados con éxito!")
        elif opcion == "3":
            if datos:
                generar_histograma(datos)
            else:
                print("No se han cargado datos.")
        elif opcion == "4":
            if datos:
                generar_grafico_dispercion(datos)
            else:
                print("No se han cargado datos.")
        elif opcion == "5":
            if datos:
                generar_diagrama_circulo(datos)
            else:
                print("No se han cargado datos.")
        elif opcion == "6":
            if datos:
                resultados = calcular_estadisticas(datos)
                print("------ Resultados de estadísticas ------")
                for estadistica, valor in resultados.items():
                    print(f"{estadistica}: {valor}")
            else:
                print("No se han cargado datos.")
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Inicio de la aplicación
if __name__ == "__main__":
    menu_principal()
 