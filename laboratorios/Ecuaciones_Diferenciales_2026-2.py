"""Clase del capítulo 8: métodos explícitos de un paso. Solo requiere NumPy.

Ejecutar desde cualquier carpeta. Produce tablas y datos para la presentación
en resultados_edo_2026-2/, junto a este archivo.
"""
# %% Métodos de un paso
from pathlib import Path
import json
import numpy as np


def paso_euler(f, t, y, h):
    return y + h * f(t, y)


def paso_punto_medio(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h / 2, y + h * k1 / 2)
    return y + h * k2


def paso_heun(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h, y + h * k1)
    return y + h * (k1 + k2) / 2


def paso_rk4(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h / 2, y + h * k1 / 2)
    k3 = f(t + h / 2, y + h * k2 / 2)
    k4 = f(t + h, y + h * k3)
    return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6


METODOS = {"Euler": paso_euler, "Punto medio": paso_punto_medio,
           "Heun": paso_heun, "RK4": paso_rk4}


def resolver(f, a, b, y0, n, paso):
    """Malla uniforme de n pasos; y0 puede ser escalar o vector real."""
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)) or n < 1:
        raise ValueError("n debe ser un entero positivo")
    if not np.isfinite([a, b]).all() or b <= a:
        raise ValueError("Se requiere a < b, con extremos finitos")
    inicial = np.asarray(y0, dtype=float)
    if not np.isfinite(inicial).all():
        raise ValueError("La condición inicial debe ser finita")
    t = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = np.empty((n + 1,) + inicial.shape)
    y[0] = inicial
    for k in range(n):
        y[k + 1] = paso(f, t[k], y[k], h)
    return t, y


# %% Un paso calculado a mano
def f(t, y):
    return y - t**2 + 1


def exacta(t):
    return (t + 1)**2 - .5 * np.exp(t)


print("PVI: y' = y - t^2 + 1, y(0) = 0.5; h = 0.2")
for nombre, paso in METODOS.items():
    print(f"{nombre:12s}: y1 = {paso(f, 0., .5, .2):.10f}")
print(f"{'Exacta':12s}: y(0.2) = {exacta(.2):.10f}")

# %% Consistencia de Euler: residuo y defecto de un paso
# Para y'=y, y(0)=1, la solución exacta es exp(t).
# Se parte de un dato exacto en t=0; no se calcula el error global.
pasos_locales = np.array([.2, .1, .05, .025])
defectos_locales = np.expm1(pasos_locales) - pasos_locales
residuos_locales = defectos_locales / pasos_locales
print("\nConsistencia de Euler en t=0 para y'=y, y(0)=1")
print("   h          tau=d/h          d")
for h_local, tau_local, d_local in zip(pasos_locales, residuos_locales, defectos_locales):
    print(f"{h_local:7.3f} {tau_local:16.8e} {d_local:16.8e}")
p_tau = float(np.log2(residuos_locales[-2] / residuos_locales[-1]))
p_defecto = float(np.log2(defectos_locales[-2] / defectos_locales[-1]))
print(f"Orden observado de tau: {p_tau:.6f}; del defecto: {p_defecto:.6f}")
print("Experimento en un punto; la prueba de las notas usa una cota uniforme en toda la malla.")
assert abs(p_tau - 1) < .05 and abs(p_defecto - 2) < .05
assert np.all(residuos_locales <= .5 * np.exp(pasos_locales) * pasos_locales)

# %% Refinamiento y orden observado
filas = []
for n in [10, 20, 40, 80]:
    fila = {"n": n, "h": 2 / n}
    for nombre, paso in METODOS.items():
        t, y = resolver(f, 0., 2., .5, n, paso)
        fila[nombre] = float(np.max(np.abs(y - exacta(t))))
    filas.append(fila)
print("\nErrores máximos sobre los nodos de [0,2]")
print(" n        Euler       Punto medio       Heun           RK4")
for fila in filas:
    print(f"{fila['n']:2d} " + " ".join(f"{fila[m]:14.6e}" for m in METODOS))
print("\nOrden observado log2(E_h / E_(h/2)), últimas dos mallas:")
ordenes = {m: float(np.log2(filas[-2][m] / filas[-1][m])) for m in METODOS}
for m, p in ordenes.items():
    print(f"{m:12s}: {p:.6f}")

