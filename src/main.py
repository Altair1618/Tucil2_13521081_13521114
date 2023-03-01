from point import Point
import randomGenerator
import bruteforce
import dnc
import visualization
import sort
import time
import fileReader
import os


def main():
    print()
    print("===============================================================================")
    print("                              Closest Pair Finder                              ")
    print("===============================================================================")

    # # Input and validation
    # # (BONUS 2) Function Generalization for Multiple Dimensions

    inp = input("\nInput using file> (Y/N): ")
    if inp.lower().find("y") != -1:
        fname = input("Enter file name (ex. test.txt): ")
        try:
            currentDir = os.path.dirname(os.path.realpath(__file__))
            listOfPoints = fileReader.readFile(os.path.join(currentDir, f"../test/{fname}"))
        except:
            try: listOfPoints = fileReader.readFile(fname)
            except: 
                print("invalid file name or invalid file content!\n")
                return
    else:
        dim = int(input("Enter Point Dimension   : "))
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
    sort.quickSort(listOfPoints, 0, len(listOfPoints) - 1, key=lambda p: p.getCoordinateValue(0))
    
    # Reset calculation counter
    bruteforce.euclidCntBF = 0
    dnc.euclidCntDnC = 0
    dnc.euclidCntDnCInBf = 0

    # Get the result using Brute Force Algorithm
    t = time.time()
    bfPairs, bfDist = bruteforce.closestPairBruteForce(listOfPoints)
    bfTime = time.time() - t

    # Get the result using Divide and Conquer Algorithm
    t = time.time()
    dncPairs, dncDist = dnc.closestPair(listOfPoints)
    dncTime = time.time() - t

    # Output result
    # totlen = max(27, max(len(str(dncPairs[0])), len(str(dncPairs[1])))) + 1
    
    pairPoints = list(set([points for pair in dncPairs for points in pair]))
    maxlen = max([len(str(ppoint)) for ppoint in pairPoints] + [27]) + 1
    pad = min(maxlen, 70)

    print("\n")
    print("                   | {: <{}}|  Divide and Conquer".format("Brute Force", pad))
    print("-------------------+-{}+-{}".format("-" * pad, "-" * pad))

    n = len(dncPairs)
    for i in range(n):
        totlen = max(27, max(len(str(dncPairs[i][0])), len(str(dncPairs[i][1])))) + 1  
        if totlen == pad:
            print("Pairs {: <{}} | {: <{}}| {}".format(i+1 if n>1 else " ", 12, str(bfPairs[i][0]), pad, str(dncPairs[i][0])))
            print("                   | {: <{}}| {}".format(str(bfPairs[i][1]), pad, str(dncPairs[i][1])))
        else:
            bf1, bf2 = str(bfPairs[i][0]), str(bfPairs[i][1])
            dc1, dc2 = str(dncPairs[i][0]), str(dncPairs[i][1])
            start1, start2, end1, end2 = 0, 0, 0, 0
            while end1 < len(bf1) or end2 < len(dc1):
                start1, start2 = end1, end2
                end1 = bf1.rfind(',',start1,start1+pad)+1 if len(bf1)-start1 > pad else len(bf1)
                end2 = dc1.rfind(',',start2,start2+pad)+1 if len(dc1)-start2 > pad else len(dc1)
                if start1 == 0 and start2 == 0:
                    print("Pairs {: <{}} | {: <{}}| {}".format(i+1 if n>1 else " ", 12, bf1[start1:end1], pad, dc1[start2:end2]))
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

    # (BONUS 1) Visualize for 3 Dimensional Input
    if listOfPoints[0].getDimension() == 3:
        vis = input("\nVisualize 3 Dimensional Plane? (Y/N) : ")
        if vis.lower().find("y") != -1:
            visualization.visualize3D(listOfPoints, dncPairs)
    if listOfPoints[0].getDimension() == 2:
        vis = input("\nVisualize 2 Dimensional Plane? (Y/N) : ")
        if vis.lower().find("y") != -1:
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
    # main()
    while True:
        main()
        ex = input("Exit program? (Y/N) : ")
        if ex.lower().find("y") != -1: 
            print("\nbye~ (^.^)/")
            break
