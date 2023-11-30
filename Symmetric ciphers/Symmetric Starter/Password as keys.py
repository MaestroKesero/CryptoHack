import requests
import tqdm
import haslib
import random
import binascii
from Crypto.Cipher import AES
from Crypto.Utils.Number import *

# Obtenemos la flag cifrada
result = result.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ciphertext = result.json()["ciphertext"]
print("La flag cifrada es: ", ciphertext)
ciphertext_bytes = bytes.fromhex(ciphertext)

# Rompemos key
with open('/usr/share/dict/words.txt','r') as f:
 for words in f:
      words = words.strip()
      key_try_hex = hashlib.md5(word.encode()).digest()
      key_try_bytes = bytes.fromhex(key_try_hex)
      #print(key_try_bytes) 

      # Comprobamos posible key
      result_flag = result_flag.get('/passwords_as_keys/decrypt/{ciphertext_bytes}/{key}/')
      flag_try = result_flag.json()["plaintext"]
      print(f"Posible flag: {flag_try}, llave utilizada: {key}")

      # Guardamos posibles flags
      with open('all_flags.txt', 'w') as flags:
      structure = f"Posible flag: {flag_try}, llave utilizada: {key}"
      flags.write(sructure)


# La clave para romper este ECB, es que si observamos el codigo, podemos observar que la Key se genera 
# de la siguiente forma: 
# with open("/usr/share/dict/words") as f:
#    words = [w.strip() for w in f.readlines()]
# keyword = random.choice(words)
#
# KEY = hashlib.md5(keyword.encode()).digest()
# Por tanto para romper dicho cifrado, necesitamos la llave que la conseguimos computando todos los valores de key
# Posteriormente descifraremos con dicha clave y el ciphertexto y por ultimo buscaremos la flag.
# Podemos buscar la flag mediante un grep del archivo o de forma mas sencilla, utilizando if b'crypto{ in flag_try: print(flag_try)

# https://blog.csdn.net/shshss64/article/details/128029134

# Buscamos en el fichero y encontramos: Posible flag: b'crypto{k3y5__r__n07__p455w0rdz?}', llave utilizada: d3e23f1eb6e79ed51133e0da48e98d4a (linea 26931)
# Por mera curiosidad, para encontrar la palabra de la cual proviene dicho hash_key, hacemos un decript online de dicho hash md5 y encontramos: bluebell
# Tardo en hacer 40000 posibles flags unas 2 horas 5 min.
