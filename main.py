# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def multiply_matrix(a, b):
    sum = 0
    temp = []
    c = []
    if len(b) != len(a[0]):
        print("Matrixes are not mutual")
        return
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j]
            temp.append(sum)
            sum = 0
        c.append(temp)
        temp = []
    return c

    # Press Ctrl+F8 to toggle the breakpoint.


def output_matrix(c):
    for i in range(len(c)):
        print('|', *c[i], sep='\t', end='\t|\n')


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    matrixA = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [9, 8, 7, 6, 5],
               [4, 3, 2, 1, 0],
               [5, 6, 7, 8, 9]]
    matrixB = [[1, 2, 3, 4],
               [6, 7, 8, 9],
               [9, 8, 7, 6],
               [4, 3, 2, 1],
               [5, 6, 7, 8]]
    matrixC = multiply_matrix(matrixA, matrixB)

    output_matrix(matrixC)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
