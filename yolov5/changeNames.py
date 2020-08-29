import os 
  
# Function to rename multiple files 
def main(): 
    i = 500  
    directory = "C:/temp/train_guns/labels/"
    for count, filename in enumerate(os.listdir(directory)): 
        dst = str(i) 
        src = filename 
        dst = dst + ".txt"    
        os.rename(os.path.join(directory,filename), 
                  os.path.join(directory,dst))
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 