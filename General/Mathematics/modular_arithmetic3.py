def modular_inverse(a,m):

    if m == 1:
        return 0

    inverse = pow(a, -1, m)
    if inverse is not None:
        print(f"El inverso modular de {a} y {m} es: {inverse}")
    else:
        print("No se ha podido encontrar el inverso modular")

a = 3
m = 13
modular_inverse(a,m)

# Dado El Pequeño Teorema de Fermat, podemos calcular los inversos multiplicativos de un numero
# mediante la siguiente ecuacion a^(-1) ≡ a^(p-2) (mod p) (sabiendo que a y p deben de ser coprimos)
# Para ello vamos a ir haciendolo paso a paso.
#
#   3 * d ≡ 1 mod 13 ?      --> Aplicando el Teorema de Fermat a^(p-1) ≡ 1 (mod p)
#   3^12 ≡ 1 mod 13         
#   3 * d ≡ 1 mod 13        --> Despejando
#   d ≡ (1/3) * mod 13      --> Esto no es valido en Aritmetica modular, por lo que multiplicamos por inverso
#   d ≡ (1/3)* 3^12 mod 13
#   d ≡ 3^11 mod 13         --> Calculamos el valor de 3^11
#   3^11 = 177147           --> Calculamos el módulo
#   177147 ≡ 9 mod 13
#
#   El inverso multiplicativo de 3 es 9.
# 
# En python haciendo uso de la funcion pow(a, -1, m), le decimos a el compilador que nos haga el inverso modular