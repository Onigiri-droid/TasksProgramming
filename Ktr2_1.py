import random


# Создание массива случайных чисел
def create(size, datatype):
    if datatype == 'int':
        return [random.randint(-10, 10) for _ in range(size)]
    elif datatype == 'float':
        return [random.uniform(-10, 10) for _ in range(size)]


# Запись массивов в файл
def write(file_name, arrays):
    with open(file_name, 'w') as file:
        for array in arrays:
            file.write(str(array) + '\n')


# Считывание массивов из файла
def read(file_name, datatype):
    arrays = []
    with open(file_name, 'r') as file:
        for line in file:
            if datatype == 'int':
                array = [int(float(num.strip())) for num in line.strip()[1:-1].split(',')]
            elif datatype == 'float':
                array = [float(num.strip()) for num in line.strip()[1:-1].split(',')]
            arrays.append(array)
    return arrays


# Вывод элементов массива
def inference(array):
    with_plus = [num for num in array if num > 0]
    with_minus = [num for num in array if num < 0]

    print(array)
    print("Положительные элементы массива:")
    print(with_plus)

    print("Отрицательные элемент массива:")
    print(with_minus)
    print()


# Операции между элементами массивов
def addition(array1, array2):
    return [a + b for a, b in zip(array1, array2)]


def subtraction(array1, array2):
    return [a - b for a, b in zip(array1, array2)]


def multiplications(array1, array2):
    return [a * b for a, b in zip(array1, array2)]


# Сортировка массива
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# Сортировка выбором
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


# Сортировка вставками
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# Быстрая сортировка
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Встроенная функция сортировки
def builtin_sort(array):
    return sorted(array)


# Основной код
choice = input("Введите '1' для считывания массивов из файла или '2' для создания новых массивов: ")
datatype = input("Введите 'int' для целых чисел или 'float' для вещественных чисел: ")
if choice == '2':
    array1 = create(10, datatype)
    array2 = create(10, datatype)

    write("text.txt", [array1, array2])
    print("Новые массивы сохранены в файл text.txt")

arrays = read("text.txt", datatype)

if arrays and len(arrays) == 2:
    print("Первый массив:")
    inference(arrays[0])

    print("Второй массив:")
    inference(arrays[1])

# 1.2 Операции между элементами массивов
print("операции между элементами массивов 1.2:")
print("Результат сложения массивов:")
print(addition(arrays[0], arrays[1]))
print("Результат вычитания массивов:")
print(subtraction(arrays[0], arrays[1]))
print("Результат умножения массивов:")
print(multiplications(arrays[0], arrays[1]))
print()

# 1.3 Сортировка
print("Сортировка массивов по возрастанию 1.3:")
print("а) Пузырьком:", bubble_sort(arrays[0].copy()))
print("б) Сортировка выбором:", selection_sort(arrays[1].copy()))
print("в) Сортировка вставками:", insertion_sort(arrays[0].copy()))
print("г) Быстрая сортировка:", quick_sort(arrays[1].copy()))
print("д) Встроенная функция sort:", builtin_sort(arrays[1].copy()))