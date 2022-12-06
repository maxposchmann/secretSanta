import secretSanta.santaReader as sr

def setup(historyFile,exclusionsFile):
    history = sr.readHistory(historyFile)
    exclusions = sr.readExclusions(exclusionsFile)

    people = list(history.keys()) + list(set(exclusions.keys()) - set(history.keys()))

    return people, history, exclusions