#Verifica 1 - a quantidade de linha, 2 - colunas, 3 - qntd de canais

import cv2 as cv

imagem = cv.imread("imagens/moedas02.jpg")

print("a imagem possui:", imagem.shape)
