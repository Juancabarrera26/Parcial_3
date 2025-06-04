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
   Se midio el tiempo de ejecucion de ambos metodos para distintos valores de N es decir los numero de armonicos. 

4. **Visualización de resultados**  
   Se grafico el tiempo que tarda cada enfoque en funcion del numero.

```
N = 5 → Tiempo iterativo: 0.018052 s | Tiempo recursivo: 0.017874 s
N = 10 → Tiempo iterativo: 0.038903 s | Tiempo recursivo: 0.036415 s
N = 20 → Tiempo iterativo: 0.078653 s | Tiempo recursivo: 0.073550 s
N = 50 → Tiempo iterativo: 0.195803 s | Tiempo recursivo: 0.200351 s
```
![Captura de pantalla 2025-06-04 090805](https://github.com/user-attachments/assets/3e69afab-1b86-46f0-afc2-3af9a729355a)
   
6. **Analisis comparativo**

* - ¿Cuál método resulta más eficiente?

**
