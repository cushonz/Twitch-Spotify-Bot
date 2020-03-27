from ConnectionInfo import token, connection, user, channel, SUMM_NAME
import socket
import TwitchBot
import time
import random


# CREATES A CONNECTION TO TWITCH IRC SERVERS
def CreateConnection():
    server = socket.socket()
    server.connect(connection)
    server.send(bytes('PASS ' + token + '\r\n', 'utf-8'))
    server.send(bytes('NICK ' + user + '\r\n', 'utf-8'))
    server.send(bytes('JOIN ' + channel + '\r\n', 'utf-8'))
    return server







# A LIST OF KEYWORDS FOR THE BOT TO RESPOND TO
def commands(MSG, sock, username):
    MSG = MSG.split(" ")
    time.sleep(1)
    if MSG[0] == '!rank':
        msg = TwitchBot.rank()
        sock.send(bytes("PRIVMSG " + channel + " :" + msg[0].lower().capitalize() + " " + msg[1] + " " + str(
            msg[3]) + " LP" + "\r\n", "UTF-8"))
    elif MSG[0] == '!help':
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + "Command List: !rank: Returns current Elo in League of Legends,  !lurk: "
                                          "Lets me know you're lurkin     ,!summname: Returns my summoner name so you "
                                          "can add me on League of Legends,    !dice: Rolls a virtual die and returns "
                                          "the value to chat.   !socials: Returns my social medias!" + "\r\n",
            "UTF-8"))
    elif MSG[0] == '!lurk':
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + "@" + username + " Thanks for the lurk, I appreciate the support! Make sure "
                                                           "your volume is above 1% and your resolution is set to "
                                                           "160p to save your bandwidth!" + "\r\n",
            "UTF-8"))
    elif MSG[0] == '!summname':
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + "Summoner Name: " + SUMM_NAME.capitalize() + " add me so we can play "
                                                                                       "sometime @" + username +
            "\r\n",
            "UTF-8"))
    elif MSG[0] == '!dice':
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + "Rolling dice..." + "\r\n",
            "UTF-8"))
        time.sleep(2)
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + "@" + user + " rolled a : " + str(random.randint(1,6))+ "!" + "\r\n",
            "UTF-8"))
    elif MSG[0] == '!socials':
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + "Follow me on Twitter! @ZaddySquid, I'm currently working on getting more "
                                          "social media setup so stick around!" + "\r\n",
            "UTF-8"))
    elif MSG[0] == '!':
        sock.send(bytes(
            "PRIVMSG " + channel + " :" + "It looks like you've tried to input a command that I dont understand, "
                                          "try running the '!help' command" + "\r\n",
            "UTF-8"))
    elif MSG[0] == '!so':
        print(len(MSG))
        if len(MSG)>1:
           name = MSG[1]
           if MSG[1][0] != '@':
               sock.send(bytes("PRIVMSG " + channel + " :" + "Shout out @" + name + " go check their channel out!" + "\r\n", 'utf-8'))
           elif MSG[1][0] == '@':
               sock.send(bytes("PRIVMSG " + channel + " :" + "Shout out " + name + " go check their channel out!" + "\r\n", 'utf-8'))


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
            commands(data[2], sock, name)
        # Replies to twitches PING with PONG in order to stay connected
        elif len(data) < 3:
            print(data)
            server.send(bytes('PONG :tmi.twitch.tv\r\n', 'utf-8'))
            print("PONG SENT")



# CALLING FUNCTIONS
server = CreateConnection()
listen(server)
