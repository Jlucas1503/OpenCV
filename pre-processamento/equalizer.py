import cv2 as cv
import numpy as np
import matplotlib.pyplot as grafico

maquina_original = cv.imread("/home/lucasmint/Documentos/OpenCV/imagens/ponteiros.jpg", 0)

maquina_equalizada = cv.equalizeHist(maquina_original) # funcao para equalizar o contraste

cv.imshow("Imagem Original", maquina_original)
cv.imshow("Imagem equalizada", maquina_equalizada)

grafico.hist(maquina_original.ravel(), 256, [0,256])
grafico.figure("Figura equalizada")
grafico.hist(maquina_equalizada.ravel(), 256, [0,256])

grafico.show()

cv.waitKey(0)
cv.destroyAllWindows()







