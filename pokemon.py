from requests_html import HTMLSession
import requests
import json

session = HTMLSession()

r = session.get("https://pokemondb.net/pokedex/national")

links = r.html.find('.img-sprite')

# https://img.pokemondb.net/artwork/large/bulbasaur.jpg
#fing to find image


pokemon_images = {'pokemon_names':[],'pokemon_image_links':[]}
for x in links:
    y = x.attrs['data-src']
    z = y.split('/')

    extention_check = z[len(z)-1]
    jpg_image = extention_check.split('.')
    jpg_image.pop()
    jpg_image.append("jpg")

    pokemon_images['pokemon_image_links'].append("https://img.pokemondb.net/artwork/large/"+jpg_image[0]+"."+jpg_image[1])
    pokemon_images['pokemon_names'].append(jpg_image[0])


txt = json.dumps(pokemon_images,indent=2)
print("Total number of pokemons are "+str(len(pokemon_images['pokemon_names'])))


file = open('pokemon.json','w')
file.write(txt)
file.close()

print("Pokemon database created")