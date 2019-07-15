import cv2

haar_face_cascade = cv2.CascadeClassifier('haar.xml')

test1 = cv2.imread('2.jpg')
gray_img = cv2.cvtColor(test1,cv2.COLOR_BGR2GRAY)

cv2.imshow("Test Image",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2);
print(faces) 

for (x, y, w, h) in faces:     
    cv2.rectangle(test1, (x, y), (x+w, y+h), (100, 255, 20), 2)

cv2.imshow("Test Image",test1)

cv2.waitKey(0)
cv2.destroyAllWindows()