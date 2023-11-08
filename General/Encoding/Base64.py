import base64

def HexToBase64():
    
    number_bytes = bytes.fromhex(number_hex)
    number_base64 = base64.b64encode(number_bytes)
    print(number_base64)
    
number_hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
HexToBase64()

# Esta funcion transforma un numero hexadecimal a bytes y 
# posteriormente a base64
