import cv2, pickle
# Creating an object. Two for usb webcam
# If error, try 0, 1, 2, ... until success
video = cv2.VideoCapture(2)
# counter for the while loop
a = 0
# counter for the buffer file
frame_count = 0
while True:
    # Create a frame object
    check, frame = video.read()
    print(check)
    print(frame)
    # Show the frame
    cv2.imshow("Capturing", frame)
    # For streaming, press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        f.close()
        break
    # creates buffer file, one file for 500 frames
    if a % 500 == 0:
        # close the file if previous one has finished writing
        if a != 0:
            f.close()
        # create file, number as index
        f = open("{}.frames".format(frame_count), "ab")
        frame_count += 1
        # append bitstream to end of file
        f.write(pickle.dumps(frame, protocol=0))
    else:
        f.write(pickle.dumps(frame, protocol=0))
    a = a + 1
video.release()

cv2.destroyAllWindows
