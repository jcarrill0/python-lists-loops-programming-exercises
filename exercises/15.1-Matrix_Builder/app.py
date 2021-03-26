#Import random

#Create the function below:
def matrixBuilder(num):
    # matriz = [None] * num # [[1, 1, 1], [], ...]
    # for i in range(num):
    #     matriz.append([])
    #     for j in range(num):
    #         matriz[i].append(1)
    # for i in range(num):
    #     matriz[i] = [1] * num
    matriz = [[1] * num for i in range(num)]
    return matriz

print(matrixBuilder(8))