#  (EN) Collatz Conjecture in Python

This is a Python project that implements the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), also known as the 3x + 1 problem. The conjecture states that any natural number will eventually reach the value 1 following these rules:

- If the number is even, divide it by 2.
- If the number is odd, multiply it by 3 and add 1.

## Contents

- [How It Works](#how-it-works)
- [How to Use](#how-to-use)

## How It Works

The project consists of two main functions:

1. `conjecture_collatz(number, memo={})`: This function takes an initial number and returns a list representing the Collatz Conjecture sequence for that number.

2. `analyze_convergence(max_number)`: This function analyzes the convergence of the Collatz Conjecture for a series of numbers up to a given maximum. It returns a dictionary showing statistics about the length of convergence sequences for each number.

## How to Use

To run the convergence analysis for the first 100 numbers, simply execute the `collatz_conjecture.py` script. You can modify the `max_number` variable to change the range of numbers to analyze.

```bash
python collatz_conjecture.py
```

## Updates

- The program now has the capability to generate plots to visualize the convergence of the Collatz conjecture. Functions have been included to plot both the convergence of sequences and the relationship between the initial number and the sequence length.



# (ES) Conjetura de Collatz en Python

Este es un proyecto en Python que implementa la [Conjetura de Collatz](https://es.wikipedia.org/wiki/Conjetura_de_Collatz), también conocida como el problema 3x + 1. La conjetura establece que cualquier número natural siempre alcanzará el valor 1 eventualmente siguiendo estas reglas:

- Si el número es par, divídelo por 2.
- Si el número es impar, multiplícalo por 3 y súmale 1.

## Contenido

- [Cómo Funciona](#cómo-funciona)
- [Cómo Usar](#cómo-usar)


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