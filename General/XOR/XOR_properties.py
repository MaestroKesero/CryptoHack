def operation():
    
    KEY1 = bytes.fromhex(KEY1_hex)
    KEY2_KEY1 = bytes.fromhex(KEY2_KEY1_hex)
    KEY2_KEY3 = bytes.fromhex(KEY2_KEY3_hex)
    FLAG_KEY1_KEY3_KEY2 = bytes.fromhex(FLAG_KEY1_KEY3_KEY2_hex)
    
    flag = bytes([a ^ b ^ c for a,b,c in zip(KEY1,KEY2_KEY3,FLAG_KEY1_KEY3_KEY2)])
    print(flag.decode('ISO-8859-1'))
    
    
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_KEY1_KEY3_KEY2_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

operation()

#Para calcular flag, podemos ir calculando independientemente key1, key2 y key3 (para ello
# es necesario hacer las XOR en pares, por ejemplo para calcular KEY2 -> KEY1 ^ KEY1_KEY2)
# y posteriormente hacer la xor entre ellos para calcular KEY1_KEY2_KEY3 y una vez
# calculado hacer la XOR con FLAG_KEY1_KEY3_KEY2 y por propiedad asociativa obtenemos FLAG

# Otra manera mas simple que ha sido la que he desarrollado es que como tenemos KEY2_KEY3
# si simplemente le hacemos la XOR con KEY1, obtenemos KEY1_KEY2_KEY3 necesarios para hacer
#la XOR con FLAG_KEY1_KEY3_KEY2 y obtener la FLAG

#Muy importante tener en cuenta que estamos en hex, b'' solo funciona si estamos en string