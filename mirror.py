# pip install opencv-python
# pip install numpy
# pip install mss
# pip install Pillow

# Horizontally mirrors the screen to be displayed on an autocue

import numpy as np
import cv2
from mss import mss
from PIL import Image
import time

bounding_box = {
    'top': 100,
    'left': 0,
    'width': 1920,
    'height': 1080
}
display_fps = False
window_name = 'Potvos Autocue'

prev_frame_time = 0
new_frame_time = 0

sct = mss()

while True:

    sct_img = np.array(sct.grab(bounding_box)) # Grab screen image and convert to matrix
    flipped = cv2.flip(sct_img, 1) # Flip matrix horizontally

    # FPS indicator
    if display_fps:
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time) 
        prev_frame_time = new_frame_time 
        fps = int(fps) 
        fps = str(fps) 
        cv2.putText(flipped, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA) 
  
    cv2.imshow(window_name, flipped) # Display flipped screen with interface

    # Keyboard q to quit
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break

    # Close button is used
    if cv2.getWindowProperty(window_name, 0) < 0:
        break