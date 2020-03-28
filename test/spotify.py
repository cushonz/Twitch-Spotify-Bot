import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import Spotify as sp

testPlaylist='37iZg7zLb6cjFVHgJRGRJM'
sp.pl = testPlaylist

# print(sp.pl)
# exit()

input_active = True
while input_active:
    searchTerm = input("Enter song to search for: ")[:sp.searchLength]
    if searchTerm.lower() == '!quit':
        input_active = False
    else:
        inputArray = sp.Utility.processInput(sp.searchDividers, sp.searchRemoves, searchTerm)
        searchArray = []
        for element in inputArray:
            searchArray.append(sp.songUri(element))
        sp.addToPlaylist(searchArray)
        print(searchArray)
        print(searchTerm + ' added to playlist')