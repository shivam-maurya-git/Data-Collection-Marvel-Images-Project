from requests import get
# Requests allows you to send HTTP/1.1 requests extremely easily
import json
from marvel import Marvel
import pandas as pd

df = pd.read_csv('marvel_comics_name_with_year.csv')
for i in df['comic_name']:
    url = f'https://gateway.marvel.com:443/v1/public/comics?title={i}&ts=1689856382&apikey=0fee022d3b133b3af21ca3da8d44e242&hash=201976039ad70f0a055f9997b275d578'
    result = get(url)
    print(url)
    json_result = json.loads(result.content)
    if json_result != {}:
      json_data = json_result['data']['results']
      if json_data != []:
        comic_image = json_data[0]['thumbnail']
        for j in comic_image:
            if j=='path':
              main_url = comic_image[j]
              image_url = main_url+'.jpg'
              response = get(image_url)
              image_data = response.content
              i = json_data[0]['series']['name']
              file_path = 'comic_images\\'+i+".jpg"
              if '"' in i:
                file_path = 'comic_images\\'+i.replace('"','_')+".jpg"
              elif '/' in i: 
                file_path = 'comic_images\\'+i.replace('/','_')+".jpg"
              elif ':' in i:
                file_path = 'comic_images\\'+i.replace(':','_')+".jpg"
              with open(file_path, "wb") as f:
                   f.write(image_data)
        

