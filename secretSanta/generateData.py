import secretSanta.santaOptimizer as optimizer

def generate(people,years,history=None,exclusions=None,gifts=1,samples=10,hardExclusionYears=0,showScores=False):
    if not history:
        # Create an empty history
        history = {}
        for person in people:
            history[person] = {}
    for year in years:
        bestCombo, best, totalSamples, validSamples = optimizer.optimize(people,history,exclusions,currentYear=year,gifts=gifts,samples=samples,hardExclusionYears=hardExclusionYears)
        print(f'------- Year: {year} -------')
        optimizer.display(bestCombo, best, totalSamples, validSamples,showScores=showScores)
        writeHistory(history,bestCombo,year)

def writeHistory(history,update,year):
    for giver in update.keys():
        # Add giver to history if necessary
        if giver not in history.keys():
            history[giver] = {}
        for recipient in update[giver].keys():
            # Add recipient to giver history if necessary
            if recipient not in history[giver].keys():
                history[giver][recipient] = []
            history[giver][recipient].append(year)
