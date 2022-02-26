import os, os.path
import requests
import os
from bs4 import BeautifulSoup as bs


error = 0
j = 0
os.system("cls")

path = './backuprecent'
path2 = './wallpapers'
file_types = ["gif","webp","jpg","png","apng","mp4"]


def make_directory(web_page_name):
  os.makedirs(f"{path2}/{web_page_name}")
  x = f"{path2}/{web_page_name}"
  print(f"{path2}/{web_page_name}   - was created")
  return x


def new_folder_name(f):
  start = f.find("・") + len("・")
  end = f.find("[")
  return_string = f[start:end]
  return return_string.strip()


def get_data(root,f):
  if j < 0:
    os.chdir(path)
  soup = bs(open(os.path.join(root, f)).read(),features="html.parser")
  return soup

def file_name(url):
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
      if "member-wallpapers" in web_page_name:
        pass
      else:
              
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
                

                try:
                #print(f"Final Name: {final_name}\n\n")
                
                    if int(final_name)  == 740758296620826726 or int(final_name) == 459513115671920641 or  int(final_name) == 584631090132680729 or int(final_name) ==  869631452374003773 or int(final_name) ==  544919834874347521 or int(final_name) == 896420807746682900:
                        duplicate = duplicate +1
                        pass
                    
                
                    else:
                        try:
                            counter=counter+1
                            #print(f"Downloading Image: {counter}\n")
                            with open(f'{path2}/{web_page_name}/{final_name}.{file_t}', 'wb') as handler:
                                handler.write(img_data)      
                        
                        except UnicodeDecodeError as e:
                            error = error+1
                            print("I ran into an error\n")
                            pass
                except ValueError:
                    final_name = str(final_name)
                    try:
                            counter=counter+1
                            #print(f"Downloading Image: {counter}\n")
                            with open(f'{path2}/{web_page_name}/{final_name}.{file_t}', 'wb') as handler:
                                handler.write(img_data)      
                        
                    except UnicodeDecodeError as e:
                            error = error+1
                            print("I ran into an error\n")
                            pass

            #else:
                #print("Unsupported file Type: ")
                #error = error+1
            
        
        j = j+counter
        print(f"\n{counter} wallpapers downloaded in {web_page_name} with {duplicate} duplicates\n")

print(f"\nOverall I downloaded {j} images and ran into {error} errors.")






"""import requests
import os
import glob
from bs4 import BeautifulSoup
from pathlib import Path

dir = Path('./backuprecent')
dir2 = Path('./strippedbackup')

os.system('cls')
for filename in glob.iglob(dir):
    with open(filename) as f:
        soup = BeautifulSoup(f)
        print(f)
        newfolder = f"{dir.stem}" 
        print(newfolder)
        os.makedirs('{dir2}\\{newfolder}')
        html_page = BeautifulSoup(f.text, 'html.parser')
        print(html_page)
        
        images = html_page.find_all("img")
        for index, image in enumerate(images):
            image_url= image.get("src")      #img src value
            
            image_extension= image_url.split(".")[-1]       #get image extension

            #get image data
            image_bytes = requests.get(image_url).content
            
            if image_bytes:
                #write the image data
                with open(f"Image {index+1}.{image_extension}", "wb") as file:
                    file.write(image_bytes)
                    print(f"Downloading image {index+1}.{image_extension}")
        

"""


