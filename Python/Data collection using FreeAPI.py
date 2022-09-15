# Free APi : https://api.punkapi.com/v2/beers/

from requests import get
import pandas as pd

# get url
base_url = "https://api.punkapi.com/v2/beers/"
response = get(base_url)
response.status_code

beers = response.json()


# required data
names = []
tagline = []
description = []
abv = []
ibu = []


for i in range(20):
    databeer = beers[i]
    names.append(databeer['name']) 
    tagline.append(databeer['tagline'])
    description.append(databeer['description'])
    abv.append(databeer['abv'])
    ibu.append(databeer['ibu'])
    
    
punk = {
    "name" : names,
    "tagline" : tagline,
    "description" : description,
    "ibu" : ibu,
    "abv" : abv
}

# Create Dataframe
df = pd.DataFrame(punk)
df.head(10)
