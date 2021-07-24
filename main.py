from parsers.fileExt import scrapeFileext
from parsers.fileInfo import scrapeFileinfo


def writeToFile(dictionary):
    outputFile = open("output/output.txt", "a")  # write to output file in append mode
    for key, value in dictionary.items():
        # print(f"{key}:{value}")
        outputFile.writelines(
            f"{key}:{value}\n"
        )  # for each key,value pair write to file
    outputFile.writelines("\n\n")
    outputFile.close()  # close the file when done writing


def readFromFile():
    fileName = input("Enter filename for input ,present in input folder:")
    try:
        with open("input/" + fileName) as file:  # reading input file
            fileFile = file.read()
    except Exception:
        print(
            "Using default input file:inpu0.csv , as no input file found"
        )  # if no input file found , use default input file
        with open("input/input0.csv") as file:
            fileFile = file.read()
    fileNames = fileFile.strip().split()
    return fileNames


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


if __name__ == "__main__":

    fileNames = readFromFile()
    outputFile = open("output/output.txt", "w")
    outputFile.close()

    for file in fileNames:  # for each input in the file find info about extension
        extension = file.split(".")[-1]  # extract the extension
        print(
            "------------------------------------------------------------------------------------------------------------------------"
        )
        d1 = scrapeFileinfo(extension)  # call findExt functon for each extension
        d2 = scrapeFileext(extension)
        d3 = Merge(d1, d2)

        writeToFile(d3)
