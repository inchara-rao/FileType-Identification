import requests
from bs4 import BeautifulSoup
from lxml import etree

BASE_URL = "https://filext.com/file-extension/"


def scrapeFileext(extension):
    fileExts2 = {}
    try:
        res = requests.get(BASE_URL + extension)
        soup = BeautifulSoup(res.text, "lxml")
        response = etree.HTML(str(soup))
        if soup.find("title").text == '404 - File not found':
            # print(extension)
            return fileExts2
    except Exception as e:
        print(e)
        return fileExts2

    try:
        primaryAssociation = response.xpath(
            "//div[@class='content']/div[@class='flex-container']/div/p/em/span/text()"
        )

        fileExts2["Primarily associated with"] = primaryAssociation[0]
    except:
        pass

    try:

        fileType = response.xpath(
            "//div[@class='teaser']/table[@class='head']/tr[2]/td[2]/strong/text()"
        )

        fileExts2["File type"] = fileType[0]
    except:
        pass
    try:
        description = response.xpath("//main/div[@class='content']/p[1]/text()")

        description.insert(
            1, response.xpath("//main/div[@class='content']/p[1]/span/text()")[0]
        )
        fileExts2["Description"] = "".join(description)
    except:
        pass
    try:
        howToOpen = response.xpath("//main/div[@class='content']/p[2]/text()")
        missedText = response.xpath("//main/div[@class='content']/p[2]/strong/text()")
        i, j, final = 0, 0, []
        while i < len(howToOpen) or j < len(missedText):
            if i < len(howToOpen):
                final.append(howToOpen[i])
            if j < len(missedText):
                final.append(missedText[j])
            i += 1
            j += 1
        fileExts2["Methods to open the file"] = ("".join(final)).replace("\n", "")
    except:
        pass
    try:
        techincalInfo = (
            soup.find("div", attrs={"class": "table"})
            .text.replace("\xa0", " ")
            .split("\n")[1:-1]
        )

        for i in techincalInfo:
            fileExts2[i.split(":")[0]] = i.split(":")[-1]

        if "Related links" in fileExts2:
            fileExts2.pop("Related links")
    except:
        pass

    try:

        solveProblems = response.xpath(
            "//main/div[@class='content']/ul[@class='ulist']"
        )[0]

        solveProblems = solveProblems.xpath(
            ".//li/span/text() | .//li[1]/span/span[@id='os-selected']/text() | .//li/span/a/text() | .//li[2]/span/em/text()"
        )

        fileExts2["Information to solve problems"] = ("".join(solveProblems)).replace(
            "\n", " "
        )
    except:
        pass

    return fileExts2
