from collections import defaultdict

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://fileinfo.com/extension/"


def scrapeFileinfo(extension):
    fileExts = defaultdict(lambda: ["Format not found"])
    fileExts["Extension"] = extension
    try:
        reqContent = requests.get(
            BASE_URL + extension
        )  # make a request to website , with specific extension

        soup = BeautifulSoup(
            reqContent.content, "html5lib"
        )  # parse the response using a html5lib parser

    except Exception as e:
        print(e)
        return fileExts

    try:
        fileExts["Name"] = soup.find(
            "h2", attrs={"class": "title"}
        ).text  # extract different data
    except:
        pass
    try:
        obj = soup.find("table", attrs={"class": "headerInfo"}).text.split()
        fileExts["Format"] = obj[-1]
        fileExts["Popularity"] = obj[obj.index("Popularity") + 1]
        fileExts["Category"] = obj[obj.index("Category") + 1]
    except:
        pass
    try:
        fileExts["Description"] = soup.find(
            "div", attrs={"class": "infoBox"}
        ).text.strip()
    except:
        pass
    print("returning dict1")
    return fileExts
