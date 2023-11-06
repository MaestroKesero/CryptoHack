def module(a,n):

    b = a % n
    print(f"El modulo es: ", b)


a = 73246787654 ** 65536
n = 65537
module(a,n)


# Cuando calculamos 5^17 mod 17, como el elevado coincide con el modulo, es como si no estuvieramos haciendo nada
# ya que seria como dar una vuelta completa y acabar en el mismo sitio
#
# Cuando calculamos 7^16 el resultado es 1 debido a El Pequeño Teorema de Fermatt.

# Dicho teorema asegura que si tenemos un numero a primo, n primo y si a es coprimo de p, enltonces podemos 
# asegurar que a^(p-1) ≡ 1 (mod p)

#En otras palabras, elevar un número "a" a la potencia "p-1" y luego tomar el residuo cuando se divide por el número primo "p" dará como resultado 1.

# NOTA: Algunos puntos clave sobre el Pequeño Teorema de Fermat:
#
# "p" debe ser un número primo: El teorema se aplica únicamente a números primos. No es válido para números compuestos.

# "a" debe ser coprimo con "p": Para que el teorema sea válido, "a" no debe ser divisible por "p". 
# Esto significa que el máximo común divisor (GCD) de "a" y "p" debe ser igual a 1.
# La congruencia modular: El teorema establece que la potencia "a^(p-1)" es congruente con 1 (mod p).
# Esto significa que "a^(p-1)" y 1 dejan el mismo residuo cuando se dividen por "p".