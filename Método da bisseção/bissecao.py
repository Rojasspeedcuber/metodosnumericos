import math

def bisection_method(func, a, b, tol=1e-6, max_iter=1000):
    if func(a) * func(b) > 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    root = (a + b) / 2
    return root, iter_count
def func(x):
    return x + math.cos(x)

a = -5
b = 4

root, iterations = bisection_method(func, a, b)
print(f"Raiz aproximada: {root}")
print(f"Número de iterações: {iterations}")


