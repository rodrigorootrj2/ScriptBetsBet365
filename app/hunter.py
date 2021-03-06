import requests
from env.envs import APITOKEN
TOKEN = APITOKEN


def timezone():
    url = "https://api-football-v1.p.rapidapi.com/v3/timezone"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    response = requests.request("GET", url, headers=headers).json()['response']    
    responsesize = len(response)
    for x in range(0,responsesize):
        print(response[x]) 

def bookmakers():
    url = "https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers).json()
    print(response)   

def bets():
    url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    response = requests.request("GET", url, headers=headers).json()['response']
    responsesize = len(response)    
    for x in range(0,responsesize):
        print(response[x])


def jogosinlive():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"live":"all"}
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()['response']    
    responsesize = len(response)
    for x in range(0,responsesize):
        shape()
        print(response[x])
    #print(response)
#@

def betlivemap():
    url = "https://api-football-v1.p.rapidapi.com/v3/odds/mapping"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    response = requests.request("GET", url, headers=headers).json()['response']
    sizeresponse = len(response)
    for x in range(0,sizeresponse):
        print(response[x])

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

def jogadores():
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
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

def estatisticas():
    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
    querystring = {"league":"39","season":"2020","team":"33"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()['response']    
    print(response) 
 



def shape():
    tarugo='#' * 70    
    print(tarugo)

def main():      
    timezone()
    #jogosinlive()
    #bets()
    #betlivemap()
    #brazilleagues()
    #estatisticas()
    #jogadores()
    #bookmakers()
   

main()