import cv2
import os

SOURCE_DIR = "C:/temp/test_infer/"
TARGET_DIR = "C:/temp/gray_infer/" #make sure this dir exists before run




for count, filename in enumerate(os.listdir(SOURCE_DIR)): 
    print(filename) 
    originalImage = cv2.imread(SOURCE_DIR + filename)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    
    # (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    
    cv2.imwrite(TARGET_DIR + filename, grayImage)  
