# Kelas untuk Titik
class Point:
    def __init__(self, coordinates):
        # Konstruktor
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def __repr__(self):
        # Representasi Titik
        s = "("

        for i in range(self.dimension):
            if i != 0: s += ", "
            s += str(self.coordinates[i])

        s += ")"
        return s

    def distanceBetween(self, other):
        # Menghitung Euclidean Distance Antara Titik self dan Titik other
        val = 0
        for i in range(self.dimension):
            val += (self.coordinates[i] - other.coordinates[i]) ** 2

        return val ** 0.5


if __name__ == "__main__":
    # Driver Class Point
    p1 = Point([0, 3])
    p2 = Point([4, 0])

    print(p1.distanceBetween(p2))
