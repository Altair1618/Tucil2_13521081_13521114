import random
from point import Point

# Konstanta Maksimal Nilai Koordinat
MAXN = 1000


def generateRandomPoints(num, dimension):
    # Menghasilkan Titik Random Sebanyak num Berdimensi dimension
    # Dipastikan Semua Titik Unik
    listPoint = []
    for i in range(num):
        while True:
            coordinates = []
            for j in range(dimension):
                coordinates += [random.randint(0, MAXN)]
            if Point not in listPoint:
                break
        listPoint += [Point(coordinates)]

    return listPoint
