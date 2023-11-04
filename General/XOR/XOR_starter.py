from pwn import xor

def xor_pwn():

    result_pwn = xor(label, number)
    flag = f"crypto{{{result_pwn.decode('ISO-8859-1')}}}"
    print("La forma xor() es:",flag)

def xor_manually():

    result_manually_bytes = bytes([a ^ number for a in label])
    result_manually = result_manually_bytes.decode('ISO-8859-1')
    flag = f"crypto{{{result_manually}}}"
    print(f"La forma manual de XOR es: ",flag)
    
    
label = b'label' #Ya esta en bytes, no necesitamos label.encode('ISO-8859-1')
number = 13

xor_pwn()
xor_manually()
