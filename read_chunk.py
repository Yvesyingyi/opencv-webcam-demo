import cv2, pickle, time

## Open buffer stream file, "0.frames" for example
f = open("0.frames", "rb")
while 1:
    # load one frame
    try:
        frame = pickle.load(f)
    except EOFError:
        break
    # print the frame for debugging
    print(frame)
    # show frame
    cv2.imshow("Capturing", frame)
    # for streaming, press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    # sleep, for 30fps output
    time.sleep(0.033)
f.close()
