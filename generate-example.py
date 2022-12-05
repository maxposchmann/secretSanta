import secretSanta.santaReader as reader
import secretSanta.generateData as generate

exclusionsFile     = 'example-exclusions.csv'
startYear          = 1992
endYear            = 2021
years              = [y for y in range(startYear,endYear+1)]
gifts              = 2
samples            = 10000
nonParticipants    = []
hardExclusionYears = 3
showScores         = True

exclusions = reader.readExclusions(exclusionsFile)
people = list(exclusions.keys())    

generate.generate(people,years,exclusions=exclusions,gifts=gifts,samples=samples,hardExclusionYears=hardExclusionYears,showScores=showScores)
