from ConnectionInfo import token, connection, user, channel, SUMM_NAME, answ
import socket
import TwitchBot
import time
import random
import Spotify


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
    MSG = MSG.split(" ")
    if MSG[0] == "!lurk":
        reply = random.randint(0, 3)
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + lurk[reply] + "\r\n",
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
    elif MSG[0] == "!sr":
        song = OMSG.replace("!sr ", "")
        if Spotify.addToPlaylist(song) != None:
            sendToChat(song.upper() + " added to playlist!", sock)
        else:
            sendToChat("I couldn't find " + song.upper() + " on Spotify!",sock)
    elif MSG[0] in answ:
        MSG = MSG.lower()
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + answ[MSG] + "\r\n",
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
        print(msg)
        # prevents index out of range error when twitch pings the bot
        if len(data) >= 3:
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
