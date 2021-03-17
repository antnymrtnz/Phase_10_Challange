#phase 10 challange
#Purpose of this function is when given a hand of 10 cards from the deck, returns all phases the hand meets
#Written and tested by Anthony R. Martinez
from random import shuffle
class Cards:
#create an array as our deck of cards with eight of every card for 96 total
    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] * 8

#shuffle the array as in shuffling a deck of cards
    def shuffle(self):
        shuffle(self.deck)

#deal out top ten values from the array like dealing out cards and store them in another array
    def deal(self):
        self.hands = self.deck[:10]
#sort the new array of ten values from least to greatest, this will help with checking the phases this hand meets
        self.hands.sort()

    def phaseMet(self):
        import collections
#count the amount pairs in the array of ten values, store that value in another array and count how many values are in that array
        self.phase_1 = [item for item, count in collections.Counter(self.hands).items() if count >= 3]
        self.phase_7 = [item for item, count in collections.Counter(self.hands).items() if count >= 4]
        self.phase_9_1 = [item for item, count in collections.Counter(self.hands).items() if count >= 5]
        self.phase_9_2 = [item for item, count in collections.Counter(self.hands).items() if count >= 2]
        self.phase_10_1 = [item for item, count in collections.Counter(self.hands).items() if count >= 5]
        self.phase_10_2 = [item for item, count in collections.Counter(self.hands).items() if count >= 3]

        self.ans = 0
        self.count = 0
        self.hands.sort()
        self.v = []
        self.n = len(self.hands)
#logic that finds a run, consecutive numbers in ascending order
        self.v.append(self.hands[0])
        for i in range(1, self.n):
            if (self.hands[i] != self.hands[i - 1]):
                self.v.append(self.hands[i])
        for i in range(len(self.v)):
            if (i > 0 and self.v[i] == self.v[i - 1] + 1):
                self.count += 1
            else:
                self.count = 1
            self.ans = max(self.ans, self.count)

#test for phase 1
        if len(self.phase_1) >= 2:
            print("Phase 1 met")
        else:
            print("Phase 1 not met")
#test for phase 2
        if self.ans >= 4 and len(self.phase_1) >= 1:
            print("Phase 2 met")
        else:
            print("Phase 2 not met")
#test for phase 3
        if self.ans >= 4 and len(self.phase_7) >= 1:
            print("Phase 3 met")
        else:
            print("Phase 3 not met")
#test for phase 4
        if self.ans >= 7:
            print("Phase 4 met")
        else:
            print("Phase 4 not met")
#test for phase 5
        if self.ans >= 8:
            print("Phase 5 met")
        else:
            print("Phase 5 not met")
#test for phase 6
        if self.ans >= 9:
            print("Phase 6 met")
        else:
            print("Phase 6 not met")
#test for phase 7
        if len(self.phase_7) >= 2:
            print("Phase 7 met")
        else:
            print("Phase 7 not met")
#test for phase 9
        if len(self.phase_9_1) >= 1 and len(self.phase_9_2) >= 1:
            print("Phase 9 met")
        else:
            print("Phase 9 not met")
#test for phase 10
        if len(self.phase_10_1) >= 1 and len(self.phase_10_2) >= 1:
            print("Phase 10 met")
        else:
            print("Phase 10 not met")
#call functions
c = Cards()
c.shuffle()
c.deal()
print (c.hands)
c.phaseMet()
