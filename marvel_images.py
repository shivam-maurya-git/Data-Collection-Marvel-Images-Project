from requests import get
# Requests allows you to send HTTP/1.1 requests extremely easily
import json
from marvel import Marvel
import pandas as pd

df = pd.read_csv('marvel_characters.csv')
for i in df['character_name']:
    url = f'https://gateway.marvel.com:443/v1/public/characters?name={i}&ts=1689856382&apikey=0fee022d3b133b3af21ca3da8d44e242&hash=8fa8c41be6288e853b1bd48b391fcc9a'
    result = get(url)
    print(url)
    json_result = json.loads(result.content)['data']['results']
    

    if json_result != []:
        character_image = json_result[0]['thumbnail']
    for j in character_image:
      if j=='path':
        main_url = character_image[j]
      elif j=='extension':
        image_extension = character_image[j]
        image_url = main_url+'.'+image_extension
        response = get(image_url)
        image_data = response.content
        file_path = 'marvel_images\\'+i+'.jpg'
        with open(file_path, "wb") as f:
          f.write(image_data)
       
        

