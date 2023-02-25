import bruteforce
import randomGenerator


def closestPair(listOfPoints):
    global sortIndex

    # Base Case
    if len(listOfPoints) <= 3:
        return bruteforce.closestPairBruteForce(listOfPoints)

    # Recursive Case

    # Get The Middle Points
    midIndex = len(listOfPoints) // 2

    # Get Divided Points
    leftPoints = listOfPoints[:midIndex]
    rightPoints = listOfPoints[midIndex:]

    # Get Closest Pair in Both Side
    leftPair, leftDistance = closestPair(leftPoints)
    rightPair, rightDistance = closestPair(rightPoints)

    # Get Minimum Distance from Both Closest Pair
    bestPair = leftPair if leftDistance > rightDistance else rightPair
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
            if candidatePoints[j].getCoordinateValue(1) - candidatePoints[i].getCoordinateValue(1) < minDist:
                break
            temp = candidatePoints[i].distanceBetween(candidatePoints[j])
            if temp < minDist:
                minDist = temp
                bestPair = [candidatePoints[i], candidatePoints[j]]

    return bestPair, minDist


if __name__ == "__main__":
    dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))

    listOfPoints = randomGenerator.generateRandomPoints(num, dim)

    # ip1, ip2, closestDistance = closestPair(listOfPoints)

    # print(f"\nClosest Pair:")
    # print(listOfPoints[ip1], listOfPoints[ip2])
    # print(closestDistance)
