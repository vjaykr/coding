def multiplyMatrix(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# giving the valuer for the matrix
matrix1 = [[1, 2], [4, 5]]
matrix2 = [[7, 8], [9, 10]]

# Call the function with sample dataa
result = multiplyMatrix(matrix1, matrix2)
print(result)



matrix1 = [[1, 2], [4, 5]]
matrix2 = [[7, 8], [9, 10]]
























# def multiply_matrix(matrix1, matrix2):
#     # Number of rows and columns for result matrix
#     rows1, cols1 = len(matrix1), len(matrix1[0])
#     rows2, cols2 = len(matrix2), len(matrix2[0])
    
#     # Initialize the result matrix with zeros
#     result = [[0] * cols2 for _ in range(rows1)]
    
#     # Perform matrix multiplication
#     for i in range(rows1):
#         for j in range(cols2):
#             result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1))
    
#     return result

# # Define the matrices
# matrix1 = [[1, 2], [4, 5]]
# matrix2 = [[7, 8], [9, 10]]

# # Call the function with the matrices
# result = multiply_matrix(matrix1, matrix2)
# print(result)
# # print(len(matrix1))
# # print(len(matrix2))
# # print(len(matrix1[0]))
# # print(len(matrix2[0]))