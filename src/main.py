import randomGenerator
import bruteforce
import dnc
import visualization
from point import Point
import time

# Program Utama
if __name__ == "__main__":
    print("========================================")
    print("        Pencari Titik Terdekat")
    print("========================================")

    # Input dan validasi
    dim = int(input("\nMasukkan dimensi titik: "))
    while dim < 2:
        print("Dimensi tidak valid, Dimensi harus lebih dari 1.\n")
        dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))
    while num < 2:
        print("Jumalh titik tidak valid, jumlah titik harus lebih dari 1.\n")
        num = int(input("Masukkan jumlah titik: "))
    

    # Menghasilkan kumpulan titik random
    listOfPoints = randomGenerator.generateRandomPoints(num, dim)

    # Sort by x values
    listOfPoints.sort(key=lambda p: p.getCoordinateValue(0))

    t1 = time.time()
    bfPairs, bfClosestDistance = bruteforce.closestPairBruteForce(listOfPoints)
    t2 = time.time()

    print("\n========================================")
    print("\nHasil Brute Force:")
    print(bfPairs[0], bfPairs[1])
    print("Jarak:", bfClosestDistance)
    print("Banyak perhitungan euclidean:", bruteforce.euclidCntBF)
    print("Waktu yang dibutuhkan:", t2 - t1, "s")

    t1 = time.time()
    dncPairs, dncClosestDistance = dnc.closestPair(listOfPoints)
    t2 = time.time()

    print("\n========================================")
    print("\nHasil Divide and Conquer:")
    print(dncPairs[0], dncPairs[1])
    print("Jarak:", dncClosestDistance)
    print("Banyak perhitungan euclidean:", dnc.euclidCntDnC)
    print("Waktu yang dibutuhkan:", t2 - t1, "s")

    if dim == 3:
        print("\n========================================")
        v = input("\nMasukkan (Y/y) untuk visualisasi bidang 3D: ")
        if v == 'y' or v == "Y":
            visualization.visualize3D(listOfPoints, dncPairs)
    
    print("\n========================================")
