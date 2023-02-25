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

    bfPairs, bfClosestDistance = bruteforce.closestPairBruteForce(listOfPoints)
    print("Hasil Brute Force:")
    print(bfPairs[0], bfPairs[1])
    print(bfClosestDistance)

    dncPairs, dncClosestDistance = dnc.closestPair(listOfPoints)
    print("Hasil Divide and Conquer:")
    print(dncPairs[0], dncPairs[1])
    print(dncClosestDistance)

    print(bfClosestDistance == dncClosestDistance)
