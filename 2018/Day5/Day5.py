#!/usr/bin/env python3


FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day5/'
FileName = 'input.txt'
# FileName = 'input_test.txt'



def ConvertUnitToString(UnitTuple):
   Type = UnitTuple[0]
   Polarity = UnitTuple[1]

   if Polarity == 1:
      UnitString = Type.upper()
   elif Polarity == -1:
      UnitString = Type.lower()
   else:
      UnitString = '0'

   return(UnitString)

def ConvertUnitToTuple(UnitString):
   Type = UnitString.upper()
   if UnitString.isupper():
      Polarity = 1
   else:
      Polarity = -1
   return(Type, Polarity)


def ConvertPolymerToString(PolymerAsTuples):
   PolymerAsList = [ConvertUnitToString(Unit) for Unit in PolymerAsTuples]
   PolymerAsString = "".join(PolymerAsList)

   return(PolymerAsString)

def ConvertPolymerToTuples(PolymerAsString):
   PolymerAsList = list(PolymerAsString)
   PolymerAsTuples = [ ConvertUnitToTuple(Unit) for Unit in PolymerAsList ]

   return(PolymerAsTuples)

def UnitsReact(Unit1, Unit2):
   Type1 = Unit1[0]
   Polarity1 = Unit1[1]
   Type2 = Unit2[0]
   Polarity2 = Unit2[1]

   TypesReact = Type1 == Type2
   PolarituesReact = Polarity1 != Polarity2

   return(TypesReact and PolarituesReact)


def ReactPolymerOnce(Polymer):
   NumberOfUnits = len(Polymer)

   # print(ConvertPolymerToString(Polymer))

   for i in range(NumberOfUnits - 1):
      if UnitsReact( Polymer[i], Polymer[i + 1] ):
         Polymer[i] = ('0', 0)
         Polymer[i + 1] = ('0', 0)

   Polymer = [Unit for Unit in Polymer if Unit != ('0', 0)]
   
   return(Polymer)

def FullyReactPolymer(Polymer):

   PreviousNumberOfUnits = 0
   NumberOfUnits = len(Polymer)

   while NumberOfUnits != PreviousNumberOfUnits:

      Polymer = ReactPolymerOnce(Polymer)
      PreviousNumberOfUnits = NumberOfUnits
      NumberOfUnits = len(Polymer)

   return(Polymer)

def GetUniqueTypes(Polymer):
   PoylmerString = ConvertPolymerToString(Polymer)

   PolymerTypes = list(PoylmerString.upper())
   UniquePolymerTypes = list(set(PolymerTypes))
   UniquePolymerTypes.sort()

   return(UniquePolymerTypes)

def RemoveUnitType(Polymer, TypeToRemove):

   Polymer = [(Type, Polarity) for (Type, Polarity) in Polymer if Type != TypeToRemove]

   return(Polymer)

InputFile = FilePath + FileName

with open(InputFile,'r') as f:
   lines = f.read().splitlines()

PoylmerString = lines[0]

# PoylmerString = "dabAcCaCBAcCcaDA"


def main():

   OriginalPolymer = ConvertPolymerToTuples(PoylmerString)

   UniquePolymerTypes = GetUniqueTypes(OriginalPolymer)
   # print(UniquePolymerTypes)

   ReactedPolymer = FullyReactPolymer(OriginalPolymer)

   NumberOfUnits = len(ReactedPolymer)

   print("The number of units remaining after reacting:")
   print(NumberOfUnits)

   PolymerLengthPerType = []

   for PolymerType in UniquePolymerTypes:
      print("Removing units of type " + PolymerType)
      AlteredPolymer = RemoveUnitType(OriginalPolymer, PolymerType)
      # print(GetUniqueTypes(AlteredPolymer))
      AlteredPolymer = FullyReactPolymer(AlteredPolymer)
      NumberOfUnits = len(AlteredPolymer)
      PolymerLengthPerType.append((PolymerType, NumberOfUnits))
      print("Number of units remaining after removing type " + PolymerType + ": " + str(NumberOfUnits))

   print("The polymer length remaining for each type after removing: ")
   for PolymerLengthByType in PolymerLengthPerType:
      print(PolymerLengthByType)

   MinPolymerLengthByType = min(PolymerLengthPerType, key=lambda x: x[1])
   print("The shirtest polymer length remaining after removing a type: ")
   print(MinPolymerLengthByType[1])
   print("Achieved by removing the type: ")
   print(MinPolymerLengthByType[0])


   # print("The remaining polymer after reacting:")
   # print(ConvertPolymerToString(ReactedPolymer))


if __name__ == "__main__":
   main()
