#!/usr/bin/env python3

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)


def ParseLocation(LocationLine):

   Location = LocationLine.split(", ")

   Location = tuple([int(Component) for Component in Location])

   return(Location)

def IntToLetter(Int):
   Letter = chr(65 + Int)
   return(Letter)

def CalculateDistance(Coordinate1, Coordinate2):

   XDistance = abs(Coordinate1[0] - Coordinate2[0])
   YDistance = abs(Coordinate1[1] - Coordinate2[1])

   TotalDistance = XDistance + YDistance

   return(TotalDistance)

def SpanGrid(Locations):

   SmallestX = min(Locations, key=lambda x: x[1][0])[1][0]
   SmallestY = min(Locations, key=lambda x: x[1][1])[1][1]
   LargestX = max(Locations, key=lambda x: x[1][0])[1][0]
   LargestY = max(Locations, key=lambda x: x[1][1])[1][1]

   GridEdges = ( (SmallestX, SmallestY), (LargestX, LargestY) )

   XRange = range(SmallestX, LargestX + 1)
   YRange = range(SmallestY, LargestY + 1)

   CoordinateList = [ (x, y) for y in YRange for x in XRange ]

   # print(CoordinateList[0: 100])

   for x in XRange:
      for y in YRange:
         (x, y)

   Grid = {Coordinate: [] for Coordinate in CoordinateList }
   return(Grid)

def most_common(lst):
    return max(set(lst), key=lst.count)

def main():

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day6/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   LocationLines = ReadFile(InputFile)


   Locations = [ParseLocation(LocationLine) for LocationLine in LocationLines]

   Locations = list(zip(range(len(Locations)), Locations))
     
   # for Location in Locations:
   #    print(Location)

   Grid = SpanGrid(Locations)
   Grid2 = Grid.copy()

   # print( list(Grid.items())[:100] )

   for CoordinateKey, NeighboursList in Grid.items():
      for Location in Locations:
         Distance = CalculateDistance(CoordinateKey, Location[1])
         Grid[CoordinateKey].append( ( Location[0],  Distance) )

   # for Coordinate in list(Grid.items())[:10]:
   #    print(Coordinate)

   for CoordinateKey, NeighboursList in Grid.items():
      DistanceToClosestNeighour = min(NeighboursList, key=lambda x: x[1])[1]

      ClosestNeighours = [ Neighbour for Neighbour in NeighboursList if Neighbour[1] == DistanceToClosestNeighour ]

      if len(ClosestNeighours) == 1:
         Grid[CoordinateKey] = ClosestNeighours[0]
      else:
         Grid[CoordinateKey] = ("", "")


   # for Coordinate in list(Grid.items()):
   #    # print(Coordinate)
   #    if Coordinate[1][1] == 0:
   #      print(Coordinate)

   LocationOccurences = [ Coordinate[1][0] for Coordinate in list(Grid.items()) if Coordinate[1][0] != ""]

   MostCommonLocation = most_common(LocationOccurences)

   Occurences = [ LocationOccurence for LocationOccurence in LocationOccurences if LocationOccurence == MostCommonLocation]
   NumberOfOccurences = len(Occurences)

   print("What is the size of the largest area that isn't infinite?")
   print(NumberOfOccurences)


   # print( Grid[(324, 346)] )

   for CoordinateKey, NeighboursList in Grid2.items():
      DistancesList = [ Neighbour[1] for Neighbour in NeighboursList]
      # print(NeighboursList)
      TotalDistanceSum = sum(DistancesList)
      # print(TotalDistanceSum)

      Grid2[CoordinateKey] = TotalDistanceSum

   CoordinatesInDenseZone = []

   for Coordinate in list(Grid2.items()):
      if Coordinate[1] < 10000:
         CoordinatesInDenseZone.append(Coordinate)


   print("What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?")
   print( len(CoordinatesInDenseZone) )

if __name__ == "__main__":
   main()
