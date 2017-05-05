def getSpriteSheet(spriteSheet, y, width, height):
    frame = []
    for x in range(5):
        image = spriteSheet.getImage(60 * x, y, width, height)
        frame.append(image)
    return frame

def swapIn1Arr(arr, x, y):
    """
    :param arr: 1D
    :param x:
    :param y:
    :return: None
    """
    listStr = list(arr)
    listStr[x], listStr[y] = listStr[y], listStr[x]
    return ''.join(listStr)

def swapIn2Arr(arr1, arr2, idx):
    a1 = list(arr1)
    a2 = list(arr2)
    a1[idx], a2[idx] = a2[idx], a1[idx]
    return ''.join(a1), ''.join(a2)

def findPath(tree, sol):
    if tree == None:
        return
    sol.append(tree)
    findPath(tree.parent, sol)

def findStep(tree):
    steps = []
    findPath(tree,steps)
    result = []
    length = len(steps)

    for i in range(0, length - 1, 1):
        y2, x2 = steps[i].getPlayer()
        y1, x1 = steps[i + 1].getPlayer()

        if x1 == x2:
            if y2 > y1:
                result.append('d')
            elif y2 < y1:
                result.append('u')
            else:
                result.append('n')
        elif y1 == y2:
            if x2 > x1:
                result.append('r')
            elif x2 < x1:
                result.append('l')
            else:
                result.append('n')
    result.reverse()
    return result

def findStep2(tree):
    steps = []
    findPath(tree, steps)
    result = []

    for step in steps:
        temp = []
        for move in step.mummy_move:
            temp.append(move)
        temp.reverse()
        result += temp
    result.reverse()
    return result