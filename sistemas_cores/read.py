import cv2 as cv

img = cv.imread("imagens/carros.jpg")

cap = cv.VideoCapture(0)
while(True):
    # Captura frame por frame
    ret,frame = cap.read()
    # mostra os frame em tempo real
    cv.imshow('frame',frame)
    if cv.waitKey(20) & 0xFF == ord('q'): #letra q para fechar a camera#
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows() 