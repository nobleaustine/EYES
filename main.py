# libraries for
import cv2           # computer vision
import numpy as np   # matrix operations
import dlib           # machine learning face detectioncd path\to\dist
from math import hypot # to calculate the distance
import time

# 0 : access default camera
camera = cv2.VideoCapture(0)

# face detector
detector = dlib.get_frontal_face_detector()

# predict landmarks : dat file face landmarks
predictor = dlib.shape_predictor('C:\\NOBLEAUSTINE\\GitWorld\\EYES\\shape_predictor_68_face_landmarks.dat')

font = cv2.FONT_HERSHEY_PLAIN
count = 0
time_taken = .00001
# infinite loop till esc is pressed 
while True:
    start_time = time.time()   
    # camera.read() return two values boolean for successful capture and captureed frame
    # here boolean is ignored by _
    _,frame = camera.read()
   
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # save computation : grayscale conversion
    faces = detector(gray)                         # detect faces in the frame
    
    for face in faces:
       
       # drawing box around faces
       # x,y = face.left(),face.top()
       # x1,y1 = face.right(),face.bottom()
       # cv2.rectangle(frame,(x,y),(x1,y1),(0,225,0),2)
       
       x,y = face.right(),face.top()
       # detected land marks as in dat file
       landmarks = predictor(gray,face)
       
       # right eye point pairs from top to down
       RE1 = (landmarks.part(43).x,landmarks.part(43).y)
       RE2 = (landmarks.part(44).x,landmarks.part(44).y)
      
       RE3 = (landmarks.part(42).x,landmarks.part(42).y)
       RE4 = (landmarks.part(45).x,landmarks.part(45).y)

       RE5 = (landmarks.part(47).x,landmarks.part(47).y)
       RE6 = (landmarks.part(46).x,landmarks.part(46).y)
      
       # midpoints int(pixels != float) of top and bottom to draw vertical line
       RE1 = (int((RE1[0] + RE2[0])/2),int((RE1[1] + RE2[1])/2))
       RE2 = (int((RE5[0] + RE6[0])/2),int((RE5[1] + RE6[1])/2))
      
       # RE : horizontal & vertical line 
       RE_ver_line =  cv2.line(frame,RE1,RE2,(225,0,0),2)
       RE_hor_line =  cv2.line(frame,RE3,RE4,(225,0,0),2)
       
       # length of line
       RE_ver_line_length = hypot((RE1[0]-RE2[0]),(RE1[1]-RE2[1]))
       RE_hor_line_length = hypot((RE3[0]-RE4[0]),(RE3[1]-RE4[1]))
      
       ratio = RE_hor_line_length/RE_ver_line_length
       if ratio > 5 :
         #  cv2.putText(frame,"BLINKING",(50,150),font,3,(225,0,0))
          count += 1
        
       
       blinks_per_minute =round((count/(time_taken))*60,3)
       
       text = f"{blinks_per_minute} {count}"
       cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,0, 0), 2)
       
       
       # left eye point pairs from top to down

       LE1 = (landmarks.part(37).x,landmarks.part(37).y)
       LE2 = (landmarks.part(38).x,landmarks.part(38).y)

       LE3 = (landmarks.part(36).x,landmarks.part(36).y)
       LE4 = (landmarks.part(39).x,landmarks.part(39).y)

       LE5 = (landmarks.part(41).x,landmarks.part(41).y)
       LE6 = (landmarks.part(40).x,landmarks.part(40).y)
       
       # midpoints int(pixels != float) of top and bottom to draw vertical line
       LE1 = (int((LE1[0] + LE2[0])/2),int((LE1[1] + LE2[1])/2))
       LE2 = (int((LE5[0] + LE6[0])/2),int((LE5[1] + LE6[1])/2))
       
       # LE : horizontal & vertical line 
       LE_ver_line =  cv2.line(frame,LE1,LE2,(225,0,0),2)
       LE_hor_line =  cv2.line(frame,LE3,LE4,(225,0,0),2)

    

    
       
    cv2.imshow("EYES",frame) # displaying captured frame
    key = cv2.waitKey(1)     # waits for a key press
   
    if key == ord('q') or key == 27:  # 'q' key or Esc key
            break
   #  if key == 27:
   #     break                 # if key == 27 => esc break loop
    end_time = time.time() 
    time_taken = time_taken + end_time - start_time


camera.release()             # to release the camera
cv2.destroyAllWindows()      # close all OpenCV windows







