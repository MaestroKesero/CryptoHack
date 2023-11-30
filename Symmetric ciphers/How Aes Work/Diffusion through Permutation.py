def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    # Invertimos 2º fila
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    # Invertimos 3º fila
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    # Invertimos 4º fila
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
    return s

# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes([matrix[i][j] for i in range(4) for j in range(4)])

state = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]

print("Los valores originales de la matriz son: ", state)
print("Los valores de la matriz con las columnas mezcladas e invertidas son: ", inv_mix_columns(state))
print("Los valores de la matriz con las filas invertidas son: ", inv_shift_rows(state))
print("Los valores de la matriz con las filas invertidas en bytes son: ", matrix2bytes(state))

# Es muy importante conocer como se distribuyen los bytes estado en la matriz ya que nosotros estamos 
# acostumbrados a trabajar con matrices de izquierda a derecha, ahora en shift rows trabajamos de arriba a abajo
# Esto es debido a como se introducen los bytes en la matriz estado.

# A su vez la variable xterm mplementa una multiplicación por dos en el campo finito GF(2^8) de manera segura para 
# la criptografía, utilizando la representación polinómica del campo finito.

# Una explicacion mas en detalle de como funciona dicha funcion lamda:
#    a & 0x80: Verifica si el bit más significativo de a es 1. Esto se hace usando una operación de AND con 0x80 (10000000 en binario). Si el resultado es diferente de cero, significa que el bit más significativo es 1.
#
#    (a << 1): Desplaza los bits de a a la izquierda en una posición. Esto es equivalente a multiplicar a por 2.
#
#    ((a << 1) ^ 0x1B) & 0xFF: Si el bit más significativo de a es 1 (según la condición en el paso 1), entonces realiza una operación XOR (exclusiva OR) con el polinomio irreducible 0x1B y luego aplica una operación AND con 0xFF para mantener solo los 8 bits menos significativos.
#
#    else (a << 1): Si el bit más significativo de a es 0 (según la condición en el paso 1), simplemente realiza un desplazamiento a la izquierda en una posición, que es equivalente a multiplicar a por 2.