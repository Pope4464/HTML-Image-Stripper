import os, os.path
import requests
import os
from bs4 import BeautifulSoup as bs

error = 0
j = 0
os.system("cls")

path = './backuprecent' #The file path in which the html Files are contained
path2 = './wallpapers' #The file path you wish for the images to be saved
file_types = ["gif","webp","jpg","png","apng","mp4",'.jpeg','.raw','.tiff','.bmp']

def make_directory(web_page_name):
  os.makedirs(f"{path2}/{web_page_name}")
  x = f"{path2}/{web_page_name}"
  print(f"{path2}/{web_page_name}   - was created")
  return x

def new_folder_name(f):
  #Put the code to slice and index strings, this will name the folders after the html file, leave as is if you wish to keep the html file as is
  return_string = f.lower()
  return return_string.strip()

def get_data(root,f):
    if j < 0:
        os.chdir(path)
    #Specify HTML PARSER or else it will throw unnesecary errors
    soup = bs(open(os.path.join(root, f)).read(),features="html.parser")
    return soup

def file_name(url):
    """ 
    Here put the nessecary string indexing and splicing so that you can name your files. I used stings such as this  https://media.discordapp.net/attachments/946438427170189332/946943719037358170/IMG_7289.jpg?width=663&height=663
    The indexing below gets the ID of the image (so i can sort through in later editions)

    """
    
    
    
    string = str(url)
    x= string.split('/')
    final=x[-2]
    #print(final)
    return final

for root, dirs, files in os.walk(path):
    for f in files:
      
        counter = 0
        duplicate = 0
        web_page_name = new_folder_name(f)   
        soup = get_data(root,f)
        make_directory(web_page_name)

        for image in soup.findAll("img"):
          #file type
          source = image["src"]
          
          #print(source)
          for x in file_types:
            if x.lower() in source.lower():
                file_t = x
                img_data = requests.get(source).content
                final_name = str(file_name(source))
                
                #final name = int(final_name) # Commented out this line and several other ID checks as they are not needed
            
                try:
                    counter=counter+1
                    #print(f"Downloading Image: {counter}\n")
                    with open(f'{path2}/{web_page_name}/{final_name}.{file_t}', 'wb',errors='replace') as handler:
                        handler.write(img_data)      
                
                except UnicodeDecodeError as e:
                    error = error+1
                    print("I ran into an error\n")
                    pass
                
                #This is not needed unless you are checking against ID such as I was
                except ValueError:
                    final_name = str(final_name)
                    try:
                        counter=counter+1
                        #print(f"Downloading Image: {counter}\n")
                        with open(f'{path2}/{web_page_name}/{final_name}.{file_t}', 'wb',errors='replace') as handler:
                            handler.write(img_data)      
                        
                    except UnicodeDecodeError as e:
                        error = error+1
                        print("I ran into an error\n")
                        pass
               
        j = j+counter
        print(f"\n{counter} wallpapers downloaded in {web_page_name} with {duplicate} duplicates\n")

print(f"\nOverall I downloaded {j} images and ran into {error} errors.")
