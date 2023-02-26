import bruteforce

euclidCntDnC = 0

def closestPair(listOfPoints):
    # Base Case
    if len(listOfPoints) <= 3:
        return bruteforce.closestPairBruteForce(listOfPoints)

    # Euclidean counter
    global euclidCntDnC

    # Recursive Case
    # Get The Dimension
    dim = listOfPoints[0].getDimension()

    # Get The Middle Points
    midIndex = len(listOfPoints) // 2

    # Get Divided Points
    leftPoints = listOfPoints[:midIndex]
    rightPoints = listOfPoints[midIndex:]

    # Get Closest Pair in Both Side
    leftPair, leftDistance = closestPair(leftPoints)
    rightPair, rightDistance = closestPair(rightPoints)

    # Get Minimum Distance from Both Closest Pair
    bestPair = leftPair if leftDistance < rightDistance else rightPair
    minDist = min(leftDistance, rightDistance)

    # Get the Absis Coordinate of the Center
    centerAbsis = (leftPoints[-1].getCoordinateValue(0) + rightPoints[0].getCoordinateValue(0)) / 2

    # Filter the Points That Distance to Center Smaller than min_dist
    candidatePoints = []
    for p in listOfPoints:
        if abs(p.getCoordinateValue(0) - centerAbsis) < minDist:
            candidatePoints += [p]

    # Sort by y value
    candidatePoints.sort(key=lambda p: p.getCoordinateValue(1))

    # Merging Process
    for i in range(len(candidatePoints) - 1):
        for j in range(i + 1, len(candidatePoints)):
            if candidatePoints[j].getCoordinateValue(1) - candidatePoints[i].getCoordinateValue(1) >= minDist:
                break
            pos = True
            for k in range(2, dim):
                if abs(candidatePoints[j].getCoordinateValue(k) - candidatePoints[i].getCoordinateValue(k)) >= minDist:
                    pos = False
                    break
            if not pos:
                continue

            temp = candidatePoints[i].distanceBetween(candidatePoints[j])
            euclidCntDnC += 1
            if temp < minDist:
                minDist = temp
                bestPair = [candidatePoints[i], candidatePoints[j]]

    return bestPair, minDist
