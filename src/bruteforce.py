import random
from point import Point

if __name__ == "__main__":
    dim = int(input("Masukkan dimensi titik: "))
    num = int(input("Masukkan jumlah titik: "))

    listPoint = []
    for i in range(num):
        coordinates = []
        for j in range(dim):
            coordinates += [random.randint(0, 10)]
        listPoint += [Point(coordinates)]

    closestDistance = -1
    ip1 = -1
    ip2 = -1
    for i in range(num - 1):
        for j in range(i + 1, num):
            dist = listPoint[i].distanceBetween(listPoint[j])
            if closestDistance == -1 or dist < closestDistance:
                closestDistance = dist
                ip1 = i
                ip2 = j

    for p in listPoint:
        print(p)

    print(f"\nClosest Pair:")
    print(listPoint[ip1], listPoint[ip2])
    print(closestDistance)
