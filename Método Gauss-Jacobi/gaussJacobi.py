import numpy as np

def gauss_jacobi(A, b, x0, max_iterations=100, tolerance=10e-5):
    n = len(A)
    x = np.array(x0, dtype=float)
    x_new = np.zeros_like(x)
    
    for iteration in range(max_iterations):
        for i in range(n):
            sum_ax = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_ax) / A[i, i]
        
        if np.allclose(x_new, x, atol=tolerance):
            print(f"Convergiu depois de {iteration + 1} iterações.")
            return x_new
        
        x = x_new.copy()
    
    print("Não convergiu dentro do número especificado de iterações.")
    return x_new

# Exemplo de uso
A = np.array([[10, 3, -2],
              [2, 8, -1],
              [1, 1, 5]], dtype=float)
b = np.array([57, 20, -4], dtype=float)
x0 = [0, 0, 0]

solution = gauss_jacobi(A, b, x0)
print("Solução:", solution)