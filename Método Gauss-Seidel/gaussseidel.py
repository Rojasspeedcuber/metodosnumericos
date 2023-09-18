import numpy as np

def gauss_seidel(A, b, x0, tol=10e-7, max_iter=100):
    n = len(b)
    x = x0.copy()
    iters = 0
    
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        
        residual = np.abs(b - np.dot(A, x_new))
        
        if np.all(residual < tol):
            break
        
        x = x_new
        iters += 1
    
    return x, iters

# Exemplo de uso:
A = np.array([[4, -1, 0, -1, 0, 0, 0, 0, 0, 0],
     [-1, 4, -1, 0, -1, 0, 0, 0, 0, 0],
     [0, -1, 4, 0, 0, -1, 0, 0, 0, 0],
     [-1, 0, 0, 4, -1, 0, 0, 0, 0, 0],
     [0, -1, 0, -1, 4, -1, -1, 0, 0, 0],
     [0, -1, 4, 0, 0, -1, 0, 0, 0, 0],
     [0, 0, 0, 0, -1, 0, 4, -1, 0, 0],
     [0, 0, 0, 0, 0, -1, -1, 4, -1, 0],
     [0, 0, 0, 0, 0, 0, 0, -1, 4, -1],
     [0, 0, 0, 0, 0, 0, 0, 0, -1, 4]], dtype=float)
b = np.array([-110, -30, -40, -110, 0, -15, -90, -25, -55, -65], dtype=float)
x0 = np.zeros_like(b, dtype=float)

solution, iterations = gauss_seidel(A, b, x0)

print("Solução:", solution)
print("Número de iterações:", iterations)


