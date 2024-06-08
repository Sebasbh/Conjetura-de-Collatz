import time
import matplotlib.pyplot as plt

def conjetura_collatz(numero, memo={}):
    """Calcula la secuencia de Collatz para un número dado."""
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
    """Analiza la convergencia de la conjetura de Collatz para los primeros max_numero números."""
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
    """Imprime estadísticas de convergencia."""
    print("Estadísticas de convergencia:")
    for num_final, longitudes in convergencia.items():
        promedio = sum(longitudes) / len(longitudes)
        maximo = max(longitudes)
        minimo = min(longitudes)
        print(f"Número final: {num_final}, Promedio de longitud: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")

def graficar_convergencia(convergencia):
    """Grafica la convergencia de la conjetura de Collatz."""
    try:
        for num_final, longitudes in convergencia.items():
            plt.plot(longitudes, label=f"Número final: {num_final}")
        plt.xlabel("Número inicial")
        plt.ylabel("Longitud de la secuencia")
        plt.title("Convergencia de la conjetura de Collatz")
        plt.legend()
        plt.show()
    except KeyboardInterrupt:
        print("\nGeneración de gráfica interrumpida.")

def graficar_dispersión(convergencia):
    """Genera un gráfico de dispersión que muestra la relación entre el número inicial y la longitud de la secuencia."""
    try:
        x = []
        y = []
        for num_final, longitudes in convergencia.items():
            for longitud in longitudes:
                x.append(num_final)
                y.append(longitud)
        plt.scatter(x, y, s=5)
        plt.xlabel("Número final")
        plt.ylabel("Longitud de la secuencia")
        plt.title("Relación entre el número final y la longitud de la secuencia de Collatz")
        plt.show()
    except KeyboardInterrupt:
        print("\nGeneración de gráfica interrumpida.")


# Analizar convergencia para los primeros 100 números
max_numero = 999

inicio = time.time()
resultado_convergencia = analizar_convergencia(max_numero)
fin = time.time()

imprimir_estadisticos(resultado_convergencia)
print(f"Tiempo de ejecución: {fin - inicio} segundos.")

# Graficar la convergencia y el gráfico de dispersión
graficar_convergencia(resultado_convergencia)
graficar_dispersión(resultado_convergencia)