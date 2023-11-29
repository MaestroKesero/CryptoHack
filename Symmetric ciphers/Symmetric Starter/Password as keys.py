import requests

def findKey(ciphertext_bytex):

  with open('/usr/share/dict/words') as f:
    for words in f:
      words = words.strip()
      key_try_hex = hashlib.md5(word.encode()).digest()
      key_try_bytes = bytes.fromhex(key_try_hex)
      print(key_try_bytes)
    
  return key_try_bytes

result = result.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ciphertext = result.json()["ciphertext"]
print("La flag cifrada es: ", ciphertext)
ciphertext_bytes = bytes.fromhex(ciphertext_hex)
key = findKey(ciphertext_bytes)


# La clave para romper este ECB, es que si observamos el codigo, podemos observar que la Key se genera 
# de la siguiente forma: 
# with open("/usr/share/dict/words") as f:
#    words = [w.strip() for w in f.readlines()]
# keyword = random.choice(words)
#
# KEY = hashlib.md5(keyword.encode()).digest()
# Por tanto para romper dicho cifrado, necesitamos obtener la clave, para ello realizaremos el proceso inverso
# y posteriormente tendremos que realizar la operacion XOR entre el ciphertext y la Key (En este caso al utilziar Crypto.Utils.AES directamente
# podemos utilizar la funcion decrypt del tiron).

# https://blog.csdn.net/shshss64/article/details/128029134
