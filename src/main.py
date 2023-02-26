import randomGenerator
import bruteforce
import dnc
import visualization
from point import Point
import time

# Program Utama
if __name__ == "__main__":
    print()
    print("=============================================================")
    print("                    Closest Pair Finder                      ")
    print("=============================================================")

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
    listOfPoints.sort(key=lambda p: p.getCoordinateValue(0))

    # Get the result using Brute Force Algorithm
    t = time.time()
    bfPairs, bfDist = bruteforce.closestPairBruteForce(listOfPoints)
    bfTime = time.time() - t

    # Get the result using Divide and Conquer Algorithm
    t = time.time()
    dncPairs, dncDist = dnc.closestPair(listOfPoints)
    dncTime = time.time() - t    

    # Output result
    pad = max(18, max(len(str(dncPairs[0])), len(str(dncPairs[1])))) + 1
    print("\n")
    print("                   | {: <{}}|  Divide and Conquer".format("Brute Force", pad))
    print("-------------------+-{}+-{}".format("-"*pad, "-"*pad))
    print("Pairs              | {: <{}}| {}".format(str(bfPairs[0]), pad, str(dncPairs[0])))
    print("                   | {: <{}}| {}".format(str(bfPairs[1]), pad, str(dncPairs[1])))
    print("-------------------+-{}+-{}".format("-"*pad, "-"*pad))
    print("Distance           | {: <{}}| {}".format(str(bfDist)[:pad-1], pad, str(dncDist)[:pad-1]))
    print("-------------------+-{}+-{}".format("-"*pad, "-"*pad))
    print("Calculation Amount | {: <{}}| {}".format(str(bruteforce.euclidCntBF)[:pad-1], pad, str(dnc.euclidCntDnC)[:pad-1]))
    print("-------------------+-{}+-{}".format("-"*pad, "-"*pad))
    print("Time Taken         | {: <{}}| {}".format(str(bfTime)[:pad-1], pad, str(dncTime)[:pad-1]))

    # (BONUS 1) Visualize for 3 Dimensional Input
    if dim == 3:
        vis = input("\nVisualize 3 Dimensional Plane? (Y/y) : ")
        if vis == 'y' or vis == 'Y':
            visualization.visualize3D(listOfPoints, dncPairs)
    print()
