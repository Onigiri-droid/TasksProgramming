import random

# 2.1 Создание двумерного массива случайных чисел
def create_2d(size):
    return [[random.uniform(-100, 100) for _ in range(size)] for _ in range(size)]

# Запись двумерного массива в файл с разделителем между матрицами
def write_2d(file_name, array1, array2):
    with open(file_name, 'w') as file:
        # Записываем первую матрицу
        for row in array1:
            file.write(','.join(map(str, row)) + '\n')
        # Добавляем пустую строку в качестве разделителя
        file.write('\n')
        # Записываем вторую матрицу
        for row in array2:
            file.write(','.join(map(str, row)) + '\n')

# Считывание двумерного массива из файла
def read_2d(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        array1 = []
        array2 = []
        current_array = array1  # Начинаем считывание в первую матрицу
        for line in lines:
            if line.strip() == '':  # Если встречаем пустую строку
                current_array = array2  # Переходим к считыванию второй матрицы
                continue
            current_array.append([float(num) for num in line.strip().split(',')])
        return array1, array2

# 2.2 Нахождение среднего арифметического элементов k-й строки
def average_of_kth_row(array, k):
    if k < 0 or k >= len(array):
        return None  # Проверяем, что k находится в пределах массива
    row = array[k]
    if not row:
        return None  # Проверяем, что строка не пустая
    return sum(row) / len(row)  # Считаем среднее арифметическое

# 2.3 Умножение матриц N*N. Результат записать в файл
def matrix_multiply(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return None  # Проверяем, что матрицы имеют одинаковый размер
    result = [[0 for _ in range(len(matrix1))] for _ in range(len(matrix1))]  # Создаем пустую матрицу-результат
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Выполняем умножение
    return result

# 2.4 Сложение двух матриц N*N. Результат записать в файл
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Проверяем, что матрицы имеют одинаковый размер
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# Размерность массива
N = 10

# Создание двух матриц
array1 = create_2d(N)
array2 = create_2d(N)

# Запись двух матриц в файл
write_2d("text2.txt", array1, array2)
print("Двумерные массивы сохранены в файл text2.txt")

# 2.2 Считывание матриц из файла
array_from_file1, array_from_file2 = read_2d("text2.txt")

k = int(input("Введите номер строки: "))
average1 = average_of_kth_row(array_from_file1, k)

if average1 is not None:
    print(f"Среднее арифметическое всех элементов {k}-й строки первой матрицы: {average1}")
else:
    print(f"Строки с индексом {k} не существует в первой матрице")

# 2.3 Умножение матриц
result_matrix = matrix_multiply(array_from_file1, array_from_file2)
if result_matrix is not None:
    with open("result.txt", 'w') as file:
        for row in result_matrix:
            file.write(','.join(map(str, row)) + '\n')
    print("Результат умножения матриц записан в файл result.txt")
else:
    print("Матрицы не могут быть умножены из-за несовпадения размеров")

# 2.4 Сложение матриц
result_matrix_addition = matrix_addition(array_from_file1, array_from_file2)
if result_matrix_addition is not None:
    with open("result2.txt", 'w') as file:
        for row in result_matrix_addition:
            file.write(','.join(map(str, row)) + '\n')
    print("Результат сложения матриц записан в файл result2.txt")
else:
    print("Матрицы не могут быть сложены из-за несовпадения размеров")
