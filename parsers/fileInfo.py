from collections import defaultdict

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://fileinfo.com/extension/"


def scrapeFileinfo(extension):
    fileExts1 = defaultdict(lambda: ["Format not found"])
    fileExts1["Extension"] = extension
    try:
        reqContent = requests.get(
            BASE_URL + extension
        )  # make a request to website , with specific extension

        soup = BeautifulSoup(
            reqContent.content, "html5lib"
        )  # parse the response using a html5lib parser

        if soup.find("title").text == 'File Extension Not Found':
            #print(extension)
            return fileExts1
    except Exception as e:
        print(e)
        return fileExts1

    try:
        fileExts1["Name"] = soup.find(
            "h2", attrs={"class": "title"}
        ).text  # extract different data
    except:
        pass
    try:
        obj = soup.find("table", attrs={"class": "headerInfo"}).text.split()
        fileExts1["Format"] = obj[-1]
        fileExts1["Popularity"] = obj[obj.index("Popularity") + 1]
        fileExts1["Category"] = obj[obj.index("Category") + 1]
    except:
        pass
    try:
        fileExts1["Description"] = soup.find(
            "div", attrs={"class": "infoBox"}
        ).text.strip()
    except:
        pass

    return fileExts1
