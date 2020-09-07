import os 
  
# Function to rename multiple files 
def main(): 
    i = 1000
    directory = "C:/Users/pc/Downloads/duckPics/"
    for count, filename in enumerate(os.listdir(directory)): 
        dst = str(i) 
        src = filename 
        dst = dst + ".jpg"    
        os.rename(os.path.join(directory,filename), 
                  os.path.join(directory,dst))
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 