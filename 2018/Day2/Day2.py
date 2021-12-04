#!/usr/bin/env python3


FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day2/'
FileName = 'input.txt'
InputFile = FilePath + FileName

with open(InputFile,'r') as f:
   lines = f.read().splitlines()

ProductIDs = lines

DoubleLetterIDs = []
TripleLetterIDs = []

for ProductID in ProductIDs:
   print(ProductID)
   # print(set(ProductID))
   IDHasDoubleCharaters = False
   IDHasTripleCharaters = False
   for character in set(ProductID):
      CharCount = ProductID.count(character)
      if CharCount == 2:
         print("Character " + character +" occurs " + str(CharCount) + " times")
         IDHasDoubleCharaters = True
      if CharCount == 3:
         print("Character " + character +" occurs " + str(CharCount) + " times")
         IDHasTripleCharaters = True
   if IDHasDoubleCharaters:
      DoubleLetterIDs.append(ProductID)
   if IDHasTripleCharaters:
      TripleLetterIDs.append(ProductID)  


print("\nIDs with double characters:")
for ID in DoubleLetterIDs:
   print(ID)

print("\nIDs with triple characters:")
for ID in TripleLetterIDs:
   print(ID)

Checksum = len(DoubleLetterIDs) * len(TripleLetterIDs)
print("The checksum is: ")
print(Checksum)


def CalcEqualPositions(ID1, ID2):

   IDPositionsEqual = [pos1 == pos2 for pos1, pos2 in zip(ID1, ID2)] 
     
   return(IDPositionsEqual)

IDsThatAreSimilar = []

NumberOfProductIDs = len(ProductIDs)
for i in range(NumberOfProductIDs):
   ID1 = ProductIDs[i]
   ID1Length = len(ID1)
   for j in range(i, NumberOfProductIDs):
      ID2 = ProductIDs[j]
      Similarity = CalcEqualPositions(ID1, ID2)
      IdenticalCharacters = sum(Similarity)
      if IdenticalCharacters == ID1Length - 1:
         IDsThatAreSimilar.append(ID1)
         IDsThatAreSimilar.append(ID2)

for ID in IDsThatAreSimilar:
   print(ID)

print(CalcEqualPositions(IDsThatAreSimilar[0], IDsThatAreSimilar[1]))

