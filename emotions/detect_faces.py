import numpy as np
import cv2

## Haarcascade for eyes face and mouth
face_cascade = cv2.CascadeClassifier('/Users/edwin/facerecon/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Users/edwin/facerecon/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('/Users/edwin/facerecon/haarcascade_smile.xml')
feliz_cascade = cv2.CascadeClassifier('/Users/edwin/emotions/cascades/smiling.xml')
bored_cascade = cv2.CascadeClassifier('/Users/edwin/emotions/cascades/bored2.xml')

#First create a caption
caption = cv2.VideoCapture(0)

while 1:
    ret, img = caption.read()
#Let´s first convert into gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detect face using OpenCV detectMultiScale which will draw a rectangle in your face
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#Create a text
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    TopLeft = (100,100)
    fontScale              = 2
    fontColor              = (184,194,4)
    lineType               = 2
#Title
    cv2.putText(img,'Lets read your emotions!!',
        TopLeft,
        font,
        fontScale,
        fontColor,
        lineType)
    caras = feliz_cascade.detectMultiScale(gray,1.3,5)
    bored_face = bored_cascade.detectMultiScale(gray,1.3,5)
##This will detect the face and if true will apply the cascade
    face_detected = False
    for (x,y,w,h) in caras:
        if w > 0:
            face_detected = True

            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'According to the machine you are happy',(0,130),font, 1, (200,255,155))
        #    cv2.imshow("face having name",img)

#pass the image to gray
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
##Eyez are going to be detected by green color RGB
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
##Mouth will be detected by a soft green, althouh by testing it the accuracy of the mouth is very low
## Only when smiling is detected

        mouth = mouth_cascade.detectMultiScale(roi_gray,1.8,20)
        for (mx,my,mw,mh) in mouth:
            if w > 0:
                face_detected = True

                cv2.rectangle(roi_color,(mx,my),((mx+mw),(my+mh)),(112,172,78),2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(roi_color,'You are smiling',(0,130),font, 1, (200,255,155))
            #cv2.rectangle(roi_color,(mx,my),((mx+mw),(my+mh)),(112,172,78),2)



    cv2.imshow('Real time picture',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

caption.release()
cv2.destroyAllWindows()
