import sympy as sp

def newton_raphson(f, x0, tol=0.0001, max_iter=100):
    
    x = sp.symbols('x')
    df = sp.diff(f, x)  # Calcula a derivada da função

    iteration = 0
    x_n = x0

    while iteration < max_iter:
        f_value = f.subs(x, x_n)
        df_value = df.subs(x, x_n)

        if abs(f_value) < tol:
            # Raiz encontrada com precisão suficiente
            return x_n, iteration

        if df_value == 0:
            # Evita divisão por zero
            raise ValueError("Derivada zero. O método de Newton-Raphson não pode ser aplicado.")

        x_n = x_n - f_value / df_value
        iteration += 1

    raise ValueError("Número máximo de iterações atingido. Não foi possível encontrar a raiz com a precisão desejada.")

# Exemplo de uso:
if __name__ == "__main__":
    x = sp.symbols('x')
    # Defina a função para a qual você deseja encontrar raízes
    f = x**2 - 2*x - 3

    # Escolha uma estimativa inicial
    x0 = 2.0

    # Chama o método de Newton-Raphson
    root, iterations = newton_raphson(f, x0)

    print(f"Raiz aproximada: {root}")
    print(f"Iterações realizadas: {iterations}")
