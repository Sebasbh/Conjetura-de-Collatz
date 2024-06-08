import time

def conjetura_collatz(numero, memo={}):
    if numero not in memo:
        secuencia = [numero]
        while numero != 1:
            if numero % 2 == 0:
                numero //= 2
            else:
                numero = numero * 3 + 1
            secuencia.append(numero)
        memo[numero] = secuencia
    return memo[numero]

def analizar_convergencia(max_numero):
    convergencia = {}
    for num_inicial in range(1, max_numero + 1):
        secuencia_collatz = conjetura_collatz(num_inicial)
        ultimo_numero = secuencia_collatz[-1]
        longitud_secuencia = len(secuencia_collatz)
        if ultimo_numero not in convergencia:
            convergencia[ultimo_numero] = [longitud_secuencia]
        else:
            convergencia[ultimo_numero].append(longitud_secuencia)
    return convergencia

def imprimir_estadisticos(convergencia):
    print("Estadísticas de convergencia:")
    for num_final, longitudes in convergencia.items():
        promedio = sum(longitudes) / len(longitudes)
        maximo = max(longitudes)
        minimo = min(longitudes)
        print(f"Número final: {num_final}, Promedio de longitud: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")

# Analizar convergencia para los primeros 100 números
max_numero = 9999999

inicio = time.time()
resultado_convergencia = analizar_convergencia(max_numero)
fin = time.time()

imprimir_estadisticos(resultado_convergencia)
print(f"Tiempo de ejecución: {fin - inicio} segundos.")
