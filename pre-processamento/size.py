import cv2 as cv

imagem = cv.imread("imagens/carros.jpg")
divisao = imagem.size / 3 #dividimos por tres para dsconsiderar a qntd de canais da imagem
print("Tamanho em bytes:", divisao, "bytes")
