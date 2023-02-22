import randomGenerator
from point import Point


def closestPairBruteForce(listOfPoints):
    # Menentukan Closest Pair dengan Brute Force
    # Digunakan untuk Uji Coba
    closestDistance = -1
    indexPoint1 = -1
    indexPoint2 = -1
    for i in range(len(listOfPoints) - 1):
        for j in range(i + 1, len(listOfPoints)):
            dist = listOfPoints[i].distanceBetween(listOfPoints[j])
            if closestDistance == -1 or dist < closestDistance:
                closestDistance = dist
                indexPoint1 = i
                indexPoint2 = j
    return indexPoint1, indexPoint2, closestDistance


if __name__ == "__main__":
    dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))

    listOfPoints = randomGenerator.generateRandomPoints(num, dim)
    ip1, ip2, closestDistance = closestPairBruteForce(listOfPoints)

    for p in listOfPoints:
        print(p)

    print(f"\nClosest Pair:")
    print(listOfPoints[ip1], listOfPoints[ip2])
    print(closestDistance)
