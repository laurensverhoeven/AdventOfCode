#!/usr/bin/env python3


FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day4/'
FileName = 'input.txt'
# FileName = 'input_test.txt'

def Sort(List):
   List.sort()
   return(List)


def ParseGuardLine(GuardLine):
   DateTimeStart = GuardLine.find("[") + 1
   DateTimeEnd = GuardLine.find("]") 
   RemainderStart = DateTimeEnd + 2

   DateTime = GuardLine[DateTimeStart:DateTimeEnd]

   Event = GuardLine[RemainderStart:].strip()

   (Date, Time) = DateTime.split(" ")

   DateSplit = Date.split("-")
   TimeSplit = Time.split(":")

   Year = int(DateSplit[0])
   Month = int(DateSplit[1])
   Day = int(DateSplit[2])

   Hour = int(TimeSplit[0])
   Minute = int(TimeSplit[1])

   ParsedEvent = ParseEvent(Event)

   Result = ((Year, Month, Day), (Hour, Minute), ParsedEvent)

   return(Result)

def ParseEvent(EventLine):
   GuardID = -1
   if EventLine == "falls asleep":
      EventNum = 1
   elif EventLine == "wakes up":
      EventNum = 0
   else:
      EventSplit = EventLine.split(' ')
      GuardID = int(EventSplit[1][1:])
      EventNum = 2
      # print(EventSplit)
      # print(GuardID)

   return(EventNum, GuardID)


InputFile = FilePath + FileName

with open(InputFile,'r') as f:
   lines = f.read().splitlines()

GuardLines = lines
GuardLinesSorted = Sort(GuardLines)
GuardEvents = [ParseGuardLine(GuardLine) for GuardLine in GuardLines]

# for GuardEvent in GuardEvents:
#    print(GuardEvent)

# GuardSleepWakeTimes = [GuardEvent for GuardEvent in GuardEvents]

GuardSleepWakeTimes = []
for GuardEvent in GuardEvents:
   Date = GuardEvent[0]
   Time = GuardEvent[1]
   Event = GuardEvent[2]
   if Event[0] == 2:
      ActiveGuard = Event[1]
   else:
      # Event = (Event[0], ActiveGuard)
      Date
      ThisGuardSleepWakeTime = (Date, Time, (Event[0], ActiveGuard))
      GuardSleepWakeTimes.append(ThisGuardSleepWakeTime)


Guards = {}

GuardIDs = list(set([GuardEvent[2][1] for GuardEvent in GuardEvents if GuardEvent[2][1] != -1]))


for GuardID in GuardIDs:
   Guards[str(GuardID)] = 0

# print(Guards)



for GuardEvent in GuardSleepWakeTimes:
   Date = GuardEvent[0]
   Time = GuardEvent[1]
   Event = GuardEvent[2]

   ThisGuardID = Event[1]

   if Event[0] == 1:
      SleepTime = Time
   elif Event[0] == 0:
      if ThisGuardID != PreviousGuardID:
         raise Exception('Unexpected Guard Change')
      WakeTime = Time
      MinutesAsleep = WakeTime[1] - SleepTime[1]
      Guards[str(ThisGuardID)] += MinutesAsleep
   PreviousGuardID = ThisGuardID
   

# print(Guards)

GuardSleepMinutes = [(int(GuardID), TimeAsleep) for (GuardID, TimeAsleep) in Guards.items() ]

GuardSleepMinutes.sort(key=lambda x: x[1])

# print(GuardSleepMinutes)

GuardIDMostAsleep = GuardSleepMinutes[-1][0]



LazyGuardWakeTimes = [GuardSleepWakeTime for GuardSleepWakeTime in GuardSleepWakeTimes if GuardSleepWakeTime[2][1] == GuardIDMostAsleep]

AsleepPerMinute = [0 for minute in range(60)]


LazyGuardSleepTimes = []

for LazyGuardWakeTime in LazyGuardWakeTimes:
   Date = LazyGuardWakeTime[0]
   Time = LazyGuardWakeTime[1]
   Event = LazyGuardWakeTime[2]
   if Event[0] == 1:
      GuardAsleep = True
      SleptInTime = Time
   if Event[0] == 0:
      GuardAsleep = False
      WokeUpTime = Time
      MinutesAsleep = range(SleptInTime[1], WokeUpTime[1])
      for i in MinutesAsleep:
         AsleepPerMinute[i] += 1
      # print(MinutesAsleep)
   # print(LazyGuardWakeTime)

# print(AsleepPerMinute)
# print(max(AsleepPerMinute))

# print([Minute for Minute in AsleepPerMinute if Minute == max(AsleepPerMinute)])

BestMinuteOfLazyGuard = AsleepPerMinute.index(max(AsleepPerMinute))





print("The ID of the Guard that is asleep the most: ")
print(GuardIDMostAsleep)

print("The minute the lazy guard is asleep most often: ")
print(BestMinuteOfLazyGuard)

print("The product of these two: ")
print( GuardIDMostAsleep * BestMinuteOfLazyGuard )


# def DetermineActiveGuard(GuardEvent):

#    Date = GuardEvent[0]
#    Time = GuardEvent[1]
#    Event = GuardEvent[2]

#    return(GuardEvent)




BestMinutePerGuard = []
for GuardID in GuardIDs:
   
   GuardWakeTimes = [GuardSleepWakeTime for GuardSleepWakeTime in GuardSleepWakeTimes if GuardSleepWakeTime[2][1] == GuardID]

   AsleepPerMinute = [0 for minute in range(60)]


   LazyGuardSleepTimes = []

   for LazyGuardWakeTime in GuardWakeTimes:
      Date = LazyGuardWakeTime[0]
      Time = LazyGuardWakeTime[1]
      Event = LazyGuardWakeTime[2]
      if Event[0] == 1:
         GuardAsleep = True
         SleptInTime = Time
      if Event[0] == 0:
         GuardAsleep = False
         WokeUpTime = Time
         MinutesAsleep = range(SleptInTime[1], WokeUpTime[1])
         for i in MinutesAsleep:
            AsleepPerMinute[i] += 1
         # print(MinutesAsleep)
      # print(LazyGuardWakeTime)

   # print(AsleepPerMinute)
   # print(max(AsleepPerMinute))

   # print([Minute for Minute in AsleepPerMinute if Minute == max(AsleepPerMinute)])

   BestMinute = AsleepPerMinute.index(max(AsleepPerMinute))
   BestMinutePerGuard.append( (GuardID, BestMinute, max(AsleepPerMinute)) )


(GuardIDMostPredictable, BestMinute, TimesAsleep) = max(BestMinutePerGuard, key=lambda x: x[2])


print("\nThe ID of the Guard that is asleep the most at any certain minute: ")
print(GuardIDMostPredictable)

print("The minute the lazy guard is asleep most often: ")
print(BestMinute)

print("The product of these two: ")
print( GuardIDMostPredictable * BestMinute )
