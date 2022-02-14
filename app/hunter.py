import time
import requests
import os
import json
from env.envs import APITOKEN
TOKEN = APITOKEN


def timezone():
    import requests

    url = "https://api-football-v1.p.rapidapi.com/v3/timezone"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    response = requests.request("GET", url, headers=headers)    
    responsep = response.json()['response']
    for x in range(0,len(responsep)):
        print(responsep[x]) 

def bookmakers():
    import requests
    url = "https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers"

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers)
    print(response.json())   

def bets():
    import requests
    url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    response = requests.request("GET", url, headers=headers)
    responsep = response.json()['response']
    for x in range(0,len(responsep)):
        print(responsep[x])


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
    size = len(responsep)
    print(responsep)


def betlivemap():
    import requests
    url = "https://api-football-v1.p.rapidapi.com/v3/odds/mapping"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    response = requests.request("GET", url, headers=headers)
    responsep = response.json()['response']
    size = len(responsep)
    for x in range(0,size):
        print(responsep[x])

def brazilleagues():
    '''
    Relatório de campeonatos atuais no brasil.
    '''
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

    querystring = {"country":"Brazil","current":"true"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    responsep = response.json()['response']
    size = len(responsep)
    for x in range(0,size):
        print(responsep[x]['league']['id'])
        print(responsep[x]['league']['name'])
        print(responsep[x]['seasons'][0]['year'])
        print(responsep[x]['seasons'][0]['start'])
        print(responsep[x]['seasons'][0]['end'])

        shape()

def bar():
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    #querystring = {"league":"475","season":"2022"}
    querystring = {"team":"131","season":"2022"}
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    responsep = response.json()['response']
    size = len(responsep)
    for x in range(0,size):
        shape()
        print(responsep[x])  

def bar2():
    #url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    #querystring = {"league":"475","season":"2022"}
    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
    querystring = {"league":"39","season":"2020","team":"33"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    responsep = response.json()['response']
    size = len(responsep)
    print(responsep)
    '''
    
    
    for x in range(0,size):
        shape()
        print(responsep[x])  '''   

 
 



def shape():
    tarugo='#' * 70    
    print(tarugo)

def main():      
    #betslive()
    #bets()
    #betlivemap()
    #brazilleagues()
    bar2()
    
#836183
main()




'''
if __name__ == "__main__":
    while True:        
        main()
        time.sleep(60)
'''
