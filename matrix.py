class Matrix:
    def __init__(self, array):
        self.array = array
        self.vertical = len(array[0])
        self.horizontal = len(array)
        for line in array:
            if len(line) != self.vertical:
                raise ValueError

    def dim(self) -> tuple:
        return self.vertical, self.horizontal

    def __mul__(self, scalar: int):
        data = []
        for i in range(0, self.horizontal):
            stroke = []
            for j in range(0, self.vertical):
                stroke.append(scalar * self.array[i][j])
            data.append(stroke)
        return Matrix(data)

    def __add__(self, other):
        data = []
        if isinstance(other, Matrix):
            for i in range(0, self.horizontal):
                stroke = []
                for j in range(0, self.vertical):
                    stroke.append(other.array[i][j] + self.array[i][j])
                data.append(stroke)
            return Matrix(data)
        return NotImplemented

    def __sub__(self, other):
        return self + other * (-1)

    def __str__(self):
        result = str()
        for i in range(0, self.horizontal):
            for j in range(0, self.vertical):
                result += " " + str(self.array[i][j])
            result += "\n"
        return result

    def __eq__(self, other):
        for i in range(0, self.horizontal):
            for j in range(0, self.vertical):
                if other.array[i][j] != self.array[i][j]:
                    return False
        return True


if __name__ == '__main__':
    a = Matrix([[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]])

    b = Matrix([[-1, 0, 3],
                [0, 0, 0],
                [3, 0, 0]])

    print(a - b)
    print(b * 2)
