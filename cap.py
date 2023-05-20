import cv2

name = input("Name: ")

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('c'):
        cv2.imwrite('faces/'+name+".jpg", img)
        break

cap.release()
cv2.destroyAllWindows()
