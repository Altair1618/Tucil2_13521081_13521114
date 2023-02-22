import bruteforce
import randomGenerator
from point import Point


def getX(point):
    return point.coordinates[0]


def closestPair(listOfPoints):
    if len(listOfPoints) <= 3:
        return bruteforce.closestPairBruteForce(listOfPoints)
    midIndex = len(listOfPoints) / 2
    midPoint = listOfPoints[midIndex]
    ip11, ip12, distLeft = closestPair(listOfPoints[:mid])
    ip21, ip22, distRight = closestPair(listOfPoints[mid:])
    min_dist = min(distLeft, distRight)
    strip = []
    for i in range(len(listOfPoints)):
        if abs(getX(listOfPoints[i]) - getX(midPoint)) < min_dist:
            strip += listOfPoints[i]


if __name__ == "__main__":
    dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))

    listOfPoints = randomGenerator.generateRandomPoints(num, dim)

    sortedList = sorted(listOfPoints, key=getX)
    indexPoint1, indexPoint2, list = closestPair(listOfPoints)
    # ip1, ip2, closestDistance = closestPair(listOfPoints)

    for p in list:
        print(p)

    # print(f"\nClosest Pair:")
    # print(listOfPoints[ip1], listOfPoints[ip2])
    # print(closestDistance)
