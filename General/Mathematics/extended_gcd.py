def extended_gcd(a,b):

    x0, x1 ,y0, y1 = 1, 0, 0, 1
    a_or, b_or = a, b 

    while b!= 0:

        # GCD Euclides
        q = a // b
        r = a - b * q

        # Actualizamos coeficientes
        x_temp = x1
        x1 = x0 - q * x1
        x0 = x_temp

        y_temp = y1
        y1 = y0 - q * y1
        y0 = y_temp

        # Futuras iteraciones
        a = b
        b = r

    print(f"GCD({a_or},{b_or}) = {a}")
    print(f"Coeficiente u: ", x0)
    print(f"Coeficiente v: ", y0)
   
p = 32321
q = 26513
extended_gcd(p,q)


# p * u + q * v = gcd(p,q)
# Basicamente lo que tenemos que calcular son los inversos modulares (Teorema Bezout) p * u + q * v = gcd(p,q)
# En este video lo explica de maravilla: https://www.youtube.com/watch?v=JGyFkl5_KHM&t=116s

# Nos guiaremos de coeficientes x0, y0 (Coeficientes lineales para calcular la combinacion)
# y de x1, y1 (coeficientes temporales para calcular las nuevas variables)


# NOTA: A que se debe esa combinacion de 1 y 0 en las variables x0,x1 y y0, y1?

# La asignación inicial de x0 a 1 y y0 a 0 (junto con x1 a 0 y y1 a 1) es una elección convencional 
# en el algoritmo extendido de Euclides. Esto se hace para establecer la combinación lineal de Bezout 
# en una forma que sea útil en el proceso de cálculo y que no afecte el resultado final.
#
# Cuando se inicia el algoritmo extendido de Euclides, no se conocen los coeficientes de la combinación 
# lineal que satisface la ecuación de Bezout. Por lo tanto, es común elegir valores iniciales que permitan 
# rastrear los coeficientes de una manera coherente durante el proceso. Estos valores de 1 y 0 
# (para x0 y y0, respectivamente) aseguran que la combinación lineal inicial sea simplemente a * 1 + b * 0, 
# lo que es igual a a, y la combinación lineal a y b es consistente con el primer paso del algoritmo.
#
# A medida que el algoritmo avanza y se realizan divisiones sucesivas para calcular el MCD y los coeficientes 
# de Bezout, estos valores iniciales se actualizan para mantener un registro de la combinación lineal de manera
# efectiva. Al final del algoritmo, los valores de x0 y y0 contendrán los coeficientes de la combinación lineal
# de Bezout que satisface la ecuación ax + by = MCD(a, b) para los números dados a y b.
#

# NOTA: Ejemplo gcd(17,3) extendido:

# X0 = 1 ; X1 = 0
# Y0 = 0 ; Y0 = 1
# x0 = x0 - q*x1 (Intercambio de variables para futuras iteraciones)
# y0 = y1 - q*y1 (Intercambio de variables para futuras iteraciones)