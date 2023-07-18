import cv2

path = r"C:\\Users\\shash\\Downloads\\jonny.jpg"
img = cv2.imread(path)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()