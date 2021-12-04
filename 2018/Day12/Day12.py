#!/usr/bin/env python3

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def WriteFile(FilePath, Lines):

   with open(FilePath,'w') as f:
      f.write("\n".join(Lines))

   return()

def ParsePots(Line):

   def ParsePots(Pot):
      if Pot == "#":
         Pot = 1
      elif Pot == ".":
         Pot = 0
      else:
         print("Character: " + Pot + " not expected")
         raise Exception('Unexpected character')
      return(Pot)

   Pots = [ ParsePots(Pot) for Pot in list(Line) ]

   return(Pots)

def ParseRule(Line):
   Condition, Result = Line.split(" => ")
   Condition = tuple(ParsePots(Condition))
   Result = ParsePots(Result)[0]
   return(Condition, Result)

def SpreadOnce(InitalPots, RuleDict):
   ResultingPots = [0, 0] + InitalPots + [0, 0]
   InitalPots = [0, 0, 0, 0] + InitalPots + [0, 0, 0, 0]

   # print(RuleDict)

   # print(InitalPots)

   for CurrentPotIndex in range(0, len(ResultingPots)):
      Pots = tuple(InitalPots[CurrentPotIndex : CurrentPotIndex + 5])
      # print(CurrentPotIndex)
      # print(Pots)
      if Pots in RuleDict:
         CurrentPotResult =  RuleDict[ Pots ]
      else: 
         CurrentPotResult = 0
      ResultingPots[CurrentPotIndex] = CurrentPotResult

   return(ResultingPots)

def PotsToString(Pots):

   def PotToString(Pot):
      if Pot == 1:
         Pot = "#"
      elif Pot == 0:
         Pot = "."
      else:
         print("Value: " + str(Pot) + " not expected")
         raise Exception('Unexpected Value')
      return(Pot)

   Pots = "".join( [ PotToString(Pot) for Pot in Pots ] )

   return(Pots)

def main():

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day12/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   FileName = 'Output.txt'
   OutputFile = FilePath + FileName

   Lines = ReadFile(InputFile)

   InitalState = Lines[0].split("initial state: ")[1]

   Rules = Lines[2:]

   Rules = [ ParseRule(Rule) for Rule in Rules ]
   RuleDict = { Condition: Result for Condition, Result in Rules }

   InitialPots = ParsePots(InitalState)


   # print(InitalState)
   # for Pot in InitialPots:
   #    print(Pot)
   # for Rule in RuleDict:
   #    print(Rule, RuleDict[Rule])


   CurrentPots = InitialPots
   NumberOfGenerataions = 20
   NumberOfGenerataions = 101
   # print(CurrentPots)


   # InitialPotCount = len(InitialPots)
   # FinalPotCount = InitialPotCount + NumberOfGenerataions * 4

   InitalZeroLocation = 0
   FinalZeroLocation = InitalZeroLocation + NumberOfGenerataions * 2

   AllGenerations = set()

   PotsPerGeneration = []

   Output = []
   Output.append(PotsToString(InitialPots))

   

   PotNumbers = "Pot" + ' ' * ( NumberOfGenerataions * 2) + "".join( [str(Num).rjust(5, "0")[-3] for Num in range( len(InitialPots) + NumberOfGenerataions * 2 )] )
   Output.append(PotNumbers)
   PotNumbers = "Pot" + ' ' * ( NumberOfGenerataions * 2) + "".join( [str(Num).rjust(5, "0")[-2] for Num in range( len(InitialPots) + NumberOfGenerataions * 2 )] )
   Output.append(PotNumbers)
   PotNumbers = "Pot" + ' ' * ( NumberOfGenerataions * 2) + "".join( [str(Num).rjust(5, "0")[-1] for Num in range( len(InitialPots) + NumberOfGenerataions * 2 )] )
   Output.append(PotNumbers)

   for Generation in range(NumberOfGenerataions):
      PotPadding = '.' * ( (NumberOfGenerataions - Generation) * 2)
      OutputLine = str(Generation).rjust(3) + PotPadding + PotsToString(CurrentPots) + PotPadding
      Output.append(OutputLine)
      # print( PotPadding + PotsToString(CurrentPots) + PotPadding)
      CurrentPots = SpreadOnce(CurrentPots, RuleDict)
      # CurrentPots = [int(Pot) for Pot in list( "".join([str(Pot) for Pot in CurrentPots]).strip("0") ) ]
      PotsPerGeneration.append((Generation, CurrentPots))
      # if tuple(CurrentPots) in AllGenerations:
      #    print("Repetition happended in generation " + str(Generation) )
      #    FirstRepeatedSet = CurrentPots
      # else:
      #    AllGenerations.add(tuple(CurrentPots))

      # # ZeroLocation = InitalZeroLocation + Generation * 2

      # print(CurrentPots)
      
      # print( [int(Pot) for Pot in list( "".join([str(Pot) for Pot in CurrentPots]).strip("0") ) ] )
      
   # print( PotsToString(CurrentPots))

   # print(Output )
   WriteFile(OutputFile, Output)

   # for Generation, PotsOfGeneration in PotsPerGeneration:
   #    print( str(Generation).rjust(3), PotsToString(PotsOfGeneration))
   #    # if PotsOfGeneration == FirstRepeatedSet:
   #    #    print( Generation, PotsToString(PotsOfGeneration))

   # # for i in range(len(CurrentPots)):
   # #    print(i - FinalZeroLocation, CurrentPots[i])

   PotsWithPlant = [ i - FinalZeroLocation for i in range(len(CurrentPots)) if CurrentPots[i]] 
   print("The numbers of the pots that have a plant: ")
   print(PotsWithPlant)

   print("After " + str(NumberOfGenerataions) + " generations, what is the sum of the numbers of all pots which contain a plant?", sum(PotsWithPlant))
   # print(sum(PotsWithPlant))

   # for n in range(100, 120):
   #    PlantNumber = 3081 + 57 * (n - 11)
   #    print("After " + str(n) + " generations, what is the sum of the numbers of all pots which contain a plant?", PlantNumber)

   return()

if __name__ == "__main__":
   main()
   