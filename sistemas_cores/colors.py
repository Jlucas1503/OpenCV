#Esse codigo divide(ou mescla) a imagem ou video selecionado em canais RGB
import cv2 as cv
import numpy as np #lib para trabalhar com arrays e matrizes de varias dimensoes

imagem = cv.imread("imagens/pessoas.jpg")
azul, verde, vermelho = cv.split(imagem)

# CASO QUISERMOS VIZUALIZAR A IMAGEM SOMENTE COM UM CANAL DE CORES 
""" zero = np.zeros_like(azul) # Cria uma array de zeros de mesmo tipo(mesmas dimensoes) do array Azul

somenteAzul = cv.merge([azul, zero, zero]) # Funcao merge() combina canais/arrays
somenteVerde = cv.merge([zero, verde, zero])

cv.imshow("Somente AZUL", somenteAzul)
cv.imshow("Canal AZUL", azul)
 """

cv.imshow("Canal AZUL", azul)
cv.imshow("Canal verde", verde)
cv.imshow("Canal vermelho", vermelho) 

cv.imwrite("imagens/pessoasAzul.jpg", azul)
cv.imwrite("imagens/pessoasVerde.jpg", verde)
cv.imwrite("imagens/pessoasVermelho.jpg", vermelho)
cv.waitKey(0)
cv.destroyAllWindows()