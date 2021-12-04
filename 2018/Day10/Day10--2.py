#!/usr/bin/env python3

import re

from PIL import Image
# import Image

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def WriteFile(FilePath, Lines):

   with open(FilePath,'w') as f:
      f.write("\n".join(Lines))

   return()

def ParsePointLine(Line):

   # position=< 9,  1> velocity=< 0,  2>

   pattern = re.compile(r"""position\=
                             \<(?P<position>.*?)\>
                             .*?
                             \<(?P<velocity>.*?)\>""", re.VERBOSE)


   match = pattern.match(Line)

   Position = match.group("position").split(", ")
   Velocity = match.group("velocity").split(", ")

   Position = tuple( [ int(PositionPart) for PositionPart in Position] )
   Velocity = tuple( [ int(VelocityPart) for VelocityPart in Velocity] )

   # XPosition, YPosition = Position
   # XVelocity, YVelocity = Velocity

   # print(XPosition, YPosition, XVelocity, YVelocity)

   # PositionStartIndex = Line.find("position=<")
   # VelocityStartIndex = Line.find("> velocity=< ")

   # PositionPart = Line.split(" velocity")[0]
   # VelocityPart = Line.split(" velocity")[0]

   Point = (Position, Velocity)

   return(Point)

def GetPointPosition(Point, Time):
   Position, Velocity = Point
   Displacement = [ VelocityComponent * Time for VelocityComponent in Velocity]

   PointPosition = tuple([ Position[i] + Displacement[i] for i in range(len(Position))])


   return(PointPosition)

def SpanGrid(Locations):

   SmallestX = min(Locations, key=lambda x: x[0])[0]
   SmallestY = min(Locations, key=lambda x: x[1])[1]
   LargestX = max(Locations, key=lambda x: x[0])[0]
   LargestY = max(Locations, key=lambda x: x[1])[1]

   GridEdges = ( (SmallestX, SmallestY), (LargestX, LargestY) )

   # XRange = range(SmallestX, LargestX + 1)
   # YRange = range(SmallestY, LargestY + 1)

   # CoordinateList = [ (x, y) for y in YRange for x in XRange ]

   # # # print(CoordinateList[0: 100])

   # # for x in XRange:
   # #    for y in YRange:
   # #       (x, y)

   # Grid = {Coordinate: [] for Coordinate in CoordinateList }
   return(GridEdges)

def ScalePoints(PointPositions, ScaleFactor):
   ScaledPointPositions = [ tuple([ int(Position[i] * ScaleFactor) for i in range(len(Position))]) for Position in PointPositions]
   return(ScaledPointPositions)

def ShiftPositions(PointPositions):
   GridEdges = SpanGrid(PointPositions)
   SmallestX, SmallestY= GridEdges[0]
   PointPositions = [ ( PosX - SmallestX, PosY - SmallestY ) for (PosX, PosY) in PointPositions ]
   return(PointPositions)

def GetDrawing(RoundedPointPositions):
   RoundedGridEdges = SpanGrid(RoundedPointPositions)
   LargestX, LargestY= RoundedGridEdges[1]

   DisplayStrings = []
   for y in range(LargestY + 1):
      DisplayString = ""
      for x in range(LargestX + 1):
         # print((x, y))
         if (x, y) in RoundedPointPositions:
            DisplayString += "#"
         else:
            DisplayString += " "
      DisplayStrings.append(DisplayString)

   return(DisplayStrings)

def GetImage(RoundedPointPositions):
   RoundedGridEdges = SpanGrid(RoundedPointPositions)
   LargestX, LargestY= RoundedGridEdges[1]

   Image = []
   for y in range(-1, LargestY + 2):
      for x in range(-1, LargestX + 2):
         # print((x, y))
         if (x, y) in RoundedPointPositions:
            Image.append(256)
         else:
            Image.append(0)

   return(Image)

def CalculateAndDraw(Points, Time, ScaleFactor):
   PointPositions = [ GetPointPosition(Point, Time) for Point in Points ]
   PointPositions = ShiftPositions(PointPositions)
   RoundedPointPositions = ScalePoints(PointPositions, ScaleFactor)
   GridEdges = SpanGrid(RoundedPointPositions)
   # for Point in RoundedPointPositions:
   #    print(Point)
   # DisplayStrings = GetDrawing(RoundedPointPositions)
   Image = GetImage(RoundedPointPositions)

   return(Image, GridEdges)


def CreateImage(Points, Time, ScaleFactor, FilePath):
   PointPositions = [ GetPointPosition(Point, Time) for Point in Points ]
   PointPositions = ShiftPositions(PointPositions)
   PointPositions = ScalePoints(PointPositions, ScaleFactor)
   ((SmallestX, SmallestY), (LargestX, LargestY)) = SpanGrid(PointPositions)
   width = LargestX - SmallestX + 1
   height = LargestY - SmallestY + 1
   NumberOfPixels = width * height
   WhitePixels = [ x + y * width for (x, y) in PointPositions ]
   AllPixels = [0 for i in range(NumberOfPixels)]
   for WhitePixel in WhitePixels:
      AllPixels[WhitePixel] = 256
   
   Ratio = 50
   Size = (width * Ratio, height * Ratio)
   img = Image.new('L', (width, height))
   # list_of_pixels = list(img.getdata())
   # print(list_of_pixels[0:1001])
   img.putdata(AllPixels)
   img = img.resize(Size)
   Name = "Image_t=" + str(Time).rjust(4, '0')
   TargetFilePath = FilePath + Name + ".png"
   img.save(TargetFilePath)

   return(NumberOfPixels)

def main():

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day10/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   PointLines = ReadFile(InputFile)
   
   Points = [ ParsePointLine(PointLine) for PointLine in PointLines]

   StartTime = 10140
   StopTime = 10150
   # ScaleFactor = 0.001
   ScaleFactor = 1

   PixelCountPerTime = []
   for Time in range(StartTime, StopTime):
      NumberOfPixels = CreateImage(Points, Time, ScaleFactor, FilePath)
      print("The image at t = " + str(Time).rjust(4, "0") + " has " + str(NumberOfPixels) + " Pixels")
      PixelCountPerTime.append((Time, NumberOfPixels))

   # for Time, NumberOfPixels in PixelCountPerTime:
   #    print("The image at t = " + str(Time).rjust(4, "0") + " has " + str(NumberOfPixels) + " Pixels")

   MinimumPixelsInfo, MinimumNumberOfPixels = min(PixelCountPerTime, key=lambda x: x[1])

   print("The " + str(MinimumPixelsInfo) + " has the minimum number of pixel, with a number of " + str(MinimumNumberOfPixels) + " Pixels")
   
   return()

if __name__ == "__main__":
   main()
   