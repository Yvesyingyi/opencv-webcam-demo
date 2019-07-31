import cv2, pickle
import numpy as np
# Creating an object. Two for usb webcam
# If error, try 0, 1, 2, ... until success
video = cv2.VideoCapture(2)
# Check if camera opened successfully
if (video.isOpened() == False): 
    print("Unable to read camera feed")
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# counter for the while loop
a = 0
# counter for the buffer file
frame_count = 0
while True:
    # Create a frame object
    check, frame = video.read()
    # Show the frame
    cv2.imshow("Capturing", frame)
    # For streaming, press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        out.release()
        break
    # creates buffer file, one file for 500 frames
    if a % 600 == 0:
        # close the file if previous one has finished writing
        if a != 0:
            out.release()
        # create file, number as index
        out = cv2.VideoWriter("{}.mp4".format(frame_count),fourcc, 24.0, (frame_width,frame_height))
        frame_count += 1
        # Write the frame into the file 'output.avi'
        out.write(frame)
    else:
        # Write the frame into the file 'output.avi'
        out.write(frame)
    a = a + 1
video.release()

cv2.destroyAllWindows
