import time
import requests
import re
import json
from env.envs import APITOKEN
TOKEN = APITOKEN

def reqX(fixtures):    
    var = fixtures
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"
    for x in range(0,len(var)):                
        querystring = {"fixture":'{}'.format(var[x]) ,"bookmaker":"8","bet":"45"}
        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': TOKEN
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        responsep = response.json()
        
        return responsep
     
def processamentodecantos(size):
    bar = size
    size = len(bar)
    array = []
    tempodojogo = 80
    for x in range(0,size):        
        golshome = bar[x]['goals']['home']
        golsaway =  bar[x]['goals']['away']
        elapsed = bar[x]['fixture']['status']['elapsed']
        C = bar[x]['teams']['home']['name']
        D = bar[x]['teams']['away']['name']
        E = bar[x]['league']['name']
        F = bar[x]['league']['country']
        G = bar[x]['events']
        H = len(G)
        I = bar[x]['fixture']['id']
        if golshome == golsaway and elapsed >= tempodojogo:                    
            array.append(I)
            jazz = reqX(array)            
            if jazz['results'] >= 1:
                
                shape()
                for y in range(0,H):                                    
                    
                    AA = G[y]['detail']
                    m = re. search('Red',AA)
                    
                    if m:                        
                        print(AA)
                print('Time:{} x {} - liga:{} pais:{} elapsed: {} Fixture: {}\n'.format(C,D,E,F,elapsed,I))
                shape()
                        
                        
                print(jazz)
                
            
        
    
def betslive():   

    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"live":"all"}
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': TOKEN
        }
    fixtureslive = requests.request("GET", url, headers=headers, params=querystring).json()['response'] 
    processamentodecantos(fixtureslive)

def shape():
    tarugo = '#' * 70
    print(tarugo)
def shapend():
    tarugo = '=' * 70
    print(tarugo)

def main():
    print('Iniciando os Trabalhos')
    betslive()
    print('Finalizando os Trabalhos')
    shape()
    shapend()
    shape()

if __name__ == "__main__":
    while True:        
        main()
        time.sleep(60)
