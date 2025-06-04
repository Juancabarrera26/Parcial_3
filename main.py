import numpy as np
import time
import matplotlib.pyplot as plt
import iterativa
import recursiva

def f(t):
    return np.sin(2 * np.pi * t)

def integrar(funcion, a, b, M):
    h = (b - a) / (M - 1)
    suma = funcion(a) + funcion(b)
    for i in range(1, M - 1):
        t = a + i * h
        suma += 2 * funcion(t)
    return (h / 2) * suma

def comparar_para_N(f, t0, T, N, M):
    inicio1 = time.time()
    iterativa.iterativa(f, t0, T, N, M, integrar)
    tiempo1 = time.time() - inicio1

    inicio2 = time.time()
    recursiva.recursiva(f, t0, T, N, M, integrar)
    tiempo2 = time.time() - inicio2

    return tiempo1, tiempo2

if __name__ == "__main__":
    t0 = 0
    T = 2 * np.pi
    M = 1000
    valores_N = [5, 10, 20, 50]
    tiempos_iterativos = []
    tiempos_recursivos = []

    for N in valores_N:
        tiempo_iter, tiempo_rec = comparar_para_N(f, t0, T, N, M)
        tiempos_iterativos.append(tiempo_iter)
        tiempos_recursivos.append(tiempo_rec)
        print(f"N = {N} → Tiempo iterativo: {tiempo_iter:.6f} s | Tiempo recursivo: {tiempo_rec:.6f} s")

    plt.plot(valores_N, tiempos_iterativos, label="Iterativo", marker='o')
    plt.plot(valores_N, tiempos_recursivos, label="Recursivo", marker='s')
    plt.xlabel("Valores de N")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos: Iterativa vs Recursiva")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
