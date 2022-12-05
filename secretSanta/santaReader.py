import csv

def readHistory(historyFile):
    history = {}
    with open(historyFile, newline='') as csvfile:
        historyData = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = next(historyData)
        years = [int(y) for y in header[1:]]
        for row in historyData:
            giver = row[0]
            history[giver] = {}
            for year, recipient in zip(years,row[1:]):
                if recipient:
                    if recipient in history[giver]:
                        # List started, append to it
                        history[giver][recipient].append(year)
                    else:
                        # Create list
                        history[giver][recipient] = [year]
    return history

def readExclusions(exclusionsFile):
    exclusions = {}
    with open(exclusionsFile, newline='') as csvfile:
        exclusionsData = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = next(exclusionsData)
        for row in exclusionsData:
            giver = row[0]
            exclusions[giver] =list(filter(lambda a: a != '',row[1:]))
    return exclusions