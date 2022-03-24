import requests
import json


# github username and token
username = 'meghakashyap'
token = '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'

# fetching data from github repo url
url = requests.get('https://api.github.com/users/'+ username +'/repos', auth=(username, token))
print(url.status_code)
data = url.json()


def fetching_Repo():
    dict = {}
    repo = []
    for i in data:
        
        # storing repo name into list
        repo.append(i["name"])
        print(i["name"])
    
    dict["Repositories"] = repo
    
    #stoirng repo in json file 
    with open("repo.json","w+") as file:
        json.dump(dict,file,indent=4)

fetching_Repo()

