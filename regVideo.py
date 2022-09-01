# from turtle import title
from pytube import YouTube

class myClass():

    #  constructor 
    def __init__(self, link):
        self.link= link

    # video title
    def viedoTitle(self, link):
        title = YouTube(link).title
        print(title)
        return title

    # print the available resolution
    def res(self, link):
        res = set()

        vid = YouTube(link)
        
        for i in vid.streams:
            res.add(i.resolution)
        
        print(res)

    # choose the resolution
    def pickRes(self):
        stringRes = input("please choose the resolution: ")

        if stringRes[-1] != "p":
            stringRes+="p"

        return stringRes

    # download the video
    def downVideo(self, link, string):
        video = YouTube(link)
        video = video.streams.filter(res=string).first().download()
        print("Done")