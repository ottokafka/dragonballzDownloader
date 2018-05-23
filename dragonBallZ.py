import requests
import bs4
import re
import shutil

count = 1
videoLinksList = []


while count != 3:

    ##  The first url dragonBall Z Episode 1
    url1 = "http://www.99tw.net/xplay/irmp408220.html?ep=" + str(count)

    print(url1)

    ## headers so the fucking website doesnt think we are a bot
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    ##  use the requests get method to retrive the data from the web site
    res = requests.get(url1, headers=headers1, stream=True)

    ##  check if the status code is good
    print("if you get 200 tots but if you get 403 or 404 its the fucken headers fault - anyway the result is " + str(
        res.status_code))

    ## grab the html text
    soup = bs4.BeautifulSoup(res.text, "html5lib")

    # print(soup)

    ## grab just the javascript because the video is fucking hidden
    js_text = soup.find('script', type="text/javascript").text

    ## loop through the tags and find the main video link
    for link in soup.find(js_text):
        match = re.findall(r'http.{159}', str(link))
        # print(match)
        # add the match to a list
        videoLinksList.append(match)

    ## Using the negative -1 means to grabs something from the end of the array
    videoLink1 = videoLinksList[-1][-1]
    print("Grabs link from the end of the List ")
    print(videoLink1)
    print(videoLinksList)

    ## Go to the new video link which as the pure video
    pureVideoDownload = requests.get(videoLink1, headers=headers1, stream=True)
    print(pureVideoDownload.status_code)

    'Downloading video please wait '
    with open('/Volumes/2ndDrive/tvShows/DragonBallZ/' + 'DragonBallZ- ' + str(count) + '.mp4', 'wb') as out_file:
        shutil.copyfileobj(pureVideoDownload.raw, out_file)
        # del will get out of the current file so the program can continue
    del pureVideoDownload

    count = count + 1
    print(count)


