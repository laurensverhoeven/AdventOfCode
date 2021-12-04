#!/usr/bin/env python3

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def main():

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day9/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   Lines = ReadFile(InputFile)

   return()

if __name__ == "__main__":
   main()
   