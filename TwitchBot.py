import requests
from ConnectionInfo import ID_URL, RANK_URL, SUMM_NAME, ID,API

def getAccount():
    response = requests.get(ID_URL + SUMM_NAME + API)
    account_data = response.json()
    return account_data

def getAPIKey():
    key = input("Enter API key for Riot Games")
    return key

def getStats():
    response = requests.get(RANK_URL + ID + API)
    summonerData = response.json()
    return summonerData


def rank():
    account_data = getAccount()
    summonerData = getStats()
    return summonerData[1]["tier"], summonerData[1]["rank"], "LP: ", summonerData[1]["leaguePoints"]
