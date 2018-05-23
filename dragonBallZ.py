from fake_useragent import UserAgent
import requests

ua = UserAgent()

count = 1
headers = {
    'User-Agent': ua.google
}



# sauce = urllib.request.urlopen('http://www.99kubo.tv/vod-play-id-78769-sid-0-pid-' + str(count) + '-flv.html').read()
url = 'http://www.99kubo.tv/vod-play-id-78769-sid-0-pid-1-flv.html'

# r = requests.get(url, headers=myHeaders)
r = requests.get(url, headers=headers)
print(r.text)
# print(r.content)
#sauce = urllib.request.urlopen('http://www.99kubo.tv/vod-play-id-78769-sid-0-pid-1-flv.html').read()

# print(sauce)
# exampleSoup = bs4.BeautifulSoup(sauce, 'html.parser')

#print(exampleSoup)

# for video in exampleSoup.find_all('a'):
#     videoLink = video.get('src')
#     print(videoLink)
    # videoSearch = re.search(r'my-video_html5_api', videoSearch, flags=0)
    #print(mp3Search)
    # if mp3Search:
    #     print(mp3Name)
    #     downloadAndRename = urllib.request.urlretrieve("https://resources.allsetlearning.com/pronwiki/resources/pinyin-audio/" + mp3Name, "/Users/automac/Music/allPinyin/" + mp3Name)


