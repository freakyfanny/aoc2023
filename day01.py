def getFirstAndLastDigit(inputString):
    firstDigit = None
    lastDigit = None

    for char in inputString:
        if char.isdigit():
            if firstDigit is None:
                firstDigit = char
            lastDigit = char

    if firstDigit is None:
        return 0
    elif firstDigit == lastDigit:
        return int(firstDigit * 2)
    else:
        return int(firstDigit + lastDigit)
        
def processFile(fileName):
    results = []

    # Read lines from the file
    with open(fileName, 'r') as file:
        lines = file.readlines()

        for line in lines:
            lineResult = getFirstAndLastDigit(line)
            results.append(lineResult)

    return results
    
def calculateSum(fileName):
    results = processFile(fileName)
    totalSum = sum(results)
    return totalSum

fileName = "puzzle-input-day01.txt"
total = calculateSum(fileName)
print("Total sum of first and last digits:", total)
