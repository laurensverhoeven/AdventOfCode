#!/usr/bin/env python3

from pprint import pformat, pprint
import math

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def CalculateRequiredFuel(DeviceMass):

   Fuel = math.floor(DeviceMass / 3) - 2

   return(Fuel)

def main():

   FilePath = './'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   Lines = ReadFile(InputFile)

   ModuleMasses = [int(Line) for Line in Lines]

   FuelPerModule = [CalculateRequiredFuel(Module) for Module in ModuleMasses]
   TotalFuel = sum(FuelPerModule)

   print("The amount of fuel required per module is:\n" + pformat(FuelPerModule))
   print("The TOTAL amount of fuel required is: " + pformat(TotalFuel))


   return()

if __name__ == "__main__":
   main()
   