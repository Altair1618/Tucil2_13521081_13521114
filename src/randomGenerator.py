import random
from point import Point

# Konstanta Maksimal Nilai Koordinat
MAXN = 1000


def generateRandomPoints(num, dimension):
    # Menghasilkan Titik Random Sebanyak num Berdimensi dimension

    listPoint = []
    for i in range(num):
        coordinates = []
        for j in range(dimension):
            coordinates += [round(random.uniform(-MAXN, MAXN), 2)]
        listPoint += [Point(coordinates)]

    return listPoint
