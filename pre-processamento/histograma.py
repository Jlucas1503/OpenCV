import cv2 as cv
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv.imread("imagens/placas_eletronicas.bmp") #imagem colorida

azul, verde, vermelho = cv.split(imagem) # Separa em tre canais de cores RGB

grafico.hist(azul.ravel(), 256, [0, 256]) #histograma em azul
grafico.figure() # cria uma figura nova
grafico.hist(verde.ravel(), 256, [0, 256]) #histograma em verde
grafico.figure()
grafico.hist(vermelho.ravel(), 256, [0, 256]) #histograma em vermelho


grafico.show() #mostra os gradifos

cv.waitKey(0)
cv.destroyAllWindows()