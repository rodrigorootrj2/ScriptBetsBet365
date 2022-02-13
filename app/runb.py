import time
import requests
import os
import json
import re
from env.envs import APITOKEN


#from foo import bar
TOKEN = APITOKEN

def reqX(fixtures):
    import requests
    var = fixtures
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"
    for x in range(0,len(var)):        
        #print(var[x])
        querystring = {"fixture":'{}'.format(var[x]) ,"bookmaker":"8","bet":"45"}
        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': TOKEN
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        responsep = response.json()
        
        return responsep
     
def blob(size):
    bar = size
    size = len(bar)
    array = []
    for x in range(0,size):
        A = bar[x]['goals']
        A1 = bar[x]['goals']['home']
        A2 =  bar[x]['goals']['away']
        B = bar[x]['fixture']['status']['elapsed']
        C = bar[x]['teams']['home']['name']
        D = bar[x]['teams']['away']['name']
        E = bar[x]['league']['name']
        F = bar[x]['league']['country']
        G = bar[x]['events']
        H = len(G)
        I = bar[x]['fixture']['id']
        if A1 == A2 and B >= 80:                    
            array.append(I)
            jazz = reqX(array)            
            if jazz['results'] >= 1:
                
                shape()
                for y in range(0,H):                                    
                    
                    AA = G[y]['detail']
                    m = re. search('Red',AA)
                    #shape()
                    if m:                        
                        print(AA)
                print('Time:{} x {} - liga:{} pais:{} elapsed: {} Fixture: {}\n'.format(C,D,E,F,B,I))
                shape()
                        
                        
                print(jazz)
                shape()
            
        
    
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
    blob(responsep)

def shape():
    tarugo = '######################################################################'
    print(tarugo)

def main():
    print('Iniciando os Trabalhos')
    betslive()
    print('Finalizando os Trabalhos')

if __name__ == "__main__":
    while True:        
        main()
        time.sleep(60)
