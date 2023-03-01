from point import Point


def readFile(fileName):
    f = open(fileName.encode('unicode_escape').decode().replace("\"", ""), 'r')
    raw = f.readlines()

    for i in range(len(raw)):
        raw[i] = raw[i][:-1]

    dim = int(raw[0])
    num = int(raw[1])

    listOfPoints = []
    for i in range(num):
        p = [float(c) for c in raw[i + 2].split()]
        listOfPoints += [Point(p)]

    f.close()

    return listOfPoints


if __name__ == "__main__":
    listOfPoints = readFile("D:\FARHAN\Kuliah\Semester 4\Stima\Tugas\Tucil2_13521081_13521114\test\testInput1.txt")
    print(listOfPoints)
