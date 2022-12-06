import numpy as np
import random
import copy
import datetime

year = datetime.date.today().year

def optimize(people,history,exclusions,currentYear=year,gifts=1,samples=10,nonParticipants=[],hardExclusionYears=0):
    # Exclude people not participating this year
    for nonParticipant in nonParticipants:
        people.remove(nonParticipant)

    # Generate list of valid recipients for each giver
    recipients = {}
    for giver in people:
        recipients[giver] = people.copy()
        recipients[giver].remove(giver)
        # Remove exclusions from valid list
        if giver in exclusions.keys():
            for exclusion in exclusions[giver]:
                try:
                    recipients[giver].remove(exclusion)
                except ValueError:
                    # Likely non-participant, possible duplicate
                    pass
        # If hard exclusion for recipients from recent years specified, remove using history
        if hardExclusionYears:
            if giver in history.keys():
                for person in history[giver].keys():
                    for y in history[giver][person]:
                        if (currentYear - y) <= hardExclusionYears:
                            try:
                                recipients[giver].remove(person)
                            except ValueError:
                                # Likely non-participant or duplicate duplicate
                                pass

    numberOfValidRecipients = []
    for person in people:
        numberOfValidRecipients.append(len(recipients[person]))
    # Sort list by number of exclusions for better performance
    people = [x for _,x in sorted(zip(numberOfValidRecipients, people))]
    print(people)

    totalSamples = 0
    validSamples = 0
    best = np.inf
    bestCombo = {}
    for _ in range(samples):
        totalSamples = totalSamples + 1
        combo = {}
        rating = 0
        # Set up number of gifts required per person
        remaining = {}
        for person in people:
            remaining[person] = gifts
        # Loop over givers and choose recipients at random
        tempRecipients = copy.deepcopy(recipients)
        for giver in people:
            combo[giver] = {}
            try:
                choice = random.sample(tempRecipients[giver],gifts)
            except ValueError:
                # If sample can't be drawn, cancel
                rating = rating + np.inf
                break

            for person in choice:
                individualRating = 0
                # Calculate score
                try:
                    if person in history[giver].keys():
                        for year in history[giver][person]:
                            individualRating = individualRating + 2.0**(year - currentYear)
                except KeyError:
                    # No history for this giver, that's fine
                    pass
                # Store choice and score
                combo[giver][person] = individualRating
                rating = rating + individualRating
                # Update potential recipient lists
                # Remove from giver's list (no duplicate gifts)
                tempRecipients[giver].remove(person)
                # De-increment counters
                remaining[person] = remaining[person] - 1
                # If a recipient has enough givers, remove them from all lists
                if remaining[person] == 0:
                    for potentialGiver in people:
                        if person in tempRecipients[potentialGiver]:
                            tempRecipients[potentialGiver].remove(person)
        # Count valid samples
        if rating < np.inf:
            validSamples = validSamples + 1
        # Compare rating to best
        if rating < best:
            best = rating
            bestCombo = combo
            if rating == 0:
                # Call it for perfect score
                break
    return bestCombo, best, totalSamples, validSamples

def display(bestCombo, best, totalSamples, validSamples, showScores = False):
    print(f'Best score was {best} after {totalSamples} total samples, {validSamples} valid samples')
    print()
    for giver in bestCombo.keys():
        print(f'Santa {giver} has recipients:')
        if showScores:
            print(', '.join([f'{k}: {v}' for k,v in bestCombo[giver].items()]))
        else:
            print(', '.join(bestCombo[giver].keys()))
        print()