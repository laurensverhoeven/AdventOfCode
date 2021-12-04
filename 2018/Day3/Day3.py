#!/usr/bin/env python3


FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day3/'
FileName = 'input.txt'
# FileName = 'input_test.txt'
InputFile = FilePath + FileName

with open(InputFile,'r') as f:
   lines = f.read().splitlines()

ClaimLines = lines

Claims = []

for ClaimLine in ClaimLines:
   StartID = ClaimLine.find("#")
   StartXPos = ClaimLine.find("@")
   StartYPos = ClaimLine.find(",")
   StartXSize = ClaimLine.find(":")
   StartYSize = ClaimLine.find("x")
   # BeforeID = ClaimLine.split("#")

   ID = int(ClaimLine[StartID + 1:StartXPos].strip())
   XPos = int(ClaimLine[StartXPos + 1:StartYPos].strip())
   YPos = int(ClaimLine[StartYPos + 1:StartXSize].strip())
   XSize = int(ClaimLine[StartXSize + 1:StartYSize].strip())
   YSize = int(ClaimLine[StartYSize + 1:].strip())

   # print("")
   # print(ID)
   # print(XPos)
   # print(YPos)
   # print(XSize)
   # print(YSize)

   # print()
   Claims.append((
      ID,
      (XPos, XSize),
      (YPos, YSize),
   ))
   # print("Hoi")


XMaxima = []
YMaxima = []

for Claim in Claims:
   XMax = sum(Claim[1])
   YMax = sum(Claim[2])
   XMaxima.append(XMax)
   YMaxima.append(YMax)
   # print(Claim)
   # print(XMax)
   # print(YMax)

FabricXSize = max(XMaxima)
FabricYSize = max(YMaxima)


# FabricXSize = 3
# FabricYSize = 10
Fabric = [[0 for x in range(FabricXSize)] for y in range(FabricYSize)] 
FabricByID = [[ [] for x in range(FabricXSize)] for y in range(FabricYSize)] 


def SetFabricPos(Positions, Value):
   XPos = Positions[0]
   YPos = Positions[1]
   Fabric[YPos][XPos] = Value

def ClaimFabricPos(Positions, ID):
   XPos = Positions[0]
   YPos = Positions[1]
   # if Fabric[YPos][XPos] == 0:
   #    Fabric[YPos][XPos] = 1
   Fabric[YPos][XPos] += 1
   FabricByID[YPos][XPos].append(ID)

# # print(Fabric)
# ClaimFabricPos(1, 9)
# for i in Fabric:
#    print(i)



for Claim in Claims:
   ID = Claim[0]
   XMin = Claim[1][0]
   YMin = Claim[2][0]
   XMax = sum(Claim[1])
   YMax = sum(Claim[2])

   XRange = range(XMin, XMax)
   YRange = range(YMin, YMax)

   for x in XRange:
      for y in YRange:
         ClaimFabricPos((x, y), ID)


# for i in Fabric:
#    print(i)

def CountDuplicateClaims(ClaimNumber):
   if ClaimNumber > 1:
      return 1
   elif ClaimNumber == 1:
      return 0
   else:
      return ClaimNumber

DoublyClaimedFabric = [[CountDuplicateClaims(XPos) for XPos in XPosList] for XPosList in Fabric]

print("The number of doubly claimed square inches is: ")
print(sum([sum(PosList) for PosList in DoublyClaimedFabric]))


# for i in FabricByID:
#    print(i)

# FabricNotDoublyClaimedByID = [ IDList[0] for IDList in FabricByID if len(IDList) == 1]
FabricDoublyClaimedByID = [[IDList for IDList in XPosList if len(IDList) > 1] for XPosList in FabricByID]

IDsWithDuplicateClaims = []
for i in FabricDoublyClaimedByID:
   for j in i:
      for k in j:
         IDsWithDuplicateClaims.append(k)

IDsWithDuplicateClaims = set(IDsWithDuplicateClaims)

IDs = set([Claim[0] for Claim in Claims])

# print(IDs)
# print(IDsWithDuplicateClaims)

IDsWithoutDuplicateClaims = set(IDs)^set(IDsWithDuplicateClaims)

print("The IDs without duplicate claims are: ")
print(next(iter(IDsWithoutDuplicateClaims)) )




# for i in FabricDoublyClaimdByID:
#    print(i)
