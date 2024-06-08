# Conjetura de Collatz en Python

Este es un proyecto en Python que implementa la [Conjetura de Collatz](https://es.wikipedia.org/wiki/Conjetura_de_Collatz), también conocida como el problema 3x + 1. La conjetura establece que cualquier número natural siempre alcanzará el valor 1 eventualmente siguiendo estas reglas:

- Si el número es par, divídelo por 2.
- Si el número es impar, multiplícalo por 3 y súmale 1.

## Contenido

- [Cómo Funciona](#cómo-funciona)
- [Cómo Usar](#cómo-usar)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Cómo Funciona

El proyecto consta de dos funciones principales:

1. `conjetura_collatz(numero, memo={})`: Esta función toma un número inicial y devuelve una lista que representa la secuencia de la Conjetura de Collatz para ese número.

2. `analizar_convergencia(max_numero)`: Esta función analiza la convergencia de la Conjetura de Collatz para una serie de números hasta un máximo dado. Devuelve un diccionario que muestra estadísticas sobre la longitud de las secuencias de convergencia para cada número.

## Cómo Usar

Para ejecutar el análisis de convergencia para los primeros 100 números, simplemente ejecuta el script `conjetura_collatz.py`. Puedes modificar la variable `max_numero` para cambiar el rango de números a analizar.

```bash
python conjetura_collatz.py
```

## Novedades

- Ahora el programa tiene la capacidad de generar gráficos para visualizar la convergencia de la conjetura de Collatz. Se han incluido funciones para graficar tanto la convergencia de las secuencias como la relación entre el número inicial y la longitud de la secuencia.