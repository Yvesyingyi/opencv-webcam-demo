import cv2
import time
 

 
# Start default camera
video = cv2.VideoCapture(2)
    
# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    
# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.
    
if int(major_ver)  < 3 :
    fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {}".format(fps))
else :
    fps = video.get(cv2.CAP_PROP_FPS)
    print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {}".format(fps))
    

# Number of frames to capture
num_frames = 120
    
    
print ("Capturing {} frames".format(num_frames))

# Start time
start = time.time()
    
# Grab a few frames
for i in range(0, num_frames) :
    ret, frame = video.read()

    
# End time
end = time.time()

# Time elapsed
seconds = end - start
print ("Time taken : {} seconds".format(seconds))

# Calculate frames per second
fps  = num_frames / seconds
print ("Estimated frames per second : {}".format(fps))

# Release video
video.release()