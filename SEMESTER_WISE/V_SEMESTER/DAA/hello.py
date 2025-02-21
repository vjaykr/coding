matrix1 = [[1, 2], [4, 5]]
matrix2 = [[7, 8], [9, 10]]

p = (matrix1[0][0] + matrix1[1][1]) * (matrix2[0][0] + matrix2[1][1])
q = (matrix1[1][0] + matrix1[1][1]) * matrix2[0][0]
r = matrix1[0][0] * (matrix2[0][1] - matrix2[1][1])
s = matrix1[1][1] * (matrix2[1][0] - matrix2[0][0])
t = (matrix1[0][0] + matrix1[0][1]) * matrix2[1][1]
u = (matrix1[1][0] - matrix1[0][0]) * (matrix2[0][0] + matrix2[0][1])
v = (matrix1[0][1] - matrix1[1][1]) * (matrix2[1][0] + matrix2[1][1])

c11 = p + s - t + v
c12 = r + t
c21 = q + s
c22 = p + r - q + u

result = [[c11, c12], [c21, c22]]
print(result)
