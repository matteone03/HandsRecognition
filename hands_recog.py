import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

# Initialize mediapipe drawing utilities and hands module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Open the webcam (index 0)
cap = cv2.VideoCapture(0)

# Initialize the Hands module with detection and tracking confidence thresholds
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Convert BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip the image horizontally
        image = cv2.flip(image, 1)
        
        # Set the image flag to non-writeable for efficient processing
        image.flags.writeable = False
        
        # Process hand detections using the Hands module
        results = hands.process(image)
        
        # Set the image flag to writeable for rendering
        image.flags.writeable = True
        
        # Convert RGB back to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Print hand detection results
        print(results)
        
        # Render hand landmarks and connections on the image
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
        
        # Show the image with hand landmarks
        cv2.imshow('Camera', image)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()

# Create a directory to save output images
os.mkdir('Output Images')
cap = cv2.VideoCapture(0)

# Initialize the Hands module with detection and tracking confidence thresholds
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Convert BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip the image horizontally
        image = cv2.flip(image, 1)
        
        # Set the image flag to non-writeable for efficient processing
        image.flags.writeable = False
        
        # Process hand detections using the Hands module
        results = hands.process(image)
        
        # Set the image flag to writeable for rendering
        image.flags.writeable = True
        
        # Convert RGB back to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Print hand detection results
        print(results)
        
        # Render hand landmarks and connections on the image
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
        
        # Save the image with hand landmarks to the 'Output Images' directory
        cv2.imwrite(os.path.join('Output Images', '{}.jpg'.format(uuid.uuid1())), image)
        
        # Show the image with hand landmarks
        cv2.imshow('Hand Tracking', image)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
