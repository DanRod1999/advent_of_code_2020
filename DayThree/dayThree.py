forest = []
with open('inputDayThree') as f:
    for line in f:
        forest.append(line[:-1])


def countTrees (forest, xShift, yShift):
    forestLen = len(forest[0])
    forestSize = len(forest)
    xPos = xShift
    yPos = yShift
    numTrees = 0
    while yPos < forestSize:
        if forest[yPos][xPos%forestLen] == "#":
            print(forest[yPos][:xPos%forestLen],'X',forest[yPos][xPos%forestLen+1:])
            numTrees += 1
        else:
            print(forest[yPos][:xPos%forestLen],'O',forest[yPos][xPos%forestLen+1:])
        
        yPos += yShift
        xPos += xShift

    return numTrees

numTrees = countTrees(forest,3,1) * countTrees(forest, 1,1) * countTrees(forest, 5,1) * countTrees(forest, 7, 1) * countTrees(forest, 1, 2)
print(numTrees)
