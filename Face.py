from cv2 import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    hi,im = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #eye = eye_cascade.detectMultiScale(gray, 1.1, 2)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 250, 0), 2)

    #for (x, y, w, h) in eye:
        #cv2.rectangle(im, (x, y), (x+w, y+h), (50, 0, 0), 1)
    # Display
    cv2.imshow('Face Detection', im)
    if cv2.waitKey(1000//12)&0xff == ord("q") :
            break

