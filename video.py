import cv2
import numpy as np
cap = cv2.VideoCapture("resource/peng.mp4")
while True:
    success, img =cap.read()
    if success:
        vidgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        vidHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        vidBGRA = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        b, g, r = cv2.split(img)
        zeros = np.zeros((img.shape[0], img.shape[1]), np.uint8)
        blue = cv2.merge([b, zeros, zeros])
        green = cv2.merge([zeros, g, zeros])
        red = cv2.merge([zeros, zeros, r])
        cv2.imshow('blue channel', blue)
        cv2.imshow('green channel', green)
        cv2.imshow('red channel', red)
        cv2.imshow('video',img)
        cv2.imshow('videogrey', vidgray)
        cv2.imshow('videohs', vidHSV)
        cv2.imshow('videobge', vidBGRA)
        k=cv2.waitKey(50)
        if k & 0xFF==ord('q'):
            break