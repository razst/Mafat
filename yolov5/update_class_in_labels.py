import os
try:  
    os.mkdir("C:/Users/pc/Downloads/BCCD.v1-resize-416x416.yolov5pytorch/train/labelsWork")  
except OSError as error:  
    print(error)  
entries = os.listdir('labels/')
for entry in entries:
    f1 = open("C:/Users/pc/Downloads/BCCD.v1-resize-416x416.yolov5pytorch/train/labelsWork/" + entry, "w+") 
    entry = 'C:/Users/pc/Downloads/BCCD.v1-resize-416x416.yolov5pytorch/train/labels/' + entry
    with open(entry, 'r') as f:
        data = f.readlines()
        i = 0
        AllData = ""
        while i < len(data):
            data[i] = data[i].split()
            data[i][0] = int(data[i][0]) + 80
            data[i][0] = str(data[i][0])
            data[i] = " ".join(data[i])
            AllData += data[i] + "\n"
            i+=1   
        f1.write(AllData)
        