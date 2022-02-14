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
def foo(valor):
    var = valor
    print(type(var))
    size = len(var)  
    print(size)  
    for x in range(0,size):
        print(var[x]['league']['id'])
        print(var[x]['league']['name'])
        print('######################################################################')


def betslive():
    import requests

    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"live":"all"}
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    responsep = response.json()['response']
    return responsep    
var = betslive()
#print(var)
foo(var)