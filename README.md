# Parcial_3

## Solucion de puntos:

* Se soluciona calculando los coeficientes de la Serie de Fourier de una funcion periodica: uno usando bucles (for) y otro usando recursion.

* Se implemento usando las siguientes funciones:

* - calcula_serie_fourier_iterativa(f, t, T, N): usando un bucle (for) para calcular los coeficientes.
* - calcula_serie_fourier_recursiva(f, t, T, N)`: usando recursividad para calcular dentro de los mismos coeficientes

## Implementacion:

# Función periódica

* Se utilizo como ejemplo la función periodica: 

* f(t)=sin(2πt), la cual es continua y periodica en el intervalo [0,2π].

# Calculo de coeficientes

* Para obtener los coeficientes de la serie de Fourier (an y bn ), se empleo la Regla del trapecio como metodo de integracion numerica. Esta regla se aplico tanto en el enfoque iterativo como en el recursivo para evaluar las integrales definidas correspondientes a cada uno de los terminos.

# Comparación de rendimiento

* Se midio el tiempo de ejecucion de ambos metodos (iterativo y recursivo) para diferentes valores de N, que representan la cantidad de armonicos calculados. A continuacion, se presentan los tiempos promedio obtenidos:

```
N = 5 → Tiempo iterativo: 0.018052 s | Tiempo recursivo: 0.017874 s
N = 10 → Tiempo iterativo: 0.038903 s | Tiempo recursivo: 0.036415 s
N = 20 → Tiempo iterativo: 0.078653 s | Tiempo recursivo: 0.073550 s
N = 50 → Tiempo iterativo: 0.195803 s | Tiempo recursivo: 0.200351 s
```
![Captura de pantalla 2025-06-04 090805](https://github.com/user-attachments/assets/3e69afab-1b86-46f0-afc2-3af9a729355a)
   
# Analisis comparativo

** ¿Cuál metodo resulta mas eficiente? **

En general, se puede decir que el metodo recursivo fue un poco mas rápido en los primeros casos cuando N es pequeño, pero para valores mas grandes como N = 50, el metodo iterativo fue mas estable.

** ¿Por qué? **

Ambos hacen basicamente lo mismo, pero con diferente forma de recorrer los datos.

El recursivo usa muchas llamadas internas, lo cual puede ser un problema si N es muy grande porque ocupa más memoria y se vuelve mas lento.

El iterativo va paso a paso con ciclos, lo que lo hace mas facil de entender y mas seguro en programas largos.

** En resumen: el recursivo a veces es mas rapido, pero el iterativo es mas claro y mejor para usar con valores grandes de N. **


