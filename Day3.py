import numpy as np
from collections import deque


def FuseDigits(digitList):
    return "".join(str(int(d)) for d in digitList)

def PopDigit(highDigits, skip, k):
    for i in range(k):
        skip += 1
        highDigits.pop()

    return highDigits,skip

        
if __name__ == "__main__":
    # Handle input
    with open('Input3.txt', 'r') as file:
        batteryLines = file.read()
    lines = batteryLines.splitlines()
    sum = 0


    for line in lines:
        #initialization
        lineQueue = deque()
        for digit in line:
            lineQueue.append(digit)
        diff = len(lineQueue)-12

        highDigits = [0]
        skip = -1            # to handle initialization zero in highDigits vector

        while len(lineQueue) > 0:
            digitUsed = False

            # Search where digit should be placed
            for i in range(diff,0,-1):
                if skip < diff-(i-1) and len(highDigits) > i-1 and int(lineQueue[0]) > int(highDigits[-i]):
                    highDigits,skip = PopDigit(highDigits,skip,i)

                    highDigits.append(lineQueue[0])
                    lineQueue.popleft()

                    digitUsed = True 
                    break
            # if no suitable loc. is found inside vector, append to end
            if not digitUsed:
                highDigits.append(lineQueue[0])
                lineQueue.popleft()

        # Grab first 12
        highDigits = highDigits[:12]

            
        fusedDigits = FuseDigits(highDigits)
        sum += int(fusedDigits)

    print(sum)