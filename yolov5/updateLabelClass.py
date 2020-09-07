import os 
from shutil import copyfile

SOURCE_DIR = "C:/Users/pc/Downloads/duckPicsAugmented/test/labels/"
DEST_DIR =   "C:/Users/pc/Downloads/duckPicsAugmented/test/tmp/"
NEW_CLASS = "2"

# Function to rename multiple files 
def main(): 
    for count, filename in enumerate(os.listdir(SOURCE_DIR)): 
        print(filename)
        if filename.count(".txt") and filename.count("classes")==0 :
            f = open(SOURCE_DIR+filename, "r")
            dest_f = open(DEST_DIR+filename, "w")
            for s in f:
                # print("Orig:",s,end='')
                arr = s.split() 
                arr[0] = NEW_CLASS
                s = " ".join(arr)
                # print("New2:",s)
                dest_f.write(s+"\n")
            dest_f.close()
            f.close()
        else:
            copyfile(SOURCE_DIR+filename, DEST_DIR+filename)
        
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 