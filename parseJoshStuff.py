# A tool for parsing the inner workings of Josh Slycord's mind
# Import needed packages
import argparse
from parser import *

parser = argparse.ArgumentParser(description="Gimmie Those R/W Counts")

parser.add_argument('--path', help="Desired output file", required=True)
parser.add_argument('--inst', help="Instruction to count", required=True)

args=parser.parse_args()

outputFile = open(args.path, 'r')

lines = outputFile.readlines()

wantedInst = "Instruction: " + args.inst + "\n"

totalCount = 0
accIgnoreList = ["top"]
ignoring = False

for index, line in enumerate(lines):
    if "system." in line:
        for acc in accIgnoreList:
            if acc in line:
                ignoring = True
            else:
                ignoring = False
    if not ignoring:
        if args.inst in line:
            if wantedInst == line:
                totalCount += [int(num) for num in lines[index+3].split() if num.isdigit()][0]
print("Total Count of " + args.inst + ": " + str(totalCount))