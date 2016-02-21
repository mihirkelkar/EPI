def subset_sum(array, k):
  matrix = list()
  for ii in range(0, len(array)+1):
    matrix.append([None] * (len(array)+1))
  array = [0] + array
  for ii in range(0, len(matrix)):
    matrix[ii][0] = True

  for jj in range(1, len(matrix)):
    matrix[0][jj] = False

  for ii in range(1, len(matrix)):
    for jj in range(1, len(matrix)):
      if jj - array[ii] >= 0:
        matrix[ii][jj] = matrix[ii - 1][jj] or matrix[ii - 1][jj - array[ii]]
      else:
        matrix[ii][jj] = matrix[ii - 1][jj]
  return matrix[-1][-1]

print subset_sum([1, 3, 9, 2], 4)
