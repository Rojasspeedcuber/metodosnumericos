from math import e

def euler_method(func, y0, t0, tn, h):
    # Lista para armazenar os resultados
    result = []
    
    # Valor inicial de y
    y = y0
    
    # Valor inicial de x (ou t)
    t = t0
    
    # Loop para calcular os valores usando o método de Euler
    while t <= tn:
        result.append((t, y))
        # Calcula o próximo valor de y usando a fórmula do método de Euler
        y = y + h * func(t, y)
        # Atualiza o valor de x (ou t) para o próximo passo
        t += h
    
    return result

# Exemplo de uma equação diferencial: dy/dx = x + y
def equation(x, y):
    return e**y*x

# Condição inicial: y(0) = 1, x varia de 0 a 1 com passo de 0.1
initial_y = 1
initial_x = 0
final_x = 1
step_size = 0.1

# Calcula a solução usando o método de Euler
solution = euler_method(equation, initial_y, initial_x, final_x, step_size)

# Imprime a solução
print("Solução usando o método de Euler:")
for x, y in solution:
    print(f"x = {x}, y = {y}")
