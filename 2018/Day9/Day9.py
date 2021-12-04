#!/usr/bin/env python3

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def ParseRuleLine(Line):

   # print(Line)

   NumberOfPlayers = int(Line.split(" players;")[0])
   LastMarbleValue = int( Line.split("last marble is worth ")[1].split(" points")[0] )

   # print(NumberOfPlayers)
   # print(LastMarbleValue)

   return(NumberOfPlayers, LastMarbleValue)

def IsMarbleSpecial(MarbleNumber):
   SpecialMarbleNumber = 23
   Remainder = MarbleNumber % SpecialMarbleNumber

   MarbleIsSpecial = Remainder == 0 and MarbleNumber != 0

   return(MarbleIsSpecial)

def PrintMarbleCircle(MarbleCircle, CurrentMarble = False, CurrentPlayer = "-"):
   ReorderedMarbleCircle = [MarbleCircle[-1]] + MarbleCircle[0:-1]

   if CurrentMarble and False:
      CurrentMarbleIndex = ReorderedMarbleCircle.index(CurrentMarble)
      ReorderedMarbleCircle[CurrentMarbleIndex] = "(" + str(ReorderedMarbleCircle[CurrentMarbleIndex]) + ")"

   
   # MarbleDigits = max( [ len(str(Marble)) for Marble in ReorderedMarbleCircle ] )
   MarbleDigits = 2
   Marbles = [ " " + str(Marble).rjust(MarbleDigits)  for Marble in ReorderedMarbleCircle ]

   Marbles = "".join(Marbles) + " " 
   if CurrentMarble:
      Marbles = Marbles.replace(" " + str(CurrentMarble) + " ", "(" + str(CurrentMarble) + ")")

   CurrentPlayerString = "[" + str(CurrentPlayer) + "]"
   Marbles = CurrentPlayerString + Marbles

   print(Marbles)
   # print( "MarbleCircle: ", Marbles )

