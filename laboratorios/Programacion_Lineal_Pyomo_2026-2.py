"""Ejemplos LAD y MAD con datos sintéticos. Métodos Numéricos, UP, 2026-2.

Instalación: python3 -m pip install pyomo highspy
Ejecución: python3 laboratorios/Programacion_Lineal_Pyomo_2026-2.py

Formulaciones de referencia:
https://mobook.github.io/MO-book/notebooks/02/02-lad-regression.html
https://mobook.github.io/MO-book/notebooks/02/03-mad-portfolio-optimization.html
"""

# CREAR_SOLVER_BEGIN
import pyomo.environ as pyo


def crear_solver():
    solver = pyo.SolverFactory("appsi_highs")
    if not solver.available(exception_flag=False):
        raise RuntimeError("HiGHS requiere el paquete highspy.")
    return solver
# CREAR_SOLVER_END


# RESOLVER_BEGIN
def resolver(modelo, solver):
    resultado = solver.solve(modelo, load_solutions=False)
    pyo.assert_optimal_termination(resultado)
    modelo.solutions.load_from(resultado)
# RESOLVER_END


def modelo_lad():
    """Ajusta una recta a cinco observaciones, una de ellas atípica."""
    # LAD_VAR_BEGIN
    z = (0, 1, 2, 3, 4)
    y = (1, 3, 15, 7, 9)
    m = pyo.ConcreteModel("LAD")
    m.I = pyo.RangeSet(0, len(y) - 1)
    m.alpha = pyo.Var(domain=pyo.Reals)
    m.beta = pyo.Var(domain=pyo.Reals)
    m.p = pyo.Var(m.I, domain=pyo.NonNegativeReals)
    m.q = pyo.Var(m.I, domain=pyo.NonNegativeReals)
    # LAD_VAR_END

    # LAD_REST_BEGIN
    @m.Constraint(m.I)
    def residuo(m, i):
        return m.alpha + z[i] * m.beta + m.p[i] - m.q[i] == y[i]

    m.error = pyo.Objective(
        expr=sum(m.p[i] + m.q[i] for i in m.I), sense=pyo.minimize
    )
    # LAD_REST_END
    return m


def modelo_mad():
    """Construye una cartera de dos activos y cuatro períodos."""
    # MAD_VAR_BEGIN
    r = {"A": (0.00, 0.02, 0.06, 0.08),
         "B": (0.04, 0.03, 0.01, 0.00)}
    media = {j: sum(serie) / len(serie) for j, serie in r.items()}

    m = pyo.ConcreteModel("Cartera MAD")
    m.J = pyo.Set(initialize=list(r))
    m.T = pyo.RangeSet(0, len(r["A"]) - 1)
    m.R = pyo.Param(initialize=0.03, mutable=True)
    m.w = pyo.Var(m.J, bounds=(0, 0.8))
    m.p = pyo.Var(m.T, domain=pyo.NonNegativeReals)
    m.q = pyo.Var(m.T, domain=pyo.NonNegativeReals)
    # MAD_VAR_END

    # MAD_REST_BEGIN
    @m.Constraint(m.T)
    def desvio(m, t):
        return m.p[t] - m.q[t] == sum(
            (r[j][t] - media[j]) * m.w[j] for j in m.J
        )

    m.presupuesto = pyo.Constraint(expr=sum(m.w.values()) == 1)
    m.retorno = pyo.Expression(expr=sum(media[j] * m.w[j] for j in m.J))
    m.meta = pyo.Constraint(expr=m.retorno >= m.R)
    m.riesgo = pyo.Objective(
        expr=sum(m.p[t] + m.q[t] for t in m.T) / len(m.T),
        sense=pyo.minimize,
    )
    # MAD_REST_END
    return m


def main():
    solver = crear_solver()

    # LAD_SOL_BEGIN
    lad = modelo_lad()
    resolver(lad, solver)
    print(f"Intercepto = {pyo.value(lad.alpha):.2f}")
    print(f"Pendiente  = {pyo.value(lad.beta):.2f}")
    print(f"Error LAD  = {pyo.value(lad.error):.2f}")
    # LAD_SOL_END

    # MAD_SOL_BEGIN
    mad = modelo_mad()
    for meta in (0.03, 0.035):
        mad.R.set_value(meta)
        resolver(mad, solver)
        pesos = {j: round(pyo.value(mad.w[j]), 6) for j in mad.J}
        print(f"\nMeta = {meta:.1%}")
        print("Pesos:", pesos)
        print(f"Retorno medio = {pyo.value(mad.retorno):.3%}")
        print(f"Riesgo MAD    = {pyo.value(mad.riesgo):.3%}")
    # MAD_SOL_END


if __name__ == "__main__":
    main()
