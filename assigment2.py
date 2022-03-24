import requests
import json

# fetching data from api using requests module
api = requests.get('https://httpbin.org/get')
content = api.json()
print(content)

dict = {}
def Api():
    
    # runing loop over fetched data
    for i in content:
        dict['User-Agent']=content['headers']['User-Agent']
        dict['Origin'] = content["origin"]
        
       # storing data in json file
    with open('data.json','w+') as file:
        json.dump(dict,file,indent=4)
    
Api()






