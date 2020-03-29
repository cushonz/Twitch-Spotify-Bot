import os, sys, pprint
import spotipy
import spotipy.util as util

# User variables
scope = "playlist-modify-public"
pl = "01UYLs2Pb5phx9eLLE7MGL"  #REPLACE this playlistId with the correct one.

# Operational variables
searchLength = 255
searchDividers = ['|', ';', ':', ',']
searchRemoves = [(' by ', " "), ("'", ""), ('"', "")]

# Functions
def getCred(redirectUri='http://localhost/'):
        with open(os.path.expanduser('~/.spotify'), 'r') as file:
            content = file.read()
            if '\r' in content:
                data = content.split('\r\n')
            else:
                data = content.split('\n')
            os.environ["SPOTIPY_CLIENT_ID"] = data[1]
            os.environ["SPOTIPY_CLIENT_SECRET"] = data[2]
            os.environ["SPOTIPY_REDIRECT_URI"] = redirectUri
            return {'userName': data[0], 'clientId': data[1], 'clientSecret': data[2]}

def processInput(searchString):
        for remove in searchRemoves:
            searchString = searchString.replace(remove[0], remove[1])
        for item in searchDividers:
            if item in searchString:
                return [x.strip() for x in searchString.split(item)]
        return [searchString]

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

def addToPlaylist(track_id):
    return sp.user_playlist_add_tracks(cred['userName'], pl, track_id)


# Main
cred = getCred()
token = util.prompt_for_user_token(cred['userName'], scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
else:
    print("Can't get token for", cred['userName'])
    exit()