import numpy as np
from collections import deque


def FuseDigits(digitList):
    return "".join(str(int(d)) for d in digitList)

        

if __name__ == "__main__":
        
    with open('Input3.txt', 'r') as file:
        batteryLines = file.read()

    lines = batteryLines.splitlines()
    sum = 0

    for line in lines:
        tempLine = line.copy()

        for idx in range(15):
            newLine[0] = 


        fusedDigits = FuseDigits(line)


        print(fusedDigits)


        # sum += int(fusedDigits)



    # print(sum)