import random

class game:
  def __init__(self):
    self.mainDeck = []
    self.p1 = 0
    self.p2 = 0
    self.deck1 = []
    self.deck2 = []
    self.warpile = []
    self.roundCounter = 0
    
    for i in range(13):
      for p in range(4):
        self.mainDeck.append(i+1)
    random.shuffle(self.mainDeck)
    
    for i in range(52):
      if(i % 2 ==0):
        self.deck1.append(self.mainDeck[i])
      else:
          self.deck2.append(self.mainDeck[i])
    
    while len(self.deck1) < 49 and len(self.deck2) < 49:
      self.drawCard()
      if self.roundCounter >= 256:
        break
      if len(self.deck1) > len(self.deck2):
        print("wow wow you kind of did good")
      elif len(self.deck2) > len(self.deck1):
        print("wow wow you kind of did good sike")
      else:
          print("tie")
      
      
    
  def drawCard(self):
    self.p1 = self.deck1[0]
    self.p2 = self.deck2[0]
    self.deck1.pop(0)
    self.deck2.pop(0)
    self.judge()
    self.roundCounter += 1

  def war(self):
    
    self.warpile.extend([self.p1, self.p2])
    self.warpile.append(self.deck1.pop(0))
    self.warpile.append(self.deck2.pop(0))
    self.drawCard()

  def judge(self):
    if self.p1 > self.p2:
      print("p1 had", self.p1, "p2 had", self.p2)
      
      if len(self.warpile) > 1:
        self.deck1.extend(self.warpile)
        self.warpile = []
        self.deck2.extend(self.p1)
      print("p1's deck is at", len(self.deck1))
    elif self.p1 < self.p2:
      print("p1 had", self.p1, "p2 had", self.p2)
      
      if len(self.warpile) > 1:
        self.deck2.extend(self.warpile)
        self.warpile = []
      print("p2's deck is at", len(self.deck2))
    else:
      print("a tie accurd")
      print("p1 had", self.p1, "p2 had", self.p2)
      self.war()
      
obj = game()