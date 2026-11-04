"""Programación lineal. Métodos Numéricos, UP, 2026-2.

Instalación: python3 -m pip install numpy scipy
Ejecución: python3 laboratorios/Programacion_Lineal_2026-2.py

Datos de BIM: https://mobook.github.io/MO-book/notebooks/02/01-bim.html
"""

import numpy as np


def simplex_revisado(A, b, c, base, tol=1e-9, max_pivotes=100):
    """Minimiza c @ x con A @ x = b y x >= 0 desde una base factible.

    Los índices de la base comienzan en cero. La trayectoria guarda cada
    par (base, x) visitado. Devuelve (x, trayectoria, None) al encontrar
    un óptimo o (None, trayectoria, rayo) si detecta no acotación.
    La tolerancia absoluta está pensada para ejemplos bien escalados.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    c = np.asarray(c, dtype=float)
    m, n = A.shape
    base = list(base)
    if b.shape != (m,) or c.shape != (n,):
        raise ValueError("Las dimensiones de A, b y c deben coincidir.")
    if len(base) != m or len(set(base)) != m:
        raise ValueError("La base debe tener m índices distintos.")
    if any(not isinstance(j, (int, np.integer)) or not 0 <= j < n for j in base):
        raise ValueError("Los índices básicos deben ser enteros entre 0 y n-1.")

    trayectoria = []
    for pivotes in range(max_pivotes + 1):
        B = A[:, base]
        x_B = np.linalg.solve(B, b)
        if np.any(x_B < -tol):
            raise ValueError("La base debe ser factible dentro de la tolerancia.")

        x = np.zeros(n)
        x[base] = x_B
        trayectoria.append((tuple(base), x))

        y = np.linalg.solve(B.T, c[base])
        reducidos = c - A.T @ y
        # Bland: primera variable no básica con costo reducido negativo.
        entra = next(
            (j for j in range(n) if j not in base and reducidos[j] < -tol),
            None,
        )
        if entra is None:
            return x, trayectoria, None

        u = np.linalg.solve(B, A[:, entra])
        filas = np.flatnonzero(u > 0)
        if filas.size == 0:
            rayo = np.zeros(n)
            rayo[base] = -u
            rayo[entra] = 1
            return None, trayectoria, rayo

        if pivotes == max_pivotes:
            break
        # El segundo componente desempata por índice de variable básica.
        sale = min(filas, key=lambda i: (max(x_B[i], 0.0) / u[i], base[i]))
        base[sale] = entra

    raise RuntimeError("Se alcanzó el límite de pivotes.")


def ejemplo_bim():
    """Compara los pivotes docentes con HiGHS y valora una unidad de plástico."""
    from scipy.optimize import linprog

    c = np.array([12., 9.])
    A = np.array([[1., 0.], [0., 1.], [1., 1.], [4., 2.]])
    b = np.array([1000., 1500., 1750., 4800.])

    m, n = A.shape
    A_estandar = np.column_stack((A, np.eye(m)))
    c_estandar = np.r_[-c, np.zeros(m)]
    x, trayectoria, rayo = simplex_revisado(
        A_estandar, b, c_estandar, base=range(n, n + m)
    )
    if rayo is not None:
        raise RuntimeError("Se esperaba un óptimo finito en BIM.")

    print("Símplex primal (base numerada desde 1)")
    for k, (base, punto) in enumerate(trayectoria):
        print(f"  {k}: base={tuple(j + 1 for j in base)}, "
              f"plan={punto[:n]}, margen={c @ punto[:n]:.0f}")

    res = linprog(-c, A_ub=A, b_ub=b, bounds=(0, None), method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    if not np.allclose(x[:n], res.x):
        raise RuntimeError("Los dos métodos devolvieron planes distintos en BIM.")

    print("\nHiGHS")
    print("Plan y margen:", res.x, -res.fun)
    print("Holguras:", b - A @ res.x)
    print("Precios sombra:", -res.ineqlin.marginals)

    b_adicional = b.copy()
    b_adicional[2] += 1  # Plástico
    nuevo = linprog(-c, A_ub=A, b_ub=b_adicional, bounds=(0, None), method="highs")
    if not nuevo.success:
        raise RuntimeError(nuevo.message)
    print("\nCon una unidad más de plástico")
    print("Plan y margen:", nuevo.x, -nuevo.fun)
    print(f"Aumento del margen: {res.fun - nuevo.fun:.2f}")


if __name__ == "__main__":
    ejemplo_bim()
