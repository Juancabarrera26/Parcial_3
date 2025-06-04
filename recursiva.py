import numpy as np

def recursiva(f, t0, T, N, M, integrar):
    a = calcular_a(f, t0, T, N, M, integrar)
    b = calcular_b(f, t0, T, N, M, integrar)
    return a, b

def calcular_a(f, t0, T, n, M, integrar):
    if n == 0:
        return []
    else:
        anteriores = calcular_a(f, t0, T, n - 1, M, integrar)

        def funcion_coseno(t):
            return f(t) * np.cos(2 * np.pi * n * t / T)

        an = (2 / T) * integrar(funcion_coseno, t0, t0 + T, M)
        return anteriores + [an]

def calcular_b(f, t0, T, n, M, integrar):
    if n == 0:
        return []
    else:
        anteriores = calcular_b(f, t0, T, n - 1, M, integrar)

        def funcion_seno(t):
            return f(t) * np.sin(2 * np.pi * n * t / T)

        bn = (2 / T) * integrar(funcion_seno, t0, t0 + T, M)
        return anteriores + [bn]
