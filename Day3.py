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

        skip = 0

        for idx, digit in enumerate(line):
            k = min(idx, 11)

            if k-2 >= 0 and int(digit) > int(highDigits[k-2]): 
                highDigits[k-2] = digit
                highDigits[k-1] = 0 

            elif k-1 >= 0  and int(digit) > int(highDigits[k-1]):
                highDigits[k-1] = digit
                highDigits[k] = 0 

            elif skip < 3 and int(digit) > int(highDigits[k]):
                highDigits[k] = digit
            
            else:
                skip += 1


        print(highDigits)
            
                


        fusedDigits = FuseDigits(highDigits)
        sum += int(fusedDigits)



    # print(sum)