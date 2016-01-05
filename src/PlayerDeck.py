
from cities import *

import random

class PlayerDeck:

    def __init__(s, intEpidemics=4):
        s.deck = allCities.keys() + events
        random.shuffle(s.deck)

        numCards = len(s.deck)
        remainder = numCards % (numCards / intEpidemics)


        ## calculate partitions where the epidemics should go between
        s.partitions = [0]

        adds = list()
        for i in range(intEpidemics):
            if i < remainder: adds.append(1)
            else: adds.append(0)

        random.shuffle(adds)

        print adds

        for i in range(intEpidemics):
            s.partitions.append(1+adds[i] + s.partitions[i] + numCards/intEpidemics)

        print numCards+intEpidemics
        print s.partitions

        # actually insert the epidemics
        for i in range(intEpidemics):
            r = random.randint(s.partitions[i],s.partitions[i+1])
            s.deck.insert(r,'epidemic')

           
    def flipTwo(s):
        # todo: check if enough cards
        return [s.deck.pop(), s.deck.pop()]

    def turnsRemaining(s):
        return ceil(len(s.deck) / 2.)

    def probabilityEpidemic(s):
        
        # trim partitions so that only the last is a spot past the top of the deck
        while s.partitions[-2] >= len(s.deck): s.partitions.pop()
        s.partitions[-1] = len(s.deck) # last one is at top of deck

        toDrawFrom = s.partitions[-1] - s.partitions[-2] 

        p = 0.

        # check out the next partition in the case we draw from that one too
        if toDrawFrom == 1 and len(s.partitions) > 2:
            p = 1. / (s.partitions[-2] - s.partitions[-3])

        # assuming we having seen the epidemic in this partition, get the probability
        if 'epidemic' in s.deck[s.partitions[-2]:s.partitions[-1]]:
            p = min(p+(min(2., float(toDrawFrom)) / toDrawFrom), 1.)

        return p

    def __str__(s):

        if len(s.deck) > 10: d = s.deck[-9:]
        else: d = s.deck

        d.reverse()
        return 'deck-----\n' + '\n'.join(d)
        




pd = PlayerDeck(7)



print pd
print pd.probabilityEpidemic()
print pd.flipTwo()
print pd.probabilityEpidemic()
print pd.flipTwo()
print pd.probabilityEpidemic()
print pd.flipTwo()
print pd.probabilityEpidemic()
print pd.flipTwo()
print pd.probabilityEpidemic()
print pd.flipTwo()
print pd
print pd.flipTwo()
print pd.probabilityEpidemic()
print pd.flipTwo()
print pd.probabilityEpidemic()
print pd.flipTwo()
print pd.probabilityEpidemic()
