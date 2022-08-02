import sympy as sym

x = sym.Symbol('x')

print(sym.diff(sym.poly(x**2+2*x+3), x))
