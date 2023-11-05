import cv2

def xor_images():

    xor_result = cv2.bitwise_xor(image1, image2)

    cv2.imshow('Imagen XOR', xor_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('Imagen Resultante.png', xor_result)


image1 = cv2.imread('flag.png')
image2 = cv2.imread('lemur.png')
xor_images()

# Para hacer XOR con dos imagenes (pixeles) necesitamos utilizar cv2.
# No necesitamos pasarlos a bytes por que vamos a operar pixel a pixel
#
# Explicacion detallada ChatGPT
# La operación XOR (bitwise XOR) entre píxeles en imágenes funciona comparando
# los bits correspondientes de los píxeles en dos imágenes y generando una nueva
# imagen donde cada bit del píxel resultante se calcula aplicando la operación XOR
# a los bits correspondientes de las dos imágenes originales.
#
# La operación XOR es una operación a nivel de bits que devuelve 1 si los bits comparados son diferentes 
# y 0 si son iguales. Aquí hay un ejemplo simple que ilustra cómo funciona la operación XOR con dos píxeles 
# en imágenes binarias (blanco y negro):

# NOTA IMPORTANTE:

# Cuando aplicas una operación XOR entre un píxel verde y un píxel rojo, 
# el resultado dependerá de los valores numéricos de los componentes de color
# en cada canal (rojo, verde y azul) en el modelo de color RGB (Red, Green, Blue).

# En el modelo de color RGB, cada canal tiene un valor que varía de 0 a 255,
# donde 0 significa que ese canal está apagado (sin color) y 255 significa que 
# está completamente encendido (máxima intensidad de color). En el caso de un píxel 
# verde y un píxel rojo, sus valores típicos pueden ser:

# Píxel verde: (0, 255, 0) (sin rojo, con verde, sin azul)
# Píxel rojo: (255, 0, 0) (con rojo, sin verde, sin azul)
# Ahora, aplicando XOR bit a bit entre los valores en los canales:

# Rojo: 0 XOR 255 = 255 (completamente encendido en rojo)
# Verde: 255 XOR 0 = 255 (completamente encendido en verde)
# Azul: 0 XOR 0 = 0 (sin azul)
# Entonces, el resultado del píxel sería (255, 255, 0), que corresponde a un color amarillo 
# (completamente encendido en rojo y verde, sin azul). Por lo tanto, al aplicar XOR entre un 
# píxel verde y uno rojo, el color resultante sería amarillo.
