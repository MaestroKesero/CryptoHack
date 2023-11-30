from pwn import xor

def add_round_key(s, k):
    state_bytes = matrix2bytes(s)
    roundKey_bytes = matrix2bytes(k)
    result_bytes = xor(state_bytes, roundKey_bytes)
    return result_bytes


def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes([matrix[i][j] for i in range(4) for j in range(4)])

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

print(add_round_key(state, round_key))

# Este ejercicio se puede hacer de muchas formas, una de ellas es haciendo el XOR sin pasar a bytes
#
# def add_round_key(s, k):
#    return [[sss^kkk for sss, kkk in zip(ss, kk)] for ss, kk in zip(s, k)]
#
# En mi caso he optado por la forma mas simple, pasamos los valores a bytes y luego hacemos la xor de los valores
# Otra forma tambien seria hacer la xor manual de manera muy simple:
#
#def add_round_key(s, k):
#    """XOR the state with the round key."""
#    return [[s_byte ^ k_byte for s_byte, k_byte in zip(s_row, k_row)] for s_row, k_row in zip(s, k)]
