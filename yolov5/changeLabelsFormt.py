import os
import cv2

def main():
    try:
        os.mkdir("labelsWork/")
    except OSError:
        print ("Creation of the directory failed")
    else:
        print ("Successfully created the directory")
    labels = os.listdir('Labels/')
    for label in labels:
        h,w = getImageSize(label)
        fileName = "labelsWork/" + label
        label = "Labels/" + label
        with open(label, 'r') as f:
            createNewfile(fileName,f.readlines(), h, w)

def createNewfile(fileName,data, h, w):
    i = 1
    labal = ""
    while(i <= int(data[0])):
        labels = data[i]
        print("i:" , i)
        labels = labels.replace('\n', '')
        li = list(labels.split(" ")) 
        W = ((int(li[2]) - int(li[0])))
        H = ((int(li[3]) - int(li[1])))
        x_center = ((W/2) + (int(li[0]))) / w 
        y_center = ((H/2) + (int(li[1]))) / h
        labal += "0 " + str(x_center) + " " + str(y_center) + " " + str(W/w) + " " + str(H/h) + " \n" 
        i += 1
    file_object  = open(fileName, "w+") 
    file_object.write(labal)

def getImageSize(label):
    print(label)
    image = label.replace('txt', 'jpeg')
    im = cv2.imread('images/' + image)
    h, w, c = im.shape
    return h,w


if __name__ == "__main__":
    main()
 