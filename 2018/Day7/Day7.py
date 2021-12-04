#!/usr/bin/env python3

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def ParseStep(StepLine):

   def FindAfter(String, Substring):
      IndexAfter = String.find(Substring) + len(Substring)
      return(IndexAfter)

   DependencyStepIndex = FindAfter(StepLine, "Step ")
   DependentStepIndex = FindAfter(StepLine, " must be finished before step ")

   DependencyStep = StepLine[DependencyStepIndex]
   DependentStep = StepLine[DependentStepIndex]

   return(DependencyStep, DependentStep)

def GetReadySteps(Dependencies):

   Steps = [Step for Step, DependencyStep in Dependencies.items() if len(DependencyStep) == 0]

   return(Steps)

def GetNextStep(Dependencies):

   ReadySteps = GetReadySteps(Dependencies)
   ReadySteps.sort()

   return(ReadySteps[0])

def main():

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day7/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   StepLines = ReadFile(InputFile)

   DependencyPairs = []

   for StepLine in StepLines:
      DependencyStep, DependentStep = ParseStep(StepLine)
      DependencyPairs.append((DependencyStep, DependentStep))
      # print(DependencyStep, DependentStep)

   UniqueDependentSteps = list(set([ DependentStep for DependencyStep, DependentStep in DependencyPairs]))
   UniqueDependencySteps = list(set([ DependencyStep for DependencyStep, DependentStep in DependencyPairs]))

   UniqueSteps = list(set(UniqueDependentSteps + UniqueDependencySteps))
   UniqueSteps.sort()

   # print( UniqueSteps )

   Dependencies = { Step: [] for Step in UniqueSteps }

   for DependencyStep, DependentStep in DependencyPairs:
      Dependencies[DependentStep].append(DependencyStep)
      

   # for Step, DependencyStep in Dependencies.items():
   #    print(Step, DependencyStep)

   Steps = []
   while len(Steps) < len(UniqueSteps):
      NextStep = GetNextStep(Dependencies)
      Steps.append(NextStep)
      del Dependencies[NextStep]
      for DependentStep in Dependencies:
         if NextStep in Dependencies[DependentStep]:
            Dependencies[DependentStep].remove(NextStep)



   print("In what order should the steps in your instructions be completed?")
   print( "".join(Steps) )

   # for DependencyStep, DependentStep in DependencyPairs:
   #    print(DependencyStep, DependentStep)



   NumberOfWorkers = 5
   OffsetTime = 60

   Dependencies2 = { Step: [] for Step in UniqueSteps }

   for DependencyStep, DependentStep in DependencyPairs:
      Dependencies2[DependentStep].append(DependencyStep)
   
   
   def RemoveCompletedDependencies(Step, Dependencies2):
      for DependentStep in Dependencies2:
         if Step in Dependencies2[DependentStep]:
            Dependencies2[DependentStep].remove(Step)

      return(Dependencies2)

   def GetDurationOfStep(NextStep):
      Unicode = ord(NextStep)
      AdditionalTime = Unicode - 64
      # print(NextStep, AdditionalTime)
      Duration = OffsetTime + AdditionalTime
      return(Duration)

   GetDurationOfStep(NextStep)

   StepsCompleted = []
   # StepsReadyForPickup = []
   t = 0
   StepsInProgress = {}
   while len(StepsCompleted) < len(UniqueSteps) and t < 10000:

      print("Time is: ", t)

      StepsJustCompleted = []
      for Step in StepsInProgress:
         if StepsInProgress[Step] == t:
            print("Just completed step: ", NextStep)
            StepsJustCompleted.append(Step)
      
      for Step in StepsJustCompleted:
         StepsCompleted.append(Step)
         del StepsInProgress[Step]
         Dependencies2 = RemoveCompletedDependencies(Step, Dependencies2)

      StepsReadyForPickup = GetReadySteps(Dependencies2)
      StepsReadyForPickup.sort()
      print("Ready for pickup: ", StepsReadyForPickup)
      
      for NextStep in StepsReadyForPickup:
         if len(StepsInProgress) < NumberOfWorkers:
            print("Picking up step: ", NextStep)
            StepDuration = GetDurationOfStep(NextStep)
            StepCompletionTime = t + StepDuration
            StepsInProgress[NextStep] = StepCompletionTime
            del Dependencies2[NextStep]

   
      for Step in StepsInProgress:
         print("In progress: ", Step, StepsInProgress[Step])

      print("Completed: ", StepsCompleted, "\n")

      t += 1

   TimeToCompletion = t -1

   print("With " + str(NumberOfWorkers) + " workers and the " + str(OffsetTime) + "+ second step durations described above, how long will it take to complete all of the steps?")
   print( str(TimeToCompletion) + " seconds" )

   print("The steps were executed in this order:")
   print( "".join(StepsCompleted) )

   return()

if __name__ == "__main__":
   main()