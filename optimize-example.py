import secretSanta.santaOptimizer as optimizer
import secretSanta.santaSetup as setup

historyFile        = 'example-history.csv'
exclusionsFile     = 'example-exclusions.csv'
currentYear        = 2022
gifts              = 2
samples            = 10
nonParticipants    = []
hardExclusionYears = 3
showScores         = False

people, history, exclusions = setup.setup(historyFile,exclusionsFile)

bestCombo, best, totalSamples, validSamples = optimizer.optimize(people,history,exclusions,currentYear=currentYear,gifts=gifts,samples=samples,nonParticipants=nonParticipants,hardExclusionYears=hardExclusionYears)

optimizer.display(bestCombo, best, totalSamples, validSamples, showScores = showScores)
