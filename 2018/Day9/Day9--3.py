#!/usr/bin/env python3


def PlayGame(NumberOfPlayers, LastMarbleValue):
   
   def UpdatePreviousIndex(MarbleIndex, NewIndexOfPreviousMarble):
      Marble, OldIndexOfPreviousMarble, IndexOfNextMarble = MarbleCircle[MarbleIndex]
      # global MarbleCircle
      MarbleCircle[MarbleIndex] = Marble, NewIndexOfPreviousMarble, IndexOfNextMarble

   def UpdateNextIndex(MarbleIndex, NewIndexOfNextMarble):
      Marble, IndexOfPreviousMarble, OldIndexOfPreviousMarble = MarbleCircle[MarbleIndex]
      # global MarbleCircle
      # print(Marble, IndexOfPreviousMarble, NewIndexOfNextMarble)
      MarbleCircle[MarbleIndex] = Marble, IndexOfPreviousMarble, NewIndexOfNextMarble


   def AddAfterMarble(Marble, AddAfterIndex):
      # global MarbleCircle
      OldMarble, IndexOfPreviousMarble, IndexOfNextMarble = MarbleCircle[AddAfterIndex]
      MarbleCircle.append((Marble, AddAfterIndex, IndexOfNextMarble))
      AddMarbleIndex = len(MarbleCircle) - 1
      UpdatePreviousIndex(IndexOfNextMarble, AddMarbleIndex)
      UpdateNextIndex(AddAfterIndex, AddMarbleIndex)
      return(AddMarbleIndex)
      
      
   def RemoveMarble(IndexOfMarbleToRemove):
      # global MarbleCircle
      MarbleToRemove, IndexOfPreviousMarble, IndexOfNextMarble = MarbleCircle[IndexOfMarbleToRemove]
      UpdateNextIndex(IndexOfPreviousMarble, IndexOfNextMarble)
      UpdatePreviousIndex(IndexOfNextMarble, IndexOfPreviousMarble)
      return(MarbleToRemove, IndexOfNextMarble)
      
      
   def GetNextMarbelIndex(MarbleIndex, n = 1):
      for i in range(n):
         MarbleIndex = MarbleCircle[MarbleIndex][2]
      return(MarbleIndex)
      
   def GetPreviousMarbelIndex(MarbleIndex, n = 1):
      for i in range(n):
         MarbleIndex = MarbleCircle[MarbleIndex][1]
         # print(MarbleIndex)
      return(MarbleIndex)
      
   def GetNormalList(MarbleCircle):
      # print(MarbleCircle)
      List = []
      CurrentMarbelIndex = 0
      for i in range(len(MarbleCircle)):
         # print(i)
         # print(MarbleCircle[CurrentMarbelIndex][0])
         List.append(MarbleCircle[CurrentMarbelIndex][0])
         CurrentMarbelIndex = GetNextMarbelIndex(CurrentMarbelIndex)
      return(List)

   def PrintMarbleCircle(MarbleCircle, CurrentMarble = False, CurrentPlayer = "-"):

      MarbleList = GetNormalList(MarbleCircle)

      ReorderedMarbleList = [MarbleList[-1]] + MarbleList[0:-1]

      if CurrentMarble and False:
         CurrentMarbleIndex = ReorderedMarbleList.index(CurrentMarble)
         ReorderedMarbleList[CurrentMarbleIndex] = "(" + str(ReorderedMarbleList[CurrentMarbleIndex]) + ")"

      
      # MarbleDigits = max( [ len(str(Marble)) for Marble in ReorderedMarbleCircle ] )
      MarbleDigits = 2
      Marbles = [ " " + str(Marble).rjust(MarbleDigits)  for Marble in ReorderedMarbleList ]

      Marbles = "".join(Marbles) + " " 
      if CurrentMarble:
         Marbles = Marbles.replace(" " + str(CurrentMarble) + " ", "(" + str(CurrentMarble) + ")")

      if CurrentPlayer == 0:
         CurrentPlayer = NumberOfPlayers
      CurrentPlayerString = "[" + str(CurrentPlayer) + "]"
      Marbles = CurrentPlayerString + Marbles

      print(Marbles)


   print("Playing with " + str(NumberOfPlayers) + " players and " + str(LastMarbleValue) + " marbles.")

   Score = { PlayerNumber: 0 for PlayerNumber in range( NumberOfPlayers  ) }
   MarbleCircle = [(0, 0, 0)]
   IndexOfCurrentMarble = 0

   for NewMarble in range(1, LastMarbleValue + 1):
      # print( "\nGetting marble " + str(NewMarble).rjust(len(str(LastMarbleValue))) + " of " + str(LastMarbleValue) + " ( " + "%0.3f" % float((NewMarble / LastMarbleValue) * 100) + "% )")

      # print(IndexOfCurrentMarble)
      # print(MarbleCircle)
      # print(GetNormalList(MarbleCircle))

      # print(NewMarble, LastMarbleValue)
      if NewMarble % 23 == 0:
         IndexOfMarbleToRemove = GetPreviousMarbelIndex(IndexOfCurrentMarble, 7)
         # print(IndexOfMarbleToRemove)
         MarbleToRemove, IndexOfCurrentMarble = RemoveMarble(IndexOfMarbleToRemove)
         # print("MarbleToRemove, NewMarble: ", MarbleToRemove, NewMarble)
         Score[NewMarble % NumberOfPlayers] += MarbleToRemove + NewMarble
      else:
         AddAfterIndex = GetNextMarbelIndex(IndexOfCurrentMarble, 1)
         IndexOfCurrentMarble = AddAfterMarble(NewMarble, AddAfterIndex)

      # print("IndexOfCurrentMarble:", IndexOfCurrentMarble)
      # print(MarbleCircle)
      # print(GetNormalList(MarbleCircle))
      # PrintMarbleCircle(MarbleCircle, NewMarble, NewMarble % NumberOfPlayers)

   Scores = []
   for Player in Score:
      Scores.append(Score[Player])
      # print("The score of player " + str(Player).rjust(len(str(NumberOfPlayers))) + " is " + str(Score[Player]) )

   WinningScore = max(Scores)
   WinningPlayers = [Player for Player in Score if Score[Player] == WinningScore]

   print("With " + str(NumberOfPlayers) + " players and " + str(LastMarbleValue) + " marbles, The players that win are:", WinningPlayers)
   print("What is the winning Elf's score?")
   print( max(Scores) )
   


NumberOfPlayers, LastMarbleValue = 459, 71790000; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers, LastMarbleValue = 459, 7179000; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers, LastMarbleValue = 459, 71790; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers =  9; LastMarbleValue = 25; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers = 10; LastMarbleValue = 1618; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers = 13; LastMarbleValue = 7999; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers = 17; LastMarbleValue = 1104; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers = 21; LastMarbleValue = 6111; PlayGame(NumberOfPlayers, LastMarbleValue)
NumberOfPlayers = 30; LastMarbleValue = 5807; PlayGame(NumberOfPlayers, LastMarbleValue)
