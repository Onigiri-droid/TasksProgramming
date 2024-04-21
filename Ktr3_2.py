import random


class Matrix:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.data = [[random.randint(-100, 100) for _ in range(self.cols)] for _ in range(self.rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def matrix_multiplication(self, other):
        if self.cols != other.rows:
            print(
                "Нельзя умножить матрицы: количество столбцов первой матрицы не равно количеству строк второй матрицы.")
            return None

        result = Matrix()
        result.data = [[0 for _ in range(other.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def scalar_multiplication(self, scalar):
        result = Matrix()
        result.data = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return result

    def average_of_row(self, k):
        if k < 0 or k >= self.rows:
            print("Некорректный номер строки.")
            return None

        row_sum = sum(self.data[k])
        return row_sum / self.cols


# Пример использования класса Matrix

# Создание первой матрицы
print("Первая матрица:")
matrix1 = Matrix()
print(matrix1)

# Создание второй матрицы
print("Вторая матрица:")
matrix2 = Matrix()
print(matrix2)

# Умножение матриц
print("Результат умножения матриц:")
result_matrix = matrix1.matrix_multiplication(matrix2)
if result_matrix is not None:
    print(result_matrix)

# Номер строки для вычисления среднего арифметического
k = int(input('Введите номер строки: '))
average = matrix1.average_of_row(k)
if average is not None:
    print(f"Среднее арифметическое элементов {k}-й строки первой матрицы: {average}\n")

# Число для умножения первой матрицы
scalar = int(input('Введите число для умножения первой матрицы: '))
print(f"Результат умножения первой матрицы на число {scalar}:")
result_scalar_multiplication = matrix1.scalar_multiplication(scalar)
print(result_scalar_multiplication)