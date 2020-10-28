# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    matrix = []

    def __init__(self, matrix = str):
        self.matrix = matrix

    def __str__(self):
        for x in self.matrix:
            for y in x:
                print(y, end=' ')
            print()

    def __add__(self, other_matrix = str):
        new_matrix = []
        i = 0
        j = 0
        while i < len(self.matrix):
            line = []
            while j < len(self.matrix[i]):
                line.append(self.matrix[i][j] + other_matrix.matrix[i][j])
                j += 1
            new_matrix.append(line)
            i += 1
            j = 0
        return new_matrix


first_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_matrix = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])


print(first_matrix + second_matrix)