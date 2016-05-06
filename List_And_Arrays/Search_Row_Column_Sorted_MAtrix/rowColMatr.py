def rowColMatrix(matrix, value):
  row = 0
  col = len(matrix[row]) - 1
  while row < len(matrix) and col > 0:
    #print matrix[row][col]
    if matrix[row][col] ==  value:
      return value
    elif matrix[row][col] > value:
      col -= 1
    elif matrix[row][col] < value:
      row += 1
  return False


matrix = [[10, 20, 30, 40],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
print rowColMatrix(matrix, 29)
