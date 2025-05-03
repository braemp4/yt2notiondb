from pytube import Playlist, YouTube # type: ignore
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

URL_PLAYLIST = "https://www.youtube.com/playlist?list=PLw88QLYxobHeVwyhAw2yGkagwMMe_aY3y"

read = []


playlist = Playlist(URL_PLAYLIST)
read.append(playlist)

#for i in range(1, len(playlist.video_urls)+1):
    #titles.append("video " + str(i))

def find_titles(playlist):
    titles = []

    for url in playlist.video_urls:

        page_scrape = requests.get(url)
        soup = BeautifulSoup(page_scrape.text, "html.parser")
        try:
            link = soup.find_all(name="title")[0]
            titles.append(link.text)
        except:
            titles.append("encoding error")

    return titles



read.append(find_titles(playlist=playlist))

print(read)

