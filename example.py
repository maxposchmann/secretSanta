import secretSanta.santaOptimizer as optimizer
import secretSanta.santaSetup as setup

historyFile     = 'exampleData-history.csv'
exclusionsFile  = 'exclusions.csv'
currentYear     = 2022
gifts           = 2
samples         = 10000
nonParticipants = []
showScores      = False

people, history, exclusions = setup.setup(historyFile,exclusionsFile)

bestCombo, best, totalSamples, validSamples = optimizer.optimize(people,history,exclusions,currentYear=currentYear,gifts=gifts,samples=samples,nonParticipants=nonParticipants)

optimizer.display(bestCombo, best, totalSamples, validSamples, showScores = showScores)