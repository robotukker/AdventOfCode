if __name__ == "__main__":
        
    with open('Input3.txt', 'r') as file:
        batteryLines = file.read()

    lines = batteryLines.splitlines()
    sum = 0

    for line in lines:
        firstDigit, secondDigit = [0,0]
        i = -1
        for digit in line:
            i += 1
            if firstDigit == 0:
                firstDigit = digit
                continue
            elif digit > firstDigit and not i == len(line)-1:
                firstDigit = digit
                secondDigit = 0
                continue
            

            if secondDigit == 0:
                secondDigit = digit
            elif digit > secondDigit:
                secondDigit = digit

        fusedDigits = firstDigit + secondDigit
        sum += int(fusedDigits)

    print(sum)