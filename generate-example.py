import secretSanta.santaReader as reader
import secretSanta.generateData as generate

exclusionsFile     = 'example-exclusions.csv'
years              = [y for y in range(2015,2021)]
gifts              = 2
samples            = 10000
nonParticipants    = []
hardExclusionYears = 3
showScores         = True

exclusions = reader.readExclusions(exclusionsFile)
people = list(exclusions.keys())    

generate.generate(people,years,exclusions=exclusions,gifts=gifts,samples=samples,hardExclusionYears=hardExclusionYears,showScores=showScores)
