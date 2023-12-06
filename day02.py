possibleCubeCount = {
    "red": 12,
    "green": 13,
    "blue": 14
}

result = 0

with open('input.txt', 'r') as file:
    gameInput = file.read()

def isGamePossible(line: str) -> bool:
    subGames = line.split(":")[1].split(";")
    for subGame in subGames:
        for numCubes in subGame.split(','):
            num, color = numCubes.split()
            if int(num) > possibleCubeCount[color]:
                return False
    return True


for index, line in enumerate(gameInput.split("\n")):
    if isGamePossible(line):
        print(f"Game {index + 1} is possible")
        result += (index + 1)

print(result)
