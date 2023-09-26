import sympy as sp

# Defina a variável simbólica
x = sp.symbols('x')

# Defina a função que você deseja integrar
funcao = sp.cos(x)**3

# Defina os limites do intervalo
a = 0.0 # a: limite inferior do intervalo
b = sp.pi / 2.0 # b: limite superior do intervalo 

# Calcule a integral exata usando SymPy
integral_exata = sp.integrate(funcao, (x, a, b)).evalf()

# Função para calcular a integral numérica pelo método do trapézio
def metodo_trapezio(a, b, n):
    h = (b - a) / n
    integral_numerica = (funcao.subs(x, a) + funcao.subs(x, b)) / 2.0
    
    for i in range(1, n):
        x_val = a + i * h
        integral_numerica += funcao.subs(x, x_val)
    
    integral_numerica *= h
    
    return integral_numerica.evalf()

# Defina o número de subintervalos
n = 4

integral_numerica = metodo_trapezio(a, b, n)

erro = abs(integral_exata - integral_numerica)

print("Resultado da integral numérica:", integral_numerica)
print("Resultado da integral exata:", integral_exata)
print("Erro absoluto:", erro)
