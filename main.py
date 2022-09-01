from pytube import YouTube
from pytube import Playlist

from regVideo import myClass
from playlist import playList


# input to get the url
strInput = input("Please enter the URL: ")

# check if url for video pf playlist
if strInput[24:25] == "p":
    yt = playList(strInput)
    yt.video(strInput)

# playlist download
else:
    yt = myClass(strInput)
    yt.viedoTitle(strInput)
    yt.res(strInput)

    yt.downVideo(strInput, yt.pickRes())
