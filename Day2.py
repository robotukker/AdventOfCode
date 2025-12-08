def CheckPair(part1, part2):
    return part1 == part2

def CheckID(id):
    for splitFactor in range(2,11):
        # stop after smallest splits is reached
        if splitFactor > len(id):
            return False
        
        # skip splits of unequal length
        if (len(id) % splitFactor) != 0:
            continue

        splitlength = len(id)//splitFactor
        splits = [id[i*splitlength:(i+1)*splitlength] for i in range(splitFactor)]

        # check if splits are equal
        if all(x == splits[0] for x in splits):
            return True
            
     # if no repeating patern is found
    return False

def CheckSequence(sequence):
    start, end = sequence.split('-')
    sum = 0
    
    for id in range(int(start),int(end)+1):
        if CheckID(str(id)):
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
        




