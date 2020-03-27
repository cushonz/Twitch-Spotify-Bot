import pprint
import sys
from Utility import Utility

import spotipy
import spotipy.util as util



# User variables
divider = '***********************************'
scope = "playlist-modify-public"
playlistPrefix = 'zs'
defaultSong = "Redbone"
pl = '01UYLs2Pb5phx9eLLE7MGL'

# Operational variables
searchLength = 255
searchDividers = ['|', ';', ':', ',']
searchRemoves = [(' by ', " "), ("'", ""), ('"', "")]
cred = Utility.getCred()
token = util.prompt_for_user_token(cred['userName'], scope)
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
else:
    print("Can't get token for", cred['userName'])
    exit()


# Functions
def createPlaylist(playlist_name, silent=False):
    try:
        playlist = sp.user_playlist_create(cred['userName'], playlist_name,
                                           description="Twitch playlist " + playlist_name)
        return playlist
    except:
        print("Unable to create " + playlist_name)
        exit()


def songUri(findMe):
    result = sp.search(findMe)
    return result['tracks']['items'][0]['uri']


def addToPlaylist(pl, track_id):
    return sp.user_playlist_add_tracks(cred['userName'], pl, track_id)


# Main
# This clause allows a command line override of playlist name
if len(sys.argv) > 1:
    playlist_name = sys.argv[1]
else:
    playlist_name = playlistPrefix + Utility.getTimestamp()

# Create the new playlist and update user
playlist = createPlaylist(playlist_name, True)
print(playlist_name + ' playlist created')

# Add default song to the playlist
result = addToPlaylist(playlist['id'], [songUri(defaultSong)])

# Take live input for new songs for playlist
input_active = True
while input_active:
    searchTerm = input("Enter song to search for: ")[:searchLength]
    if searchTerm.lower() == '!quit':
        input_active = False
    else:
        inputArray = Utility.processInput(searchDividers, searchRemoves, searchTerm)
        searchArray = []
        for element in inputArray:
            searchArray.append(songUri(element))
        addToPlaylist(playlist['id'], searchArray)
        print(searchArray)
        print('Song added')
