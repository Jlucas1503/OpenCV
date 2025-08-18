# Converter os canais RGB de uma imagem para valores cinza
import cv2 as cv

imagem = cv.imread("imagens/pessoas.jpg")


imagemAlterada = cv.cvtColor(imagem, cv.COLOR_RGB2GRAY) # RBG to GRAY, ou seja, converte RGB em cinza e guarda em 'imagem'

cv.imshow("RGB2GRAY", imagem)
cv.imshow("imagem Cinza", imagemAlterada)
cv.waitKey(0)
cv.destroyAllWindows()

""" DETALHAMENTO MATEMATICA/TEORICO --> a imagem em tons de cinza, após a
conversão, é gerada a partir da soma ponderada dos canais de cor vermelho,
verde e azul. Nessa soma, os canais vermelho e verde apresentam um peso
(coeficiente de ponderação) maior quando comparado ao canal azul,
justamente pelo fato do olho humano ser mais sensível a essas cores.
Os coeficientes de ponderação são diferentes para cada canal, e todos são
padronizados e definidos com base na resposta perceptual do olho humano
para cada uma dessas cores. """