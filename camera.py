import cv2
import numpy as np
import random
import os
import time
haar = None
now = None
out = None
fps = 20

def main():
    global out
    global now
    global haar
    if(os.path.exists('output.mp4')):
        os.remove('output.mp4')
    cap = cv2.VideoCapture(0)
    if (cap.isOpened() == False):
        print("Error Opening Files")
    vsize = (int(cap.get(3)),int(cap.get(4)))
    haar = cv2.CascadeClassifier('haar.xml')
    out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps,vsize)
    now = time.time()
    while True:
        read_show(cap,out)
    cap.release()
    out.release()

def read_show(cap,out):
    print_time("s:")
    ret,frame = cap.read()
    if(ret == 0):
        quit()
    find_faces(frame)
    cv2.imshow("Frame",frame)
    writefile(frame)
    cv2.waitKey(1)

def find_faces(frame):
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

def print_time(tr):
    # print (now)
    pass

def writefile(frame):
    global now
    global out
    new = time.time()
    diff = new - now
    now = new
    t = int(diff*fps)
    print (t)
    for i in range(t):
        out.write(frame)

main()