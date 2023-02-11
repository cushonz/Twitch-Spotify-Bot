# Twitch Bot Readme

A Twitch bot designed to listen and respond to user commands in a Twitch channel. It was built using the Twitch API and Spotify API and can perform various functions like adding songs to a playlist, displaying the current song, displaying the rank and uptime of the channel, rolling a dice, and responding to specific messages.

## Requirements

- Twitch API key
- Spotify API key
- Python 3.x

## Libraries Used

- socket
- time
- random
- requests
- json
- datetime

## Files

- TwitchBot
- Spotify
- ConnectionInfo

## How to Use

1. Clone the repository to your local machine.
2. Replace the necessary information in the `ConnectionInfo.py` file:
   - Replace the `token` with your Twitch API key.
   - Replace the `connection` details with your desired details.
   - Replace the `user` with your Twitch username.
   - Replace the `channel` with your Twitch channel name.
   - Replace the `SUMM_NAME` with your Summoner name.
   - Replace the `answers` dictionary with messages the bot should respond to.
3. Replace the `Client-ID` in the headers dictionary with your Twitch API client ID.
4. Replace the Twitch channel name `zaddysquid` in the `upTime()` function with your Twitch channel name.
5. Run the `CreateConnection()` function to connect the bot to the Twitch channel.
6. Run the `listen(sock)` function to listen to messages in the Twitch channel.

## Available Commands

- `!lurk` - Bot responds with a random message thanking the user for lurking in the channel.
- `!dice` - Bot rolls a dice and displays the result in the chat.
- `!rank` - Bot displays the rank of the Twitch channel.
- `!uptime` - Bot displays the uptime of the Twitch channel.
- `!sr` - Bot adds a song to the Spotify playlist. Example: `!sr Shape of you`
- `!song` - Bot displays the current song being played in Spotify.

The bot is also programmed to respond to certain messages, which can be configured in the `answers` dictionary in the `ConnectionInfo.py` file.
