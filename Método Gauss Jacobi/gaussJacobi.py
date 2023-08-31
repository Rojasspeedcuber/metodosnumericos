import numpy as np

def gauss_jacobi(A, b, x0, max_iterations=100, tolerance=1e-6):
    n = len(A)
    x = np.array(x0, dtype=float)
    x_new = np.zeros_like(x)
    
    for iteration in range(max_iterations):
        for i in range(n):
            sum_ax = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_ax) / A[i, i]
        
        if np.allclose(x_new, x, atol=tolerance):
            print(f"Converged after {iteration + 1} iterations.")
            return x_new
        
        x = x_new.copy()
    
    print("Did not converge within the specified number of iterations.")
    return x_new

# Exemplo de uso
A = np.array([[10, 3, -2],
              [2, 8, -1],
              [1, 1, 5]], dtype=float)
b = np.array([57, 20, -4], dtype=float)
x0 = [0, 0, 0]

solution = gauss_jacobi(A, b, x0)
print("Solution:", solution)