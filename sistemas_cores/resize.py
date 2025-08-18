import cv2 as cv

def resizeImg (frame, scale=0.5):
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)
    dimensao = (largura, altura)

    return cv.resize(frame, dimensao, interpolation=cv.INTER_AREA)

# lê uma imagem de repositorio e guardar na var img
img = cv.imread("imagens/carros.jpg")

img_resized = resizeImg(img, scale=0.3) # redimensiona a img e guarda isso em uma nova var

cv.imshow("carros", img_resized)
cv.waitKey(0)