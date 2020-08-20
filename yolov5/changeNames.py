import os 
  
# Function to rename multiple files 
def main(): 
    i = 400  
    directory = "C:/Users/pc/Desktop/train-mafat/images/"
    for count, filename in enumerate(os.listdir("images")): 
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