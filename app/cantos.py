import time
import requests
import re
import json
from env.envs import APITOKEN
TOKEN = APITOKEN

def requisicaodasfixtures(fixtures):    
    '''
   Query: bookmaker 8, é a bet365.
          bet 45 = cantos.
    '''
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"
    #print(fixtures)              
    querystring = {"fixture":'{}'.format(fixtures) ,"bookmaker":"8","bet":"45"}
    headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': TOKEN
            }
    requisicaodecantosparabet365 = requests.request("GET", url, headers=headers, params=querystring).json()
    return requisicaodecantosparabet365
     
def processamentodecantos(fixtureinlive):
    bar = fixtureinlive
    size = len(bar)
    arrayfixtureidempatados = []
    tempodojogo = 80
    for x in range(0,size):        
        golshome = bar[x]['goals']['home']
        golsaway =  bar[x]['goals']['away']
        elapsed = bar[x]['fixture']['status']['elapsed']
        teamhome = bar[x]['teams']['home']['name']
        teamaway = bar[x]['teams']['away']['name']
        liga = bar[x]['league']['name']
        pais = bar[x]['league']['country']
        eventos = bar[x]['events']
        sizeeventos = len(eventos)
        fixtureid = bar[x]['fixture']['id']
        if golshome == golsaway and elapsed >= tempodojogo:                    
            arrayfixtureidempatados.append(fixtureid)
            jazz = requisicaodasfixtures(fixtureid)            
            if jazz['results'] >= 1:
                
                shape()
                for y in range(0,sizeeventos):                                    
                    
                    detalhesdoevento = eventos[y]['detail']
                    cartosvermelhos = re. search('Red',detalhesdoevento)
                    
                    if cartosvermelhos:                        
                        print('RED CARD')
                print('Time:{} x {} - liga:{} pais:{} elapsed: {} Fixture: {}\n'.format(teamhome,teamaway,liga,pais,elapsed,fixtureid))
                shape()
                #print(eventos)
                                    
                        
                print(jazz['response'][0]['bookmakers'][0]['bets'][0]['values'])
                
            
        
    
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
        try:
            main()
            time.sleep(60)
        except:
            pass
