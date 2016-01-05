
from cities import *

import random

class PlayerDeck:

    def __init__(s, intEpidemics=4):
        s.deck = allCities.keys() + events
        random.shuffle(s.deck)

        numCards = len(s.deck)
        remainder = numCards % (numCards / intEpidemics)


        ## calculate partitions where the epidemics should go between
        partitions = [0]

        adds = list()
        for i in range(intEpidemics):
            if i < remainder: adds.append(1)
            else: adds.append(0)

        random.shuffle(adds)


        for i in range(intEpidemics):
            partitions.append(i+adds[i] + partitions[i] + numCards/intEpidemics)

        print numCards+intEpidemics
        print partitions

        # actually insert the epidemics
        for i in range(intEpidemics):
            r = random.randint(partitions[i],partitions[i+1])
            print 'inserted epidemic at', r
            s.deck.insert(r,'epidemic')

           
    def flipTwo(s):
        return [s.deck.pop(), s.deck.pop()]




#pd = PlayerDeck(5)

#print pd.flipTwo()
###print pd.flipTwo()
#print pd.flipTwo()
#print pd.flipTwo()
#print pd.flipTwo()
#print pd.flipTwo()
#print pd.flipTwo()
#print pd.flipTwo()
