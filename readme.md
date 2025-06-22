🖱️ AI Virtual Mouse using Hand Gesture Recognition

This project implements an AI-powered virtual mouse that allows users to control their computer's cursor and perform basic click actions using hand gestures detected via a webcam. It aims to provide an alternative input method, especially useful in scenarios where a physical mouse is inconvenient or inaccessible.

✨ Features

Hand Detection: Real-time recognition of a single hand in the webcam feed.

Cursor Control: Move the mouse cursor by tracking the position of the index finger.

Left Click Gesture: Perform a left-click action by pinching the thumb and index finger together.

Smooth Movement: Incorporates a smoothing factor for more fluid cursor motion.

Visual Feedback: Displays hand landmarks, finger tips, and the click detection on the live webcam feed (can be toggled off).

💡 How It Works

The AI Virtual Mouse leverages the following core libraries and concepts:

OpenCV (cv2): Used for capturing video from the webcam, processing frames (e.g., flipping), and displaying the visual output.

MediaPipe (mediapipe): A powerful framework for on-device machine learning. Specifically, it uses the mp.solutions.hands module to:

Detect hands in the video stream.

Identify 21 distinct 3D landmarks on each hand.

From these landmarks, the project extracts the coordinates of the index finger tip and thumb tip.

PyAutoGUI (pyautogui): A cross-platform GUI automation Python module. It translates the detected hand/finger movements into mouse cursor movements and simulates click events on the operating system level.

Numpy (numpy): Used for numerical operations, particularly for interpolating the finger position to screen coordinates for smoother cursor control.

The system continuously captures video frames, processes them with MediaPipe to find hand landmarks, calculates the screen position based on the index finger, and performs a click if the thumb and index finger are pinched close enough.

🚀 Setup and Installation

To get this project up and running on your local machine, follow these steps:

Clone the repository (or download the code):
If you have Git installed:

git clone <repository_url> # Replace with your repository URL if applicable
cd deep-fake-detection-system # Or the directory where you saved the code

Otherwise, download the virtual_mouse.py file directly.

Create a Virtual Environment (Recommended):
It's good practice to use a virtual environment to manage project dependencies.

python -m venv venv

Activate the Virtual Environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install Required Libraries:
With your virtual environment activated, install the necessary Python packages:

pip install opencv-python mediapipe pyautogui numpy

opencv-python: OpenCV library for computer vision.

mediapipe: Google's framework for ML solutions, used here for hand tracking.

pyautogui: For controlling the mouse.

numpy: For numerical operations.

🎮 Usage

Run the script:

After activating your virtual environment and installing dependencies, navigate to the directory where virtual_mouse.py is saved and run:

python virtual_mouse.py

Control the Mouse:

A webcam feed window will appear.

Move your hand in front of the camera. The tip of your index finger will control the movement of your mouse cursor on the screen.

To perform a left click, bring your thumb and index finger close together (a "pinch" gesture). You'll see a visual indication on the screen and a "Left Click!" message in your terminal.

Quit the application:

Press the 'q' key while the webcam feed window is active.

Alternatively, press Ctrl+C in your terminal.

⚙️ Configuration

You can customize the behavior of the virtual mouse by adjusting the following parameters at the beginning of the virtual_mouse.py file:

SMOOTHING_FACTOR (default: 7):

Controls how smoothly the mouse cursor moves.

Higher values result in smoother but less responsive movement.

Lower values result in more responsive but potentially jumpier movement.

CLICK_THRESHOLD (default: 50):

The maximum pixel distance between the index finger tip and thumb tip to register a click.

Decrease this value if clicks are triggered too easily.

Increase this value if clicks are not registering easily enough.

DRAW_LANDMARKS (default: True):

Set to False if you want to hide the MediaPipe hand landmarks and connections on the webcam feed for a cleaner display.

🚧 Limitations and Future Improvements

This project provides a foundational virtual mouse. Here are some areas for future enhancement:

Additional Gestures: Implement gestures for right-click, double-click, drag-and-drop, scrolling, or specific keyboard shortcuts.

Active Region Definition: Allow users to define a specific rectangular region within the webcam frame that maps to the screen, providing more precise control and reducing accidental movements.

Multi-Hand Support: Extend to support two hands for more complex interactions (e.g., one hand for movement, the other for clicks/scrolling).

Enhanced Smoothing Algorithms: Explore more advanced filtering techniques (e.g., Kalman filters) for even smoother and more accurate cursor tracking.

User Calibration: Implement a simple calibration step for users to adjust sensitivity and click thresholds based on their hand size and preferred interaction style.

Robustness to Lighting/Background: Improve performance in varying lighting conditions or with complex backgrounds.

GUI Interface: Develop a graphical user interface (using Tkinter, PyQt, or web-based frameworks) for easier configuration and feedback.

Developed for Computer Science Projects 🧑‍💻