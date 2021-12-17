# A tool for parsing the inner workings of Josh Slycord's mind
# Import needed packages
import argparse
import csv
from parser import *

parser = argparse.ArgumentParser(description="Gimmie Those R/W Counts")

parser.add_argument('--path', help="Desired output file", required=True)
parser.add_argument('--type', help="What you're looking for", required=False)
parser.add_argument('--inst', help="Instruction to count", required=False)
parser.add_argument('--outName', help="Output File Name", required=False)

args=parser.parse_args()

outputFile = open(args.path, 'r')

lines = outputFile.readlines()

if args.type == "inst":
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
if args.type == "top":
    nameList = []
    cycleList = []
    simTimeList = []
    
    # Append Row Labels
    nameList.append("Acc Name")
    cycleList.append("Cycles")
    simTimeList.append("Simulation Time (s)")

    for index, line in enumerate(lines):
        if "top.llvm_interface" in line:
            for accLine in lines[index:]:
                if "Simulation Time (Total):" in accLine:
                    accLine = (accLine.replace("Simulation Time (Total):",'')).replace(' ', '')
                    accLine = accLine.replace('ms', ' ').replace('s', ' ').replace('m', ' ').replace('h', ' ')
                    accLine = accLine.split(' ')
                    
                    timeTotal = 0.0
                    
                    timeTotal += float(accLine[0])*3600
                    timeTotal += float(accLine[1])*60
                    timeTotal += float(accLine[2])
                    timeTotal += float(accLine[3])/1000
                    
                    simTimeList.append(timeTotal)
                elif "Runtime" in accLine:
                    nameList.append(line)
                    cycleList.append([int(num) for num in accLine.split() if num.isdigit()][0])
                    break
    with open(args.outName, 'w') as f:
        write = csv.writer(f)
        write.writerow(nameList)
        write.writerow(simTimeList)
        write.writerow(cycleList)
    print("All done")