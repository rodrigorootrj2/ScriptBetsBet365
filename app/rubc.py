import requests
'''
Listando as Ligas dos campeonatos brasileiros.
'''
from env.envs import APITOKEN
TOKEN = APITOKEN
def main():
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    querystring = {"country":"Brazil"}
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    responsep = response.json()
    size = len(responsep)
    print(responsep)

size = len(foo['response'])
for x in range(0,size):
#    size = len(foo['response']) 
    print(foo['response'][x]['league']['id'])
    print(foo['response'][x]['league']['name'])

    print('######################################################################')