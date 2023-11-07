from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def obtainModule():

    with open("bruce_rsa.pub","rb") as file:

        public_key = serialization.load_ssh_public_key(file.read())
        n_hex = public_key.public_numbers().n
        n_decimal = int(n_hex)
        
        print("El valor decimal del modulo es: ", n_decimal)

obtainModule()

# He probado otras alternativas con paramiko y OpenSSl pero no funcionan debido 
# a que necesitan claves publicas y privadas de RSA, nosotros queremos cargar
# claves publicas ssh con formato OpenSSH por lo que haremos la siguiente manera
# no podemos obtener el exponente privado debido a que este solo lo podemos obtener
# en claves privadas.
# Nosotros lo que estamos haciendo es obtener el modulo n de la clave publica .pub
# y transformarla en decimal para calcular el entero correspondiente.