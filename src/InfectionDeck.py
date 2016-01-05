
from cities import *
import random

class InfectionDeck:

    def __init__(s):
        s.deck = [allCities.keys()]
        random.shuffle(s.deck[0])
        s.discard = []


    def initialCities(s):
        if len(s.deck) > 1: print "BAD: calling initial cities when deck no in initial state. continuing anyway"
        cities = [[],[],[]]

        for i in [0,1,2]:
            for j in [0,0,0]:
                cities[i].append(s.deck[0].pop())
            s.discard.extend(cities[i])
            
        return cities


    def flip(s, intToFlip):
        flipped = list()

        while intToFlip > 0:

            while s.deck[-1] == []: s.deck.pop()
            flipped.append(s.deck[-1].pop())
            intToFlip -= 1


        s.discard.extend(flipped)
        return flipped


    def drawBottom(s):
        card = s.deck[0].pop(0)
        s.discard.append(card)
        return card



    def reshuffleDiscard(s):
        random.shuffle(s.discard)
        s.deck.append(s.discard)
        s.discard = []

    def probability(s,cityName, intNum, offset=0):
        if offset <= 0: return s.probabilityNow(cityName, intNum)
        return s.probabilityLater(cityName, intNum, offset)


    def probabilityNow(s, cityName, intNum):
        
        print 'deck -------'
        print s.deck
        print

        remain = intNum

        for i in reversed(s.deck):
            if cityName in i:
                # we will draw past that city, so definitely drawing it:
                if len(i) <= remain: return 1.
            
                # drawing will end in current block of cards
                if len(i) > remain:
                    p = float(remain) / len(i)
                    return p

            # city was not in that group so go on
            remain -= len(i)
            if remain <= 0: break

        # end loop and haven't found
        return 0.


    def probabilityLater(s,cityName, intNum, intOffset):

        count = 0
        for i in reversed(s.deck):
            
            if cityName in i:
                if intOffset >= count+len(i): return 0.
                numDraws = intNum

                # adjust endpoints of how many to draw from this group:
                if intOffset < count:
                    numDraws -= (count-intOffset)
                if intOffset+intNum > count+len(i):
                    numDraws -= (intOffset+intNum-count-len(i))

                return max(float(numDraws) / len(i), 0.)

            count += len(i)
            if count >= intNum+intOffset: break

        return 0.



id = InfectionDeck()

print id.initialCities()

print id.flip(2)
print id.flip(2)
#print id.flip(2)
#print id.flip(2)

c = id.drawBottom()
print c
id.reshuffleDiscard()

print id.probability(c,2)


print id.flip(2)
print id.probability(c,2)

#print id.flip(2)
print id.drawBottom()
id.reshuffleDiscard()
print id.probability(c,2)
print id.probability(c,2,2)
print id.probability(c,2,4)
print id.probability(c,2,6)
print id.probability(c,2,8)
print id.probability(c,2,10)
print id.probability(c,2,12)
print id.probability(c,2,14)
print id.probability(c,2,16)

#print id.flip(2)
#print id.flip(2)
#print id.flip(2)
#print id.flip(2)
#print id.flip(2)
