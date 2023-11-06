from cryptography import x509
from cryptography.hazmat.backends import default_backend

def Der_to_PEM():

    # Cargar el certificado X.509 en formato DER
    with open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der","rb") as der_file:
        der_data = der_file.read()

    # Cargamos el certificado x.509 desde los datos DER
    cert = x509.load_der_x509_certificate(der_data, default_backend())

    public_key = cert.public_key()
    n = public_key.public_numbers().n
    dec_value = int(n)
    print("El valor decimal del modulo es: ", dec_value)

Der_to_PEM()

# Para calcular el modulo del certificado Der, necesitamos cargar el certificado x509 en DER
# Posteriormente tenemos que acceder a diferentes componentes del certificado para ello utilizamos
# La función load_der_x509_certificate toma los datos DER del certificado y el backend, y devuelve un 
# objeto Certificate que representa el certificado X.509. A partir de ese objeto, puedes acceder a diferentes 
# componentes del certificado, como la clave pública, el módulo n y otros detalles del certificado. 
# En el código anterior, estamos interesados en obtener la clave pública y su módulo n.
#
# Conceptos a aclarar y es que no podemos convertir x509 de DER a PEM y luego leer el modulo de la clave RSA porque no es un RSA
# Por tanto necesitamos utilizar este metodo, ademas dejo en forma de apuntes la manera de pasar DER a PEM mediante openssl
# y mediante un script realizado en python.
#
# Podemos convertir el contenido de DER a PEM de la siguiente manera:
#
# PEM to DER
#
#from OpenSSL import crypto
#
#with open("privacy_enhanced_mail.pem","rb") as keyfile:
#    cert_file = keyfile.read()
#    cert_pem = crypto.load_certificate(crypto.FILETYPE_PEM, cert_file)
#    cert_der = crypto.dump_certificate(crypto.FILETYPE_ASN1, cert_pem)
#
# PEM to DER openssl
# the der file has been atfirst converted into pem file using the below command
# openssl x509 -inform DER -outform PEM -in 2048b-rsa-example-cert.der -out 2048b-rsa-example-cert.pem
#
# Script en python para cambiar de DER a PEM
#
#from pyasn1.codec.der import decoder
#import base64
#
# Cargar el archivo DER
#with open("certificado.der", "rb") as der_file:
#    der_data = der_file.read()
#
# Decodificar el archivo DER
#decoded_der = decoder.decode(der_data)
#
# Codificar el archivo PEM
#pem_data = base64.b64encode(der_data).decode('utf-8')
#
# Agregar saltos de línea cada 64 caracteres (o el número deseado)
#formatted_pem = "\n".join([pem_data[i:i+64] for i in range(0, len(pem_data), 64)])
#
# Formatear el archivo PEM con encabezados y pies
#formatted_pem = "-----BEGIN CERTIFICATE-----\n" + formatted_pem + "\n-----END CERTIFICATE-----"
#
# Guardar el archivo PEM
#with open("certificado.pem", "w") as pem_file:
#    pem_file.write(formatted_pem)
