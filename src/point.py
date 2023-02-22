class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def __repr__(self):
        s = "("

        for i in range(self.dimension):
            if i != 0: s += ", "
            s += str(self.coordinates[i])

        s += ")"
        return s

    def isSameDimension(self, other):
        return self.dimension == other.dimension

    def distanceBetween(self, other):
        if not self.isSameDimension(other): return -1

        val = 0
        for i in range(self.dimension):
            val += (self.coordinates[i] - other.coordinates[i]) ** 2

        return val ** 0.5


if __name__ == "__main__":
    p1 = Point([0, 3])
    p2 = Point([4, 0])

    print(p1.distanceBetween(p2))
