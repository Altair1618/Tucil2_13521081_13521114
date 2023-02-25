import randomGenerator

euclidCntBF = 0

def closestPairBruteForce(listOfPoints):
    # Menentukan Closest Pair dengan Brute Force
    # Digunakan untuk Uji Coba
    closestDistance = -1
    indexPoint1 = -1
    indexPoint2 = -1
    global euclidCntBF
    for i in range(len(listOfPoints) - 1):
        for j in range(i + 1, len(listOfPoints)):
            dist = listOfPoints[i].distanceBetween(listOfPoints[j])
            euclidCntBF += 1
            if closestDistance == -1 or dist < closestDistance:
                closestDistance = dist
                indexPoint1 = i
                indexPoint2 = j
    return [listOfPoints[indexPoint1], listOfPoints[indexPoint2]], closestDistance


if __name__ == "__main__":
    dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))

    listOfPoints = randomGenerator.generateRandomPoints(num, dim)
    closestPair, closestDistance= closestPairBruteForce(listOfPoints)


    print(f"\nClosest Pair:")
    print(closestPair[0], closestPair[1])
    print(closestDistance, euclidCntBF)
