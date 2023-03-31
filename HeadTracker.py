import cv2
import os
import time

cap = cv2.VideoCapture(0)

# Define the Haar cascade classifier for face detection
cascPath= os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml" # Gets the opencv training data
face_cascade = cv2.CascadeClassifier(cascPath)  # The face detector object with the pre-loaded training data

# Set the initial position of the face
y_prev = 0
head_pos_prev = 0

bop_counter =0

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Iterate over each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Update the previous y position of the face


    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Check for quit command
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
