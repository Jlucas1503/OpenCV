import cv2 as cv
import numpy as np
import matplotlib as grafico

#ler imagem
ponteiros = cv.imread("/home/lucasmint/Documentos/OpenCV/imagens/folha.jpg")

#ler o numero de linhas, em seguida o numero de colunas - funcao Shape()
totalLinhas, totalColunas, ca = ponteiros.shape

cv.imshow("Imagem original", ponteiros)

# criamos uma matriz que recebe o centro da imagem e desloca '90' graus em scale=1
# !! Se atentar com a ordem de parametros!
matrizRotacionada = cv.getRotationMatrix2D((totalColunas / 2, totalLinhas / 2), 90, 1)

# a funcao warpAffine recebe a imagem e rotaciona de acordo com a matriz nova
# --> warpAffine(src, matriz, dsize)
imagemRotacionada = cv.warpAffine(ponteiros, matrizRotacionada, (totalColunas, totalLinhas))

cv.imshow("Imagem rotacionada", imagemRotacionada)
cv.waitKey(0)
cv.destroyAllWindows()

