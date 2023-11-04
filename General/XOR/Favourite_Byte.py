def xor():
    
    flag = bytes.fromhex(flag_hex)
    
    for possible_key in range(256):
    
        decrypted_data = bytes([byte ^ possible_key for byte in flag])
        
        if(decrypted_data.decode('ISO-8859-1').startswith("crypto")):
            print(f"Flag encontrada: {decrypted_data.decode('utf-8')} con el byte favorito: {possible_key}")
    
flag_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d" 
xor()

# Los posibles bytes van de 0 a 256, entonces vamos operando y vamos imprimiendo valores
# comprobamos si una cadena imprimida empieza con crypto y si se cumple la imprimimos