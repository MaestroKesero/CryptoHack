import requests

result = result.get('https://aes.cryptohack.org/block_cipher_starter/encrypt_flag')
ciphertext = result.json()["ciphertext"]
print("El texto cifrado recibido es: ",ciphertext)

result_message = result_message.get('https://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertext}')
flag_hex = flag_hex.json()["plaintext"]
flag = bytes.fromhex(flag_hex)
print("La flag es: ", flag)


# Este ejercicio es muy simple, simplemente presionamos encrypt_flag() para obtener el hash de la flag, posteriormente
# introduciremos dicho Hash en decrypt_flag() y por ultimo pasaremos dicho texto en hexadecimal a texto claro.
# crypto{bl0ck_c1ph3r5_4r3_f457_!}

# Debido a la simplicidad de este ejercicio, he decidido aprender a hacer scripting en bash con peticiones HTTP y trabajar con json
