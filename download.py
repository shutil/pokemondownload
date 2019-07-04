import shutil, requests, json
import os
import time

os.makedirs("images")

def download(url,name):
    path = url
    response = requests.get(url, stream=True)
    with open('image/'+name+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
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

