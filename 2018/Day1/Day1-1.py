#!/usr/bin/env python3


FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day1/'
FileName = 'InputChanges'
InputFile = FilePath + FileName

with open(InputFile,'r') as f:
   lines = f.read().splitlines()

FrequencyChanges = []

for line in lines:
   # print(line)
   # print(type(line))

   if line[0] == '-':
      # print("Negative")
      # print(int(line[1:]))
      ThisFrequency = -1 * int(line[1:])
      # print(ThisFrequency)
      FrequencyChanges.append(ThisFrequency)
   elif line[0] == '+':
      # print("Positive")
      ThisFrequency = +1 * int(line[1:])
      FrequencyChanges.append(ThisFrequency)
   else:
      print(line)
      raise Exception('Unexpected character')


# print("Frequency changes:")
# for FrequencyChange in FrequencyChanges:
#    print(FrequencyChange)


TotalFrequencyChange = sum(FrequencyChanges)
print("Total frequency change is:")
print(TotalFrequencyChange)

IntermediateFrequencies = [0]

for FrequencyChange in FrequencyChanges:
   ThisFrequency = IntermediateFrequencies[-1] + FrequencyChange
   IntermediateFrequencies.append(ThisFrequency)


DuplicateFound = False

UniqueFrequencies = [0]
LastFrequency = 0
while not DuplicateFound:
   for FrequencyChange in FrequencyChanges:
      ThisFrequency = LastFrequency + FrequencyChange
      LastFrequency = ThisFrequency
      # print(IntermediateFrequency)
      if ThisFrequency in UniqueFrequencies:
         print("The first duplicate frequency is:")
         print(ThisFrequency)
         DuplicateFound = True
         break
      else:
         UniqueFrequencies.append(ThisFrequency)

# print(UniqueFrequencies)

# print(len(UniqueFrequencies))
# print(len(set(UniqueFrequencies)))

# for i in range(len(IntermediateFrequencies)):
#    # print(IntermediateFrequencies[i])
#    if IntermediateFrequencies[i] in IntermediateFrequencies[0:i-1] and i > 0:
#       print("This frequency occurs multiple times:")
#       print(IntermediateFrequencies[i])


