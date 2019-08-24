import cv2
from os.path import isfile,join

image = cv2.imread('/Users/edwin/emotions/downloads/happy_people/13.jpg')
resized = cv2.resize(image, (50,50))
dstpath = "/Users/edwin/emotions/" # Destination Folder

cv2.imwrite("Image_Happy.jpg",resized)
#cv2.imwrite('/Users/edwin/emotions/',resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
