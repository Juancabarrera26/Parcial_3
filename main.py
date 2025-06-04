import numpy as np
import time
from iterativa import iterativa
from recursiva import recursiva

def f(t):
    return np.sin(2 * np.pi * t)

def integrar(funcion, a, b, M):
    h = (b - a) / (M - 1)
    suma = funcion(a) + funcion(b)
    for i in range(1, M - 1):
        t = a + i * h
        suma += 2 * funcion(t)
    return (h / 2) * suma

def comparar(f, t0, T, N, M):
    inicio1 = time.time()
    a1, b1 = iterativa(f, t0, T, N, M, integrar)
    tiempo1 = time.time() - inicio1

    inicio2 = time.time()
    a2, b2 = recursiva(f, t0, T, N, M, integrar)
    tiempo2 = time.time() - inicio2

    print("Tiempo iterativo:", tiempo1, "segundos")
    print("Tiempo recursivo:", tiempo2, "segundos")

if __name__ == "__main__":
    t0 = 0
    T = 2 * np.pi
    N = 10
    M = 1000
    comparar(f, t0, T, N, M)
