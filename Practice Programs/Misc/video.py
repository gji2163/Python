import cv2 
import numpy as np 

def play(File):
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture(File) 

    # Check if camera opened successfully
    a=cap.read()
    if (a[0]== False): 
        print("Error opening video file")
    else:
        print(a)

    # Read until video is completed 
    while(cap.isOpened()): 
    # Capture frame-by-frame 
        ret,frame = cap.read() 
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # Break the loop 
        else:
            break

    # When everything done, release the video capture object 
    cap.release() 

    # Closes all the frames 
    cv2.destroyAllWindows() 
