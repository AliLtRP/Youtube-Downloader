from pytube import Playlist

class playList:
    
    # constructor
    def __init__(self, link):
        self.link = link
    
    # download the list with highest resolution
    def video(self, link):
        playlist = Playlist(link)

        print("Start Downloading...")
        for i in playlist.videos:
            i.streams.get_highest_resolution().download()
            print(i.title, "Done")