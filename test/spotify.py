import os,sys,inspect
import pprint
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import Spotify as sp

testPlaylist='37iZg7zLb6cjFVHgJRGRJM'
#sp.pl = testPlaylist

input_active = True
while input_active:
    searchTerm = input("Enter song to search for: ")[:sp.searchLength]
    if searchTerm.lower() == '!quit':
        input_active = False
    elif searchTerm.lower() == '!song':
        pprint.pprint(sp.sp.currently_playing())
    else:
        newSong = sp.addToPlaylist(searchTerm)
        if newSong != None:
            print(searchTerm + ' added to playlist')
        else:
            print("I couldn't find "+searchTerm+" on spotify, feel free to try again")