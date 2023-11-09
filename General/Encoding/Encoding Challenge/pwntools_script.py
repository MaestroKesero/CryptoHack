from pwn import * # pip install pwntools
from Crypto.Util.number import long_to_bytes
import json
import codecs, base64

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode(encoded_string, encoded_type):

    if (encoded_type == "base64"):
        return base64.b64decode(encoded_string).decode('iso-8859-1')
    elif (encoded_type == "hex"):
        return bytes.fromhex(encoded_string).decode('iso-8859-1')
    elif (encoded_type == "rot13"):
        return codecs.decode(encoded_string, "rot13")
    elif (encoded_type == "bigint"):
        return long_to_bytes(int(encoded_string, 16)).decode('iso-8859-1')
    else:
        #(encode_type == "utf-8"):
        return ''.join(chr(i) for i in encoded_string)

for i in range (101):

    received = json_recv()
    print("Received type: ")
    print(received["type"])
    encoded_type = received["type"]

    print("Received encoded value: ")
    print(received["encoded"])
    encoded_string = received["encoded"]
    
    to_send = {
    "decoded": decode(encoded_string, encoded_type)
    }
    json_send(to_send)

# Para comenzar este problema tenemos saber el formato de como vamos a recibir el json para ello ejecutamos
# el script y vemos que recibimos los objetos de esta manera Received type: hex  Received encoded value: 736f7272795f67736d5f636f6d7061726174697665
# posteriormente tratamos dicha informacion y la mandamos a la funcion para que la interprete
# He modificado el codigo de tal manera que metamos dentro de un bucle con 100 iteraciones y la 101 corresponde con la flag