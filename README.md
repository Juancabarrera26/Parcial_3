# Parcial_3

## Solucion de puntos:

** Se soluciona calculando los coeficientes de la Serie de Fourier de una funcion periodica: uno usando bucles (for) y otro usando recursion.

** Se implemento usando las siguientes funciones:

* - calcula_serie_fourier_iterativa(f, t, T, N): usando un bucle (for) para calcular los coeficientes.
* - calcula_serie_fourier_recursiva(f, t, T, N)`: usando recursividad para calcular dentro de los mismos coeficientes

## Implementacion:

**Funcion periódica**  
   Se usó (f(t) = sin(t)( como ejemplo

2. **Calculo de coeficientes**  
   Se uso la (Regla del Trapecio) para calcular las integrales de los coeficientes `a₀`, `aₙ`, `bₙ`.

3. **Comparacion de rendimiento**  
   Se midio el tiempo de ejecucion de ambos metodos para distintos valores de N (numero de armonicos). Opcionalmente, también se puede medir el consumo de memoria usando `memory_profiler`.

4. **Visualización de resultados**  
   Se grafico el tiempo que tarda cada enfoque en funcion del numero de armonicos.
