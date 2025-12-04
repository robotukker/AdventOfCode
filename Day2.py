def CheckPair(half1, half2):
    return half1 == half2

def splitID(id):
    return id[:(len(id)//2)], id[(len(id)//2):]

def CheckID(id):
    first, second = splitID(id)
    if CheckPair(first, second):
        return first
    else:
        CheckID(first)

def CheckSequence(sequence):
    start, end = sequence.split('-')
    sum = 0
    
    for id in range(int(start),int(end)+1):
        if CheckID(str(id)) is not None:
            sum += id
    return sum

def StringtoList(idString):
    return idString.split(',')

if __name__ == "__main__":
    with open('Input2.txt', 'r') as file:
        SequenceString = file.read()

    SequenceList = StringtoList(SequenceString)

    sumTotal= 0
    for sequence in SequenceList:
        sumTotal += CheckSequence(sequence)

    print(sumTotal)
        




