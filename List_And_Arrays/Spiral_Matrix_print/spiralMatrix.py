def spiralPrint(matrix):
  minrow = 0
  maxrow = len(matrix) - 1
  mincol = 0
  maxcol = len(matrix[0]) - 1
  row = 0
  col = 0
  state = 'right'
  solutions = list()
  while len(solutions) < len(matrix) * len(matrix[0]):
    solutions.append(matrix[row][col])
    if state == 'right':
      if col < maxcol:
        col += 1
      else:
        state = 'down'
        row += 1
        minrow += 1
    elif state == 'down':
      if row < maxrow:
        row += 1
      else:
        state = 'left'
        col -= 1
        maxcol -= 1
    elif state == 'left':
      if col > mincol:
        col -= 1
      else:
        state = 'up'
        row -= 1
        maxrow -= 1 
    elif state == 'up':
      if row > minrow:
        row -= 1
      else:
        state = 'right'
        col += 1
        mincol += 1
  print solutions


temp = [[1, 2, 3, 4], [5, 6,7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
spiralPrint(temp)
spiralPrint([[1, 2, 3], [4, 5, 6], [7, 8, 9]])     
