from point import Point
import randomGenerator
import bruteforce
import dnc
import visualization
import sort
import time


def main():
    print()
    print("===============================================================================")
    print("                              Closest Pair Finder                              ")
    print("===============================================================================")

    # Input and validation
    # (BONUS 2) Function Generalization for Multiple Dimensions
    dim = int(input("\nEnter Point Dimension   : "))
    while dim < 2:
        print("Invalid Input! Dimension must be higher than 1.\n")
        dim = int(input("Enter Point Dimension   : "))

    num = int(input("Enter Number of Points  : "))
    while num < 2:
        print("Invalid input! There must be more than 1 point.\n")
        num = int(input("Enter Number of Points  : "))

    # Generate N random points
    listOfPoints = randomGenerator.generateRandomPoints(num, dim)

    # Sort by x values
    sort.quickSort(listOfPoints, 0, num - 1, key=lambda p: p.getCoordinateValue(0))

    # Get the result using Brute Force Algorithm
    t = time.time()
    bfPairs, bfDist = bruteforce.closestPairBruteForce(listOfPoints)
    bfTime = time.time() - t

    # Get the result using Divide and Conquer Algorithm
    t = time.time()
    dncPairs, dncDist = dnc.closestPair(listOfPoints)
    dncTime = time.time() - t

    # Output result
    totlen = max(27, max(len(str(dncPairs[0])), len(str(dncPairs[1])))) + 1
    pad = min(totlen, 70)

    print("\n")
    print("                   | {: <{}}|  Divide and Conquer".format("Brute Force", pad))
    print("-------------------+-{}+-{}".format("-" * pad, "-" * pad))
    if totlen == pad:
        print("Pairs              | {: <{}}| {}".format(str(bfPairs[0]), pad, str(dncPairs[0])))
        print("                   | {: <{}}| {}".format(str(bfPairs[1]), pad, str(dncPairs[1])))
    else:
        bf1, bf2 = str(bfPairs[0]), str(bfPairs[1])
        dc1, dc2 = str(dncPairs[0]), str(dncPairs[1])
        start1, start2, end1, end2 = 0, 0, 0, 0
        while end1 < len(bf1) or end2 < len(dc1):
            start1, start2 = end1, end2
            end1 = bf1.rfind(',',start1,start1+pad)+1 if len(bf1)-start1 > pad else len(bf1)
            end2 = dc1.rfind(',',start2,start2+pad)+1 if len(dc1)-start2 > pad else len(dc1)
            if start1 == 0 and start2 == 0:
                print("Pairs              | {: <{}}| {}".format(bf1[start1:end1], pad, dc1[start2:end2]))
            else:
                print("                   | {: <{}}| {}".format(bf1[start1:end1], pad, dc1[start2:end2]))
        start1, start2, end1, end2 = 0, 0, 0, 0
        while end1 < len(bf2) or end2 < len(dc2):
            start1, start2 = end1, end2
            end1 = bf2.rfind(',',start1,start1+pad)+1 if len(bf2)-start1 > pad else len(bf2)
            end2 = dc2.rfind(',',start2,start2+pad)+1 if len(dc2)-start2 > pad else len(dc2)
            print("                   | {: <{}}| {}".format(bf2[start1:end1], pad, dc2[start2:end2]))
    print("-------------------+-{}+-{}".format("-" * pad, "-" * pad))
    print("Distance           | {: <{}}| {}".format(str(bfDist)[:pad - 1], pad, str(dncDist)[:pad - 1]))
    print("-------------------+-{}+-{}".format("-" * pad, "-" * pad))
    print("Calculation Amount | {: <{}}| {}".format(str(int(bruteforce.euclidCntBF - dnc.euclidCntDnCInBf))[:pad - 1],
                                                    pad, str(int(dnc.euclidCntDnC + dnc.euclidCntDnCInBf))[:pad - 1]))
    print("-------------------+-{}+-{}".format("-" * pad, "-" * pad))
    print("Time Taken (s)     | {: <{}}| {}".format(str(bfTime)[:pad - 1], pad, str(dncTime)[:pad - 1]))

    print(bfPairs[0])
    print(bfPairs[1])

    # (BONUS 1) Visualize for 3 Dimensional Input
    if dim == 3:
        vis = input("\nVisualize 3 Dimensional Plane? (Y/y) : ")
        if vis == 'y' or vis == 'Y':
            visualization.visualize3D(listOfPoints, dncPairs)
    if dim == 2:
        vis = input("\nVisualize 2 Dimensional Plane? (Y/y) : ")
        if vis == 'y' or vis == 'Y':
            visualization.visualize2D(listOfPoints, dncPairs)
    print()


def debug():
    dim = int(input("\nEnter Point Dimension   : "))
    num = int(input("Enter Number of Points  : "))
    for i in range(100):
        listOfPoints = randomGenerator.generateRandomPoints(num, dim)
        sort.quickSort(listOfPoints, 0, num - 1, key=lambda p: p.getCoordinateValue(0))
        bfPairs, bfDist = bruteforce.closestPairBruteForce(listOfPoints)
        dncPairs, dncDist = dnc.closestPair(listOfPoints)

        if bfDist != dncDist:
            print("Ada kegagalan")
            print(listOfPoints)
            break


# Program Utama
if __name__ == "__main__":
    main()
    # debug()
