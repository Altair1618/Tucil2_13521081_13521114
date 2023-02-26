import matplotlib.pyplot as plt
import randomGenerator
import bruteforce


def visualize3D(points, pair):
    n = len(points)
    xAxis = []
    yAxis = []
    zAxis = []

    for i in range(n):
        if points[i] == pair[0] or points[i] == pair[1]: continue
        xAxis.append(points[i].coordinates[0])
        yAxis.append(points[i].coordinates[1])
        zAxis.append(points[i].coordinates[2])

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(xAxis, yAxis, zAxis, c="Blue", depthshade=False)

    pair1 = pair[0].getCoordinates()
    pair2 = pair[1].getCoordinates()

    ax.scatter3D(pair1[0], pair1[1], pair1[2], c="Red")
    ax.scatter3D(pair2[0], pair2[1], pair2[2], c="Red")

    ax.text(pair1[0], pair1[1], pair1[2], "(%d,%d,%d)" % (pair1[0], pair1[1], pair1[2]), size='small', va='bottom', ha='center')
    ax.text(pair2[0], pair2[1], pair2[2], "(%d,%d,%d)" % (pair2[0], pair2[1], pair2[2]), size='small', va='top', ha='center')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


if __name__ == "__main__":    
    num = int(input("Masukkan banyak titik: "))
    listPoint = randomGenerator.generateRandomPoints(num, 3)
    pair, cd = bruteforce.closestPairBruteForce(listPoint)
    print("Hasil Brute Force:")
    print(pair[0], pair[1])
    print(cd)
    visualize3D(listPoint, pair)

