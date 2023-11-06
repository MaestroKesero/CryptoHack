def gcd(a,b):

    while b > 0:
        
        module = a % b
        a = b
        b = module

    print(f"El GCD es:", a)

a = 12
b = 8
gcd(a,b)

a = 66528
b = 52920 
gcd (a,b)

# El algoritmo de Eucldes se basa en obtener los residuos de las divisiones
# a y b para posteriormente dividir la parte b entre el modulo resultante.

# Ineficiente al operar con numeros grandes debido a su 
# gran factorizacion
