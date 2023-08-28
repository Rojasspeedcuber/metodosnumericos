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