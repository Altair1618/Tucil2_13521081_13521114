import bruteforce
import sort
import randomGenerator
from point import Point

euclidCntDnC = 0
euclidCntDnCInBf = 0


def closestPair(listOfPoints):
    # Euclidean counter
    global euclidCntDnC
    global euclidCntDnCInBf

    n = len(listOfPoints)
    
    # Base Case
    if n <= 3:
        euclidCntDnCInBf += (n * (n - 1)) / 2
        return bruteforce.closestPairBruteForce(listOfPoints)

    # Recursive Case
    # Get The Dimension
    dim = listOfPoints[0].getDimension()
    sqrtdim = dim ** 0.5

    # Get The Middle Points
    midIndex = n // 2

    # Get Divided Points
    leftPoints = listOfPoints[:midIndex]
    rightPoints = listOfPoints[midIndex:]

    # Get Closest Pair in Both Side
    leftPairs, leftDistance = closestPair(leftPoints)
    rightPairs, rightDistance = closestPair(rightPoints)

    # Get Minimum Distance from Both Closest Pair
    if leftDistance < rightDistance:
        bestPairs = leftPairs
    elif leftDistance > rightDistance:
        bestPairs = rightPairs
    else:
        bestPairs = leftPairs + rightPairs
    minDist = min(leftDistance, rightDistance)

    # Get the Absis Coordinate of the Center
    centerAbsis = (leftPoints[-1].getCoordinateValue(0) + rightPoints[0].getCoordinateValue(0)) / 2

    # Filter the Points That Distance to Center Smaller than min_dist
    candidatePoints = []
    for p in listOfPoints:
        if abs(p.getCoordinateValue(0) - centerAbsis) <= minDist:
            candidatePoints += [p]

    # Sort by y value
    sort.quickSort(candidatePoints, 0, len(candidatePoints)-1, key=lambda p: p.getCoordinateValue(1))

    # Merging Process
    for i in range(len(candidatePoints) - 1):
        for j in range(i + 1, len(candidatePoints)):
            if candidatePoints[j].getCoordinateValue(1) - candidatePoints[i].getCoordinateValue(1) > minDist:
                break

            pos = True
            mhtDist = 0
            for k in range(dim):
                mhtDist += abs(candidatePoints[j].getCoordinateValue(k) - candidatePoints[i].getCoordinateValue(k))
                if mhtDist > minDist * sqrtdim:
                    pos = False
                    break
            if not pos:
                continue

            temp = candidatePoints[i].distanceBetween(candidatePoints[j])
            euclidCntDnC += 1
            if temp < minDist:
                minDist = temp
                bestPairs = [[candidatePoints[i], candidatePoints[j]]]
            elif temp == minDist:
                addedPair = [candidatePoints[i], candidatePoints[j]]
                if addedPair not in bestPairs and [candidatePoints[j], candidatePoints[i]] not in bestPairs:
                    bestPairs += [addedPair]

    return bestPairs, minDist


if __name__ == "__main__":
    # dim = int(input("Masukkan dimensi titik: "))
    # num = int(input("Masukkan jumlah titik: "))
    
    # listOfPoints = randomGenerator.generateRandomPoints(num, dim)
    listOfPoints = [Point([1, 1]), Point([3, 4]), Point([999, 7]), Point([200, 10])]
    closestPairs, closestDistance = closestPair(listOfPoints)

    print(f"\nClosest Pair:")
    for pair in closestPairs:
        print(pair)
    print(closestDistance, euclidCntDnC + euclidCntDnCInBf)
