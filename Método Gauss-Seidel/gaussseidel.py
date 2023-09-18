def gauss_seidel(A, b, tol=10e-7, max_iter=100):
    n = len(b)
    x = [0.0] * n
    iter_count = 0

    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sigma = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]

        iter_count += 1

        # Verifica a convergência com base na tolerância
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            break

        x = x_new

    return x, iter_count

# Exemplo de uso
A = [[4, -1, 0, -1, 0, 0, 0, 0, 0, 0],
     [-1, 4, -1, 0, -1, 0, 0, 0, 0, 0],
     [0, -1, 4, 0, 0, -1, 0, 0, 0, 0],
     [-1, 0, 0, 4, -1, 0, 0, 0, 0, 0],
     [0, -1, 0, -1, 4, -1, -1, 0, 0, 0],
     [0, -1, 4, 0, 0, -1, 0, 0, 0, 0]
     ]
b = [5, 5, 5, 5]

sol, iterations = gauss_seidel(A, b)
print("Solução:", sol)
print("Número de iterações:", iterations)
