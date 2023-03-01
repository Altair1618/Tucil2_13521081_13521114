import matplotlib.pyplot as plt
import randomGenerator
import bruteforce, dnc
from point import Point
import fileReader


def visualize3D(points, pairs):
    n = len(points)
    xAxis = []
    yAxis = []
    zAxis = []
    
    pairPoints = list(set([points for pair in pairs for points in pair]))
    labeled = [False for i in range(len(pairPoints))]

    for i in range(n):
        if points[i] in pairPoints: continue
        xAxis.append(points[i].coordinates[0])
        yAxis.append(points[i].coordinates[1])
        zAxis.append(points[i].coordinates[2])


    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_title("3D VISUALIZATION")
    ax.scatter3D(xAxis, yAxis, zAxis, c="Blue", depthshade=False)

    p = len(pairs)
    for i in range(p):

        pair1 = pairs[i][0].getCoordinates()
        pair2 = pairs[i][1].getCoordinates()
        
        ax.scatter3D(pair1[0], pair1[1], pair1[2], c="Red")
        ax.scatter3D(pair2[0], pair2[1], pair2[2], c="Red")

        ax.plot((pair1[0], pair2[0]), (pair1[1], pair2[1]), (pair1[2], pair2[2]), c="Red")

        if pair1[2] < pair2[2]: va1="top"; va2="bottom"
        else : va1="bottom"; va2="top"

        if not labeled[pairPoints.index(pairs[i][0])]:
            ax.text(pair1[0], pair1[1], pair1[2], "(%.1f,%.1f,%.1f)" % (pair1[0], pair1[1], pair1[2]), size='small', va=va1, ha='center')
            labeled[pairPoints.index(pairs[i][0])] = True
        if not labeled[pairPoints.index(pairs[i][1])]:
            ax.text(pair2[0], pair2[1], pair2[2], "(%.1f,%.1f,%.1f)" % (pair2[0], pair2[1], pair2[2]), size='small', va=va2, ha='center')
            labeled[pairPoints.index(pairs[i][1])] = True

    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')
    plt.show()

def visualize2D(points, pairs):
    n = len(points)
    xAxis = []
    yAxis = []
    
    pairPoints = list(set([points for pair in pairs for points in pair]))
    labeled = [False for i in range(len(pairPoints))]

    for i in range(n):
        if points[i] in pairPoints: continue
        xAxis.append(points[i].coordinates[0])
        yAxis.append(points[i].coordinates[1])


    fig = plt.figure()
    ax = plt.axes()
    ax.set_title("2D VISUALIZATION")
    ax.scatter(xAxis, yAxis, c="Blue")

    p = len(pairs)
    for i in range(p):

        pair1 = pairs[i][0].getCoordinates()
        pair2 = pairs[i][1].getCoordinates()
        
        ax.scatter(pair1[0], pair1[1], c="Red")
        ax.scatter(pair2[0], pair2[1], c="Red")

        ax.plot((pair1[0], pair2[0]), (pair1[1], pair2[1]), c="Red")

        if pair1[1] < pair2[1]: va1="top"; va2="bottom"
        else : va1="bottom"; va2="top"

        if not labeled[pairPoints.index(pairs[i][0])]:
            ax.text(pair1[0], pair1[1], "(%.1f,%.1f)" % (pair1[0], pair1[1]), size='small', va=va1, ha='center')
            labeled[pairPoints.index(pairs[i][0])] = True
        if not labeled[pairPoints.index(pairs[i][1])]:
            ax.text(pair2[0], pair2[1], "(%.1f,%.1f)" % (pair2[0], pair2[1]), size='small', va=va2, ha='center')
            labeled[pairPoints.index(pairs[i][1])] = True

    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    plt.grid()
    plt.show()


if __name__ == "__main__":    
    # num = int(input("Masukkan banyak titik: "))
    # listPoint = randomGenerator.generateRandomPoints(num, 3)
    listPoint = fileReader.readFile("testInput1.txt")
    pairs, cd = dnc.closestPair(listPoint)
    print("Hasil dnc:")
    print(pairs)
    pairs, cd = bruteforce.closestPairBruteForce(listPoint)
    print("hasil bf:")
    print(pairs)
    print(cd)
    print(listPoint)
    visualize3D(listPoint, pairs)
