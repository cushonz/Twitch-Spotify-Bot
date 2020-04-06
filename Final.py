from ConnectionInfo import token, connection, user, channel, SUMM_NAME, answ
import socket
import TwitchBot
import time
import random
import Spotify
import requests
import json
from datetime import datetime,timedelta

headers = {"Client-ID":'knyi2zb44wkzrbh0xqa312w5kq6mpu'}

def upTime():
    stream = requests.get("https://api.twitch.tv/helix/streams?user_login=zaddysquid", headers = headers)
    streamJ = stream.json()
    time = streamJ['data'][0]['started_at']
    time = datetime.strptime(time,'%Y-%m-%dT%H:%M:%SZ')
    compare = datetime.now()+timedelta(hours=7)
    uptime = compare-time
    print(uptime)
    return uptime


# CREATES A CONNECTION TO TWITCH IRC SERVERS
def CreateConnection():
    server = socket.socket()
    server.connect(connection)
    server.send(bytes('PASS ' + token + '\r\n', 'utf-8'))
    server.send(bytes('NICK ' + user + '\r\n', 'utf-8'))
    server.send(bytes('JOIN ' + channel + '\r\n', 'utf-8'))
    return server


lurk = ["YOOOO THANKS FOR THE LURK MAN!", "You do be lurkin doe", "thanks for the lurk ya cutie",
        "Man I appreciate the fuck outta you"]


def commandsNew(MSG, sock, user):
    OMSG = MSG.lower()
    MSG = MSG.lower()
    MSG = MSG.split(" ")
    if MSG[0] == "!lurk":
        reply = random.randint(0, 3)
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + lurk[reply] + " @"+user + "\r\n",
            "UTF-8"))
    elif MSG[0] == "!dice":
        roll = random.randint(1, 6)
        sendToChat("You rolled a :" + str(roll), sock)
    elif MSG[0] == "!rank":
        RankData = TwitchBot.rank()
        rank = RankData[0]
        league = RankData[1]
        elo = RankData[3]
        sendToChat("Current Rank: " + rank + " " + league + " " + str(elo) + " LP", sock)
    elif MSG[0] == "!uptime":
        uptime = str(upTime())
        hour = uptime[0]
        minute = int(uptime[2])*10 + int(uptime[3])
        sendToChat("Up time: "+str(hour)+" hours and "+str(minute)+" minutes!",sock)
    elif MSG[0] == "!sr":
        song = OMSG.replace("!sr ", "")
        if Spotify.addToPlaylist(song) != None:
            sendToChat(song.capitalize() + " added to playlist! Thanks for the suggestion @"+user, sock)
        else:
            sendToChat("I couldn't find " + song.upper() + " on Spotify! Sorry @"+user,sock)
    elif MSG[0] == "!song":
        trackInfo = Spotify.currentSongTitle()
        sendToChat("Currently Playing: " + trackInfo,sock)
    elif MSG[0] in answ:
        MSGS = MSG[0].lower()
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + answ[MSGS] + "\r\n",
            "UTF-8"))


def sendToChat(answer, sock):
    sock.send(bytes(
        "PRIVMSG " + channel + " :" + answer + "\r\n",
        "UTF-8"))


# GENERAL FUNCTION TO LISTEN TO ALL MESSAGES IN CHAT
def listen(sock):
    while True:
        time.sleep(2)
        msg = sock.recv(2048).decode('UTF-8')
        data = msg.split(":")
        # prevents index out of range error when twitch pings the bot
        if len(data) >= 3:
            print(data[1]+ ":" + data[2])
            data[2] = data[2].strip()
            name = data[1].split("!")
            name = name[0]
            commandsNew(data[2], sock, name)
        # Replies to twitches PING with PONG in order to stay connected
        elif len(data) < 3:
            server.send(bytes('PONG :tmi.twitch.tv\r\n', 'utf-8'))

# CALLING FUNCTIONS
server = CreateConnection()
listen(server)
