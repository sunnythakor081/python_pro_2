def initializeMatrix(row,col,value):
    if row*col != len(value):
        print("Value is Missing")
        return
    item=0
    matrix = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(value[item])
            item+=1
        matrix.append(row)
    
    return matrix

def printMatrix(matrixPass):
    for row in matrixPass:
        for col in row:
            print(col,end="   ")
        print()