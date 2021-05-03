import pandas as pd
import json
import requests
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/1470000/FoodNtrIrdntInfoService/getFoodNtrItdntList'

queryParams = '?' + \
              'ServiceKey=' + 'kWyANjUVYzXfzeThcm4wuMCx2ufPvkLK1odiTRYpldwHHxKrmgUzFxD3OHx8GXUpyVbp0hRfslzrTPJw26aKKw%3D%3D' + \
              '&numofRows=' + '3' # \

result = requests.get(url + queryParams)
print(result.content)
table = xml.loads(result.content)
data = pd.DataFrame(js['resultcode']['resultMsg']['Items']['Item'])