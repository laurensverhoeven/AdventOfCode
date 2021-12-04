#!/usr/bin/env python3

NumberOfPlayers, LastMarbleValue = 459, 71790
NumberOfPlayers, LastMarbleValue = 459, 7179000

Score = { PlayerNumber: 0 for PlayerNumber in range( NumberOfPlayers  ) }
MarbleCircle = [0]
CurrentMarble = 0
IndexOfCurrentMarble = MarbleCircle.index(CurrentMarble)

for NewMarble in range(1, LastMarbleValue + 1):
    # print( "Getting marble " + str(NewMarble).rjust(len(str(LastMarbleValue))) + " of " + str(LastMarbleValue) + " ( " + "%0.3f" % float((NewMarble / LastMarbleValue) * 100) + "% )")

    if NewMarble % 23 == 0:
        IndexOfMarbleToRemove = (IndexOfCurrentMarble - 7) % len(MarbleCircle)
        Score[NewMarble % NumberOfPlayers] += MarbleCircle[IndexOfMarbleToRemove] + NewMarble
        del MarbleCircle[IndexOfMarbleToRemove]
        IndexOfCurrentMarble = IndexOfMarbleToRemove
    else:
        IndexOfCurrentMarble = ( IndexOfCurrentMarble + 2 )% len(MarbleCircle)
        MarbleCircle.insert(IndexOfCurrentMarble, NewMarble)


Scores = []
for Player in Score:
    Scores.append(Score[Player])
    # print("The score of player " + str(Player).rjust(len(str(NumberOfPlayers))) + " is " + str(Score[Player]) )

WinningScore = max(Scores)
WinningPlayers = [Player for Player in Score if Score[Player] == WinningScore]

print("The players that win are: ", WinningPlayers)

print("What is the winning Elf's score?")
print( max(Scores) )
