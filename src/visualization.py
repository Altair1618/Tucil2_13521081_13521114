import matplotlib.pyplot as plt
import randomGenerator
import bruteforce

def visualize3D(points, i1, i2):
    n = len(points)
    xAxis = []
    yAxis = []
    zAxis = []

    for i in range(n):
        if i == i1 or i == i2: continue
        xAxis.append(points[i].coordinates[0])
        yAxis.append(points[i].coordinates[1])
        zAxis.append(points[i].coordinates[2])

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(xAxis, yAxis, zAxis, c="Black", depthshade=False)

    pair1 = points[i1].getCoor()
    pair2 = points[i2].getCoor()

    ax.scatter3D(pair1[0], pair1[1], pair1[2], c="Red")
    ax.scatter3D(pair2[0], pair2[1], pair2[2], c="Red")

    ax.text(pair1[0], pair1[1], pair1[2], "(%d,%d,%d)" % pair1, size='small', va='bottom', ha='center')
    ax.text(pair2[0], pair2[1], pair2[2], "(%d,%d,%d)" % pair2, size='small', va='top', ha='center')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


if __name__ == "__main__":    
    num = int(input("Masukkan banyak titik: "))
    listPoint = randomGenerator.generateRandomPoints(num, 3)
    idx1, idx2, cd = bruteforce.closestPairBruteForce(listPoint)
    print("Hasil Brute Force:")
    print(listPoint[idx1], listPoint[idx2])
    print(cd)
    visualize3D(listPoint, idx1, idx2)

