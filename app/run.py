import time
import requests
import os
import json

TOKEN="bbdbfe19bfmsh8476707275ef943p12565djsnd84f6469a950"
def cred():
    #TOKEN = os.getenv('APITOKEN')
    print(APITOKEN)

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
    '''
    for x in range(0,size):
        fixtureid = responsep[x]['fixture']['id']
        fixtureelapsed = responsep[x]['fixture']['status']['elapsed']        
        if fixtureelapsed >= 80:
            print('{} - {}'.format(fixtureid,fixtureelapsed))'''

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




def main():      
    betslive()
    #bets()
    #betlivemap()
#836183
main()




'''
if __name__ == "__main__":
    while True:        
        main()
        time.sleep(60)
'''
