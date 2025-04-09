from vista import resultados
import time
inicio = time.time()
def leer(ruta):
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
    return [linea.strip() for linea in lineas if linea.strip().isdigit()]
def verificarpalindromo(numero):
    return numero == numero[::-1]
def buscarpalindromos(ruta_archivo):
    numeros = leer(ruta_archivo)
    palindromos = []
    for num in numeros:
        if verificarpalindromo(num):
            palindromos.append(num)
    resultados(palindromos)
time.sleep(1)

fin = time.time()
print("Tiempo de ejecución")
print(fin-inicio)