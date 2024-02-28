
# traditional matrix multiplication
def mm(first, second):
    operations_count = 0

    sum = 0
    SIZE = len(first)
    multiply = [[0] * SIZE] * SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                sum += first[i][k] * second[k][j]
                operations_count += 1 # addition and multiplication
            multiply[i][j] = sum
            sum = 0
    return multiply, operations_count
    


if __name__ == "__main__":
    first = [[0,1,2], [0,0,1], [2,1,0]]  # Matrix examples
    second = [[0,0,1], [1,0,0], [0,1,0]] 
    result = mm(first, second)
    for row in result:
        print(row)