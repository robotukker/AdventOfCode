import numpy as np

def FuseDigits(digitList):
    return "".join(str(int(d)) for d in digitList)

    

if __name__ == "__main__":
        
    with open('Input3.txt', 'r') as file:
        batteryLines = file.read()

    lines = batteryLines.splitlines()
    sum = 0

    for line in lines:
        print(line)
        highDigits = np.zeros(12)
        i = -1

        for digit in line:
            i += 1
            i = 11 if i > 11 else i
            tempHighDigits = highDigits.copy()
            tempHighDigits[i] = digit
            if int(FuseDigits(highDigits)) < int(FuseDigits(tempHighDigits)):
                highDigits = tempHighDigits.copy()
                continue

        print(highDigits)
        fusedDigits = FuseDigits(highDigits)
        sum += int(fusedDigits)



    # print(sum)