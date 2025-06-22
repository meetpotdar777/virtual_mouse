# main.py - AI Virtual Mouse using Hand Gesture Recognition

import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# --- Configuration Parameters ---
SMOOTHING_FACTOR = 7  # Adjust for smoother (higher value) or more responsive (lower value) mouse movement
CLICK_THRESHOLD = 50  # Distance threshold for pinch detection (in pixels) for a click
DRAW_LANDMARKS = True # Set to False to hide hand landmarks on screen

# --- PyAutoGUI setup ---
pyautogui.FAILSAFE = False # Disable failsafe feature to prevent accidental termination (use with caution!)
screen_width, screen_height = pyautogui.size() # Get your screen resolution

# --- MediaPipe Hand Tracking Setup ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,  # Minimum confidence value for hand detection
    min_tracking_confidence=0.7,  # Minimum confidence value for hand tracking
    max_num_hands=1 # Only track one hand for simpler control
)
mp_drawing = mp.solutions.drawing_utils # For drawing hand landmarks

# --- Webcam Initialization ---
cap = cv2.VideoCapture(0) # 0 for default webcam
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# --- Variables for smoothing and tracking ---
prev_x, prev_y = 0, 0 # Previous mouse coordinates for smoothing
curr_x, curr_y = 0, 0 # Current mouse coordinates for smoothing
last_click_time = 0 # To prevent multiple rapid clicks

print("AI Virtual Mouse Started. Press 'q' to quit.")
print("Move your index finger to control the mouse.")
print("Pinch your thumb and index finger together to left click.")

# --- Main Loop ---
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a more natural feel (like a mirror)
    frame = cv2.flip(frame, 1)
    
    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks and control mouse
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if DRAW_LANDMARKS:
                # Draw hand landmarks on the original BGR frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark coordinates for Index Finger Tip (8) and Thumb Tip (4)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            
            # Convert normalized coordinates to pixel coordinates
            index_x = int(index_finger_tip.x * frame_width)
            index_y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            # --- Mouse Movement Logic ---
            # Map index finger position to screen coordinates
            # A simple linear mapping. You might want to define an active region for better control.
            target_mouse_x = np.interp(index_x, [0, frame_width], [0, screen_width])
            target_mouse_y = np.interp(index_y, [0, frame_height], [0, screen_height])

            # Apply smoothing
            curr_x = prev_x + (target_mouse_x - prev_x) / SMOOTHING_FACTOR
            curr_y = prev_y + (target_mouse_y - prev_y) / SMOOTHING_FACTOR

            pyautogui.moveTo(curr_x, curr_y)
            
            # Update previous coordinates for next frame's smoothing
            prev_x, prev_y = curr_x, curr_y

            # --- Left Click Logic (Pinch Gesture) ---
            # Calculate Euclidean distance between index finger tip and thumb tip
            distance = np.sqrt((index_x - thumb_x)**2 + (index_y - thumb_y)**2)
            
            # Check if distance is below click threshold and enough time has passed since last click
            if distance < CLICK_THRESHOLD and (time.time() - last_click_time > 0.5): # 0.5 second debounce
                pyautogui.click()
                last_click_time = time.time()
                print("Left Click!")
                # Visually indicate click on the webcam feed
                cv2.circle(frame, (index_x, index_y), 15, (0, 255, 0), cv2.FILLED)

            # Draw circles on finger tips for visual debugging
            cv2.circle(frame, (index_x, index_y), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 255), cv2.FILLED)

    # Display the frame
    cv2.imshow('AI Virtual Mouse', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
cap.release()
cv2.destroyAllWindows()
print("AI Virtual Mouse stopped.")