import shutil, requests, json
import os
import time

os.makedirs("image")

def download(url,name):
    response = requests.get(url, stream=True)
    f = open("image/"+name+".jpg","wb")
    shutil.copyfileobj(response.raw,f)
    f.close()
    
    del response


file = open("pokemon.json")
str_data = file.read()
file.close()
data = json.loads(str_data)

num = len(data['pokemon_names'])
r = 20

for x in range(0,num):
    name = data['pokemon_names'][x]
    link = data['pokemon_image_links'][x]
    download(link,name)
    print(str(x+1)+") "+name + " image downloaded")

