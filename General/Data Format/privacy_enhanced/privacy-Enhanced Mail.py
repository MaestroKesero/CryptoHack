from Crypto.PublicKey import RSA
import base64

def import_Key():

    with open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem","r") as key_file:

        private_key = RSA.importKey(key_file.read())
        dec_d = private_key.d 
        decimal_value = int(dec_d)
        print("El valor en decimal de la clave privada es: ", decimal_value)

import_Key()


# Para leer el entero decimal de una clave RSA importada tanto publica como privada,
# tenemos que abrir la clave (en este caso pem) y posteriormente leemos el componente
# privado con .d que es un numero entero, o tambien podemos leer el modulo con .n

# NOTA: Apuntes encontrados valiosos

#https://letsencrypt.org/docs/a-warm-welcome-to-asn1-and-der/
#https://www.cryptologie.net/article/260/asn1-vs-der-vs-pem-vs-x509-vs-pkcs7-vs/