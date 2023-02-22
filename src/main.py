import randomGenerator
import bruteforce
import dnc


if __name__ == "__main__":
    # Program Utama
    dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))

    listOfPoints = randomGenerator.generateRandomPoints(num, dim)

    print("Titik-titik yang dihasilkan:")
    for p in listOfPoints:
        print(p)
    print()

    bfPoint1, bfPoint2, bfClosestDistance = bruteforce.closestPairBruteForce(listOfPoints)
    print("Hasil Brute Force:")
    print(listOfPoints[bfPoint1], listOfPoints[bfPoint2])
    print(bfClosestDistance)
