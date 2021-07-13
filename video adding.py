import cv2
import numpy as np
vid=cv2.VideoCapture(0)
img1=cv2.imread('resource/bag.jpg')
img2=cv2.imread('resource/bag2.jpg')
img3=cv2.imread('resource/bag3.jpg')
img4=cv2.imread('resource/bag4.jpg')
img5=cv2.imread('resource/bag5.jpg')
img6=cv2.imread('resource/bag6.jpg')
i=int(input())
while True:
    flag,frame=vid.read()
    if not flag:
        print('cant access')
        break
    if i==1:
        img1 = cv2.resize(img1, (frame.shape[1], frame.shape[0]))
        blended_img1 = cv2.addWeighted(frame, 0.8, img1, 0.3, gamma=0.1)
        cv2.imshow('blended1', blended_img1)
        cv2.waitKey(10)
    elif i==2:
        img2 = cv2.resize(img2, (frame.shape[1], frame.shape[0]))
        blended_img2 = cv2.addWeighted(frame, 0.8, img2, 0.3, gamma=0.1)
        cv2.imshow('blended2', blended_img2)
        cv2.waitKey(10)
    elif i==3:
        img3 = cv2.resize(img3, (frame.shape[1], frame.shape[0]))
        blended_img3 = cv2.addWeighted(frame, 0.8, img3, 0.3, gamma=0.1)
        cv2.imshow('blended3', blended_img3)
        cv2.waitKey(10)
    elif i==4:
        img4 = cv2.resize(img4, (frame.shape[1], frame.shape[0]))
        blended_img4 = cv2.addWeighted(frame, 0.8, img4, 0.3, gamma=0.1)
        cv2.imshow('blended4', blended_img4)
        cv2.waitKey(10)
    elif i==5:
        img5 = cv2.resize(img5, (frame.shape[1], frame.shape[0]))
        blended_img5 = cv2.addWeighted(frame, 0.8, img5, 0.3, gamma=0.1)
        cv2.imshow('blended5', blended_img5)
        cv2.waitKey(10)
    elif i==6:
        img6 = cv2.resize(img6, (frame.shape[1], frame.shape[0]))
        blended_img6 = cv2.addWeighted(frame, 0.8, img6, 0.3, gamma=0.1)
        cv2.imshow('blended6', blended_img6)
        cv2.waitKey(10)
    k=cv2.waitKey(10)
    if k & 0xFF==ord('q'):
        break