import math


def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    
    return result

valores_x = [0.7, 1.2, 1.3, 1.5, 2.0, 2.3, 2.6]
valores_y = [0.043, 1.928, 2.497, 3.875, 9.000, 13.467, 19.176]
ponto = 1.4

print(lagrange_interpolation(valores_x, valores_y, ponto))


def interpolation_error(x, x_values, y_values):
    """
    Calcula o erro de interpolação em um ponto x específico.
    
    x: O ponto no qual se deseja calcular o erro de interpolação.
    x_values: Lista dos valores conhecidos de x.
    y_values: Lista dos valores conhecidos de y correspondentes aos valores de x.
    
    Retorna o erro de interpolação em x.
    """
    n = len(x_values)
    max_derivative = 1  # Ordem máxima da derivada das funções interpolantes
    
    error = 0.0
    for i in range(n):
        term = 1.0
        for j in range(n):
            if j != i:
                term *= abs(x - x_values[j]) / abs(x_values[i] - x_values[j])
        error += term
    
    error *= max_derivative * max(y_values) / (math.factorial(n) * (2**n))
    
    return error

# Exemplo de uso
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
interpolation_point = 2.5

interpolated_value = lagrange_interpolation(x_values, y_values, interpolation_point)
error = interpolation_error(interpolation_point, x_values, y_values)

print(f"Valor interpolado em x = {interpolation_point}: {interpolated_value}")
print(f"Erro de interpolação em x = {interpolation_point}: {error}")
