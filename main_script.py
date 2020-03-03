import cv2

image = cv2.imread("picture.jpg")

face_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor= 1.1,
    minNeighbors= 5,
    minSize=(10, 10)
)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
cv2.imshow("Original image", image)
cv2.waitKey(0)

