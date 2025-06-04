import numpy as np

def iterativa(f, t0, T, N, M, integrar):
    a = []
    b = []

    for n in range(1, N + 1):
        def funcion_coseno(t):
            return f(t) * (np.cos(2 * np.pi * n * t / T))

        def funcion_seno(t):
            return f(t) * (np.sin(2 * np.pi * n * t / T))

        an = (2 / T) * integrar(funcion_coseno, t0, t0 + T, M)
        bn = (2 / T) * integrar(funcion_seno, t0, t0 + T, M)

        a.append(an)
        b.append(bn)

    return a, b
