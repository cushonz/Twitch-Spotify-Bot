import requests
from ConnectionInfo import ID_URL, RANK_URL, SUMM_NAME, ID, API


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
    if summonerData[0]['queueType'] == "RANKED_FLEX_SR":
        return summonerData, 1
    else:
        return summonerData, 0


def rank():
    account_data = getAccount()
    summonerData, use = getStats()
    return summonerData[use]["tier"], summonerData[use]["rank"], "LP: ", summonerData[use]["leaguePoints"]
