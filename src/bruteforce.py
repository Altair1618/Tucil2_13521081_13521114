import randomGenerator

euclidCntBF = 0


def closestPairBruteForce(listOfPoints):
    global euclidCntBF

    # Menentukan Closest Pair dengan Brute Force
    # Digunakan untuk Uji Coba
    closestDistance = -1
    closestPairs = []

    for i in range(len(listOfPoints) - 1):
        for j in range(i + 1, len(listOfPoints)):
            dist = listOfPoints[i].distanceBetween(listOfPoints[j])
            euclidCntBF += 1
            if closestDistance == -1 or dist < closestDistance:
                closestDistance = dist
                closestPairs = [[listOfPoints[i], listOfPoints[j]]]
            elif dist == closestDistance:
                closestPairs += [[listOfPoints[i], listOfPoints[j]]]

    return closestPairs, closestDistance


if __name__ == "__main__":
    dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))

    listOfPoints = randomGenerator.generateRandomPoints(num, dim)
    closestPair, closestDistance = closestPairBruteForce(listOfPoints)

    print(f"\nClosest Pair:")
    print(closestPair)
    print(closestDistance, euclidCntBF)
