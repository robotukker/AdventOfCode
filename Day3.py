import numpy as np
from collections import deque


def FuseDigits(digitList):
    return "".join(str(int(d)) for d in digitList)

def PopDigit(highDigits, skip, k):
    for i in range(k):
        if highDigits[-i] != 0:
            skip += 1
        highDigits.pop()

    return highDigits,skip

        

if __name__ == "__main__":
        
    with open('Input3.txt', 'r') as file:
        batteryLines = file.read()

    lines = batteryLines.splitlines()
    sum = 0

    for line in lines:
        print(line)
        lineQueue = deque()
        highDigits = [0]
        skip = 0

        for digit in line:
            lineQueue.append(digit)

        diff = len(lineQueue)-12
        print(diff)

        while len(lineQueue) > 0:
            if skip < diff-2 and len(highDigits) > 2 and int(lineQueue[0]) > int(highDigits[-3]):
                highDigits,skip = PopDigit(highDigits,skip,3)

                highDigits.append(lineQueue[0])
                lineQueue.popleft()

            elif skip < diff-1 and len(highDigits) > 2 and int(lineQueue[0]) > int(highDigits[-2]):
                highDigits,skip = PopDigit(highDigits,skip,2)

                highDigits.append(lineQueue[0])
                lineQueue.popleft()

            elif skip < diff and int(lineQueue[0]) > int(highDigits[-1]):
                highDigits,skip = PopDigit(highDigits,skip,1)
            
                highDigits.append(lineQueue[0])
                lineQueue.popleft()
                
            else:
                highDigits.append(lineQueue[0])
                lineQueue.popleft()

        highDigits = highDigits[:12]
        print(highDigits)
            
        fusedDigits = FuseDigits(highDigits)
        sum += int(fusedDigits)



    print(sum)