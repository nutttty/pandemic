
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



id = InfectionDeck()

print id.initialCities()

#print id.flip(2)
#print id.flip(2)
#print id.flip(2)
#print id.flip(2)

#print id.drawBottom()
#id.reshuffleDiscard()


#print id.flip(2)
#print id.flip(2)
#print id.drawBottom()
#id.reshuffleDiscard()

#print id.flip(2)
#print id.flip(2)
#print id.flip(2)
#print id.flip(2)
#print id.flip(2)