def main():

   def PlaceMarble(MarbleNumber, IndexOfCurrentMarble, CurrentPlayer):

      # print("\nPlacing new marble with number: ", MarbleNumber)
      # IndexOfCurrentMarble = MarbleCircle.index(CurrentMarble)

      # CurrentMarble = 0

      # print("MarbleNumber, CurrentMarble: ", MarbleNumber, CurrentMarble)
      if IsMarbleSpecial(MarbleNumber):
         IndexOfMarbleToRemove = (IndexOfCurrentMarble - 7) % len(MarbleCircle)
         # print("IndexOfMarbleToRemove: ", IndexOfMarbleToRemove)
         MarbleToRemove = MarbleCircle[IndexOfMarbleToRemove]
         # print("MarbleToRemove: ", MarbleToRemove)
         del MarbleCircle[IndexOfMarbleToRemove]
         # MarbleToRemove = MarbleCircle2.find()
         # MarbleToRemove = [ (Index, MarbleToRemove) for (Index, MarbleToRemove) in MarbleCircle2 if Index == IndexOfMarbleToRemove]
         # print(MarbleToRemove)
         # MarbleCircle2.remove( MarbleToRemove )

         # print(MarbleCircle)
         # print(IndexOfMarbleToRemove)
         # print(MarbleCircle2)
         # for Position, Marble in enumerate(MarbleCircle2):
         #    # print(Marble[0])
         #    if Marble[0] == IndexOfMarbleToRemove:
         #       # print("Removing marble ", Marble)
         #       MarbleToRemovePosition = Position
         #       MarbleToRemove2 = Marble
         #       break

         # del MarbleCircle2[MarbleToRemovePosition]
         
         IndexOfCurrentMarble = IndexOfMarbleToRemove
         # CurrentMarble = MarbleCircle[IndexOfCurrentMarble]
         PointsScored = MarbleToRemove + MarbleNumber
         # PointsScored = MarbleToRemove2[1] + MarbleNumber
         Score[CurrentPlayer] += PointsScored
      else:

         # MarbleCount = len(MarbleCircle)
         # IndexOfNextMarble = IndexOfCurrentMarble + 1 % MarbleCount
         # IndexOfNextNextMarble = IndexOfCurrentMarble + 2 % MarbleCount
         # print(IndexOfNextMarble, IndexOfNextNextMarble)

         IndexOfNewMarble = IndexOfCurrentMarble + 2 
         IndexOfNewMarble = IndexOfNewMarble % len(MarbleCircle)
         MarbleCircle.insert(IndexOfNewMarble, MarbleNumber)
         # IndexOfNewMarble = IndexOfNewMarble % len(MarbleCircle2)
         # MarbleCircle2.append( (IndexOfNewMarble, MarbleNumber) )
         # print("IndexOfNewMarble: ", IndexOfNewMarble)
         # print("IndexOfNewMarble: ", IndexOfNewMarble)
         # print("CurrentMarble: ", CurrentMarble)
         # print( "MarbleCircle: ", MarbleCircle )
         # print( "MarbleCircle: ", [MarbleCircle[-1]] + MarbleCircle[0:-1] )
         # CurrentMarble = MarbleNumber
         IndexOfCurrentMarble = IndexOfNewMarble
         # PrintMarbleCircle(MarbleCircle, CurrentMarble)
      
      return(IndexOfCurrentMarble)

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day9/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   RuleLines = ReadFile(InputFile)

   NumberOfPlayers, LastMarbleValue = [ ParseRuleLine(RuleLine) for RuleLine in RuleLines ][0]
   NumberOfPlayers, LastMarbleValue = [ ParseRuleLine(RuleLine) for RuleLine in RuleLines ][0]; LastMarbleValue = 100 * LastMarbleValue
   # NumberOfPlayers =  9; LastMarbleValue =   25
   # NumberOfPlayers = 10; LastMarbleValue = 1618
   # NumberOfPlayers = 13; LastMarbleValue = 7999
   # NumberOfPlayers = 17; LastMarbleValue = 1104
   # NumberOfPlayers = 21; LastMarbleValue = 6111
   # NumberOfPlayers = 30; LastMarbleValue = 5807

   Score = { PlayerNumber: 0 for PlayerNumber in range( 1, NumberOfPlayers + 1 ) }

   print("The number of players is " + str(NumberOfPlayers) + ", the value of the last marble is " + str(LastMarbleValue))

   MarbleCircle = [0]
   # MarbleCircle2 = [(0, 0)]
   CurrentMarble = 0
   IndexOfCurrentMarble = MarbleCircle.index(CurrentMarble)
   # IndexOfCurrentMarble = MarbleCircle2.[0][0]

   for RoundNumber in range(0, LastMarbleValue):
      print( "Starting round " + str(RoundNumber).rjust(len(str(LastMarbleValue))) + " of " + str(LastMarbleValue - 1) + " ( " + "%0.3f" % float((RoundNumber / LastMarbleValue) * 100) + "% )")
      CurrentPlayer = RoundNumber % NumberOfPlayers + 1
      # print("RoundNumber, CurrentPlayer: ", RoundNumber, CurrentPlayer)
      NewMarble = RoundNumber + 1
      IndexOfCurrentMarble = PlaceMarble(NewMarble, IndexOfCurrentMarble, CurrentPlayer)
      # PrintMarbleCircle(MarbleCircle, CurrentMarble, CurrentPlayer)

   # PrintMarbleCircle(MarbleCircle, CurrentMarble, CurrentPlayer)
   # for i in MarbleCircle2:
   #    print(i)

   Scores = []
   for Player in Score:
      Scores.append(Score[Player])
      # print("The score of player " + str(Player).rjust(len(str(NumberOfPlayers))) + " is " + str(Score[Player]) )

   WinningScore = max(Scores)
   WinningPlayers = [Player for Player in Score if Score[Player] == WinningScore]

   print("The players that win are: ", WinningPlayers)

   print("What is the winning Elf's score?")
   print( max(Scores) )

   return()

if __name__ == "__main__":
   main()
