def xor():

    key_part = bytes([byte1 ^ byte2 for byte1,byte2 in zip(flag_enc, flag_format)])
    key = (key_part.decode('ISO-8859-1') + "y").encode('ISO-8859-1')

    print("La llave es: ",key.decode('ISO-8859-1'))

    for i in range((len(flag_enc) // len(key))):

        key += (key.decode('ISO-8859-1') + "myXORkey").encode('ISO-8859-1')

    flag = bytes([a ^ b for a,b in zip(key, flag_enc)])
    print(flag.decode('ISO-8859-1'))
    
flag_enc_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
flag_enc = bytes.fromhex(flag_enc_hex)
flag_format = b"crypto{"
xor()

# El formato de la flag es: crypto{}, por lo tanto vamos a hacer la XOR entre la flag_enc y format_flag
# para calcular parte de la Key el resultado es myXORke, suponemos que el siguiente caracter es myXORkey
# ahora suponemos que la llave es la mencionada anteriormente por lo que debemos de ir repitiendo dicha cadena 
# tantas veces hasta completar flag_enc (division entera siempre).