# %% Modelo económico hipotético: acumulación de capital
delta, K0, T = .05, 10., 10.


def inversion(t):
    return 2 * np.exp(.02 * t)


def capital_rhs(t, K):
    return inversion(t) - delta * K


def capital_exacto(t):
    return K0 * np.exp(-delta * t) + 2 / (.05 + .02) * (
        np.exp(.02 * t) - np.exp(-delta * t))


print(f"\nCapital: K(10) exacto = {capital_exacto(T):.10f}")
for m, paso in METODOS.items():
    t, K = resolver(capital_rhs, 0., T, K0, 20, paso)
    print(f"{m:12s}: K(10) = {K[-1]:.10f}; error = {abs(K[-1]-capital_exacto(T)):.3e}")

# %% Sistemas y estabilidad (complemento)
def oscilador(t, z):
    return np.array([z[1], -z[0]])


t, z = resolver(oscilador, 0., 1., [1., 0.], 40, paso_rk4)
referencia = np.column_stack([np.cos(t), -np.sin(t)])
print(f"\nSistema: error máximo RK4 = {np.max(np.abs(z-referencia)):.3e}")
for h in [.25, .75]:
    print(f"y'=-4y, h={h}: amplificación Euler={1-4*h:.2f}, "
          f"Heun={1-4*h+(-4*h)**2/2:.2f}")

# %% Verificaciones y archivos para las transparencias
assert np.isclose(paso_euler(f, 0., .5, .2), .8)
assert np.isclose(paso_heun(f, 0., .5, .2), .826)
assert np.isclose(paso_punto_medio(f, 0., .5, .2), .828)
assert not np.isclose(paso_heun(f, 0., .5, .2), paso_punto_medio(f, 0., .5, .2))
for m, esperado in {"Euler": 1, "Punto medio": 2, "Heun": 2, "RK4": 4}.items():
    assert abs(ordenes[m] - esperado) < .12, (m, ordenes[m])
    assert all(filas[j + 1][m] < filas[j][m] for j in range(3))
    # Consistencia: integra una derivada constante exactamente.
    tt, yy = resolver(lambda t, y: np.ones_like(y), 0., 1., [2., 3.], 8, METODOS[m])
    np.testing.assert_allclose(yy[-1], [3., 4.], atol=1e-14)
assert np.max(np.abs(z - referencia)) < 4e-9

SALIDA = Path(__file__).resolve().parent / "resultados_edo_2026-2" if "__file__" in globals() else Path("resultados_edo_2026-2")
SALIDA.mkdir(exist_ok=True)
(SALIDA / "verificacion.json").write_text(json.dumps({"errores": filas, "ordenes": ordenes}, indent=2))


def cientifico_tex(x):
    mantisa, exponente = f"{x:.3e}".split("e")
    return rf"${mantisa}\times10^{{{int(exponente)}}}$"


tabla = [r"\begin{tabular}{rrrrr}\toprule",
         r"$n$ & Euler & Punto medio & Heun & RK4\\\midrule"]
for fila in filas:
    tabla.append(str(fila["n"]) + " & " + " & ".join(cientifico_tex(fila[m]) for m in METODOS) + r"\\")
tabla.append(r"\bottomrule\end{tabular}")
(SALIDA / "tabla_errores.tex").write_text("\n".join(tabla))
tabla = [r"\begin{tabular}{lrr}\toprule", r"Método & Orden teórico & Orden observado\\\midrule"]
for (m, p), teorico in zip(ordenes.items(), [1, 2, 2, 4]):
    tabla.append(f"{m} & {teorico} & {p:.3f}" + r"\\")
tabla.append(r"\bottomrule\end{tabular}")
(SALIDA / "tabla_ordenes.tex").write_text("\n".join(tabla))
t, e = resolver(f, 0., 2., .5, 10, paso_euler)
_, h = resolver(f, 0., 2., .5, 10, paso_heun)
_, r = resolver(f, 0., 2., .5, 10, paso_rk4)
np.savetxt(SALIDA / "trayectorias.dat", np.column_stack([t, exacta(t), e, h, r]),
           header="t exacta Euler Heun RK4", comments="")
print("\nVerificación completa: pasos manuales, órdenes, consistencia y sistema vectorial.")
