#Esse código faz a conversao do sistema RGB para o HSR, amplamente usado em processamento digital de imagens
#Esse etapa faz parte da segmentacao, e possui enorme importantancia
""" OBS: caso tivermos interesse em exibir as imagens mescladas em HSV, precisamos converter em RGB, pois os
 monitores padroes usam RGB como canais de cor
 """
import cv2 as cv

imagem = cv.imread("imagens/rebanho.jpg")

imagem = cv.cvtColor(imagem, cv.COLOR_BGR2HSV)

matiz, saturacao, valor = cv.split(imagem) #separa em tres caracteristicas diferentes

cv.imshow("matiz", matiz)
cv.imshow("saturacao", saturacao)
cv.imshow("valor", valor)

cv.waitKey(0)
cv.destroyAllWindows()
