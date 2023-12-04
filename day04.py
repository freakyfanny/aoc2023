def evaluateCard(card):
    _, nums = card.split(":")
    winnerNums, nums = nums.split("|")
    winnerNums = [int(w) for w in winnerNums.split() if w]
    nums = [int(n) for n in nums.split() if n]
    return len(set(nums).intersection(set(winnerNums)))

def part1(cards):
    sumTotal = 0
    for card in cards:
        currentExponent = evaluateCard(card) - 1
        if currentExponent >= 0:
            sumTotal += 2**currentExponent
    print("Total points:", sumTotal)

def part2(cards):
    cardNums = [1] * len(cards)
    for id, card in enumerate(cards):
        wins = evaluateCard(card)
        cardNums[id + 1 : id + wins + 1] = [x + cardNums[id] for x in cardNums[id + 1 : id + wins + 1]]

    print("Total cards:", int(sum(cardNums)))

# Read card data from file
filePath = 'puzzle-day04.txt'
with open(filePath, 'r') as file:
    cardsData = file.readlines()

part1(cardsData)
part2(cardsData)
