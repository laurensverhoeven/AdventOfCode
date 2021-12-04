#!/usr/bin/env python3

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def SpanGrid( SmallestX, SmallestY, LargestX, LargestY ):

   # GridEdges = ( (SmallestX, SmallestY), (LargestX, LargestY) )

   # print(SmallestX, SmallestY, LargestX, LargestY)

   XRange = range(SmallestX, LargestX + 1)
   YRange = range(SmallestY, LargestY + 1)

   CoordinateList = [ (x, y) for y in YRange for x in XRange ]

   # print(CoordinateList[0: 100])

   Grid = {Coordinate: {} for Coordinate in CoordinateList }
   return(Grid)

def GetRackID(Coordinate):
   RackID = Coordinate[0] + 10
   return(RackID)

def GetPowerLevel(Coordinate, SerialNumber):
   (x, y) = Coordinate
   RackID = GetRackID(Coordinate)
   PowerLevel = RackID * y
   PowerLevel += SerialNumber
   PowerLevel = PowerLevel * RackID
   PowerLevel = int(str(int(PowerLevel))[-3])
   PowerLevel -= 5

   return(PowerLevel)

def main():

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day11/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   Lines = ReadFile(InputFile)

   SerialNumber = int(Lines[0])
   # SerialNumber = 18

   

   SmallestX, SmallestY, LargestX, LargestY = (1, 1, 300, 300)
   Grid = SpanGrid(SmallestX, SmallestY, LargestX, LargestY)
   # print(Grid)

   AllCoordinates = [Coordinate for Coordinate in Grid]
   for Coordinate in AllCoordinates:
      PowerLevel = GetPowerLevel(Coordinate, SerialNumber)
      # print(PowerLevel)
      Grid[Coordinate]["PowerLevel"] = PowerLevel

   
   for Coordinate in AllCoordinates:
      (XCoordinate, YCoordinate) = Coordinate
      if XCoordinate <= 297 and YCoordinate <= 297:
         CoordinatesOfSquare = [ (x, y) for x in range(XCoordinate, XCoordinate + 3) for y in range(YCoordinate, YCoordinate + 3) ]
         TotalPowerlevel = 0
         for SquareCoordinate in CoordinatesOfSquare:
            TotalPowerlevel += Grid[SquareCoordinate]["PowerLevel"]
         Grid[Coordinate]["SquarePowerLevel"] = TotalPowerlevel
         # print(TotalPowerlevel)

   SquarePowerLevel = []
   for Coordinate in AllCoordinates:
      if "SquarePowerLevel" in Grid[Coordinate]:
         SquarePowerLevel.append(Grid[Coordinate]["SquarePowerLevel"])

   MaxSquarePowerLevel = max(SquarePowerLevel)

   MaxSquarePowerLevel = 0
   VarSquarePowerLevel = []
   # for SquareSide in range(300):
   for SquareSide in range(8, 9):
      print("SquareSide:", SquareSide)
      for Coordinate in AllCoordinates:
         (XCoordinate, YCoordinate) = Coordinate
         # SquareSide = 3
         if XCoordinate <= 300 - SquareSide and YCoordinate <= 300 - SquareSide:
            CoordinatesOfSquare = [ (x, y) for x in range(XCoordinate, XCoordinate + SquareSide) for y in range(YCoordinate, YCoordinate + SquareSide) ]
            TotalPowerlevel = 0
            for SquareCoordinate in CoordinatesOfSquare:
               TotalPowerlevel += Grid[SquareCoordinate]["PowerLevel"]
            Grid[Coordinate]["SquarePowerLevel" + str(SquareSide)] = TotalPowerlevel
            # if TotalPowerlevel > 28:
            #    print("TotalPowerlevel: ", TotalPowerlevel)
            # print(TotalPowerlevel)
      for Coordinate in AllCoordinates:
         if "SquarePowerLevel" + str(SquareSide) in Grid[Coordinate]:
            VarSquarePowerLevel.append(Grid[Coordinate]["SquarePowerLevel" + str(SquareSide)])
      if max(VarSquarePowerLevel) > MaxSquarePowerLevel:
         OldMaxSquarePowerLevel = MaxSquarePowerLevel
         MaxSquarePowerLevel = max(VarSquarePowerLevel)
         print("MaxSquarePowerLevel increased from " + str(OldMaxSquarePowerLevel) + " to " + str(MaxSquarePowerLevel))

   MaxSquarePowerLevel = max(VarSquarePowerLevel)

   for SquareSide in range(300):
      for Coordinate in AllCoordinates:
         if "SquarePowerLevel" + str(SquareSide) in Grid[Coordinate]:
            if Grid[Coordinate]["SquarePowerLevel" + str(SquareSide)] == MaxSquarePowerLevel:
               print(Coordinate, SquareSide, Grid[Coordinate])

   # Coordinate = (  3,  5); SerialNumber =  8; print(GetPowerLevel(Coordinate, SerialNumber))
   # Coordinate = (122, 79); SerialNumber = 57; print(GetPowerLevel(Coordinate, SerialNumber))
   # Coordinate = (217,196); SerialNumber = 39; print(GetPowerLevel(Coordinate, SerialNumber))
   # Coordinate = (101,153); SerialNumber = 71; print(GetPowerLevel(Coordinate, SerialNumber))

   return()

if __name__ == "__main__":
   main()
   