import secretSanta.santaReader as sr

def setup(historyFile,exclusionsFile):
    history = sr.readHistory(historyFile)
    exclusions = sr.readExclusions(exclusionsFile)

    people = list(history.keys()) + list(set(exclusions.keys()) - set(history.keys()))

    numberOfExclusions = []
    for person in people:
        try:
            numberOfExclusions.append(len(exclusions[person]))
        except KeyError:
            numberOfExclusions.append(0)

    # Sort list by number of exclusions for better performance
    people = [x for _,x in sorted(zip(numberOfExclusions, people),reverse=True)]
    
    return people, history, exclusions