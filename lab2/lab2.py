import numpy as np


def gauss_elimination_1(matrix, v):
    n = len(matrix)
    # Skalowanie macierzy, aby uzyskać 1 na przekątnej
    for i in range(n):
        divisor = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= divisor
        v[i] /= divisor
    # Eliminacja wierszy pod przekątną
    for i in range(n):
        for j in range(i + 1, n):
            multiplier = matrix[j][i]
            for k in range(n):
                matrix[j][k] -= multiplier * matrix[i][k]
            v[j] -= multiplier * v[i]
    # Rozwiązanie układu równań z macierzą trójkątną górną
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = v[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
    return x
    

def gauss_elimination_with_pivot(matrix, v):
    n = len(matrix)
    
    # Częściowy pivoting
    for i in range(n):
        max_index = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_index][i]):
                max_index = k
        matrix[[i, max_index]] = matrix[[max_index, i]]  # Swap rows in matrix
        v[[i, max_index]] = v[[max_index, i]]  # Swap elements in v
        # Eliminacja wierszy pod przekątną
        for j in range(i + 1, n):
            multiplier = matrix[j][i]
            for k in range(n):
                matrix[j][k] -= multiplier * matrix[i][k]
            v[j] -= multiplier * v[i]
    # Rozwiązanie układu równań z macierzą trójkątną górną
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = v[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
    return x


if __name__ == "__main__":
    birthday_number = 3
    matrix = np.random.randint(-9, 9, size=(birthday_number, birthday_number))
    v = np.random.randint(-9, 9, size=birthday_number)

    print(f"Wylosowana macierz:\n{matrix}\nWylosowany wektor: {v}\n")

    # Algorytm eliminacji Gaussa generujący 1 na przekątnej
    x1 = gauss_elimination_1(matrix, v)
    print(f"Wektor wynikowy: x={x1}")
    x2 = gauss_elimination_with_pivot(matrix, v)
    print(f"Wektor wynikowy: x={x2}")
    

