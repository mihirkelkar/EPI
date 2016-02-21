def findLCS(string_a, string_b):
    matrix = list()
    for ii in range(0, len(string_b)+1):
      new_list = list()
      for jj in range(0, len(string_a)+1):
        new_list.append(None)
      matrix.append(new_list)
    for ii in range(0, len(matrix)):
      matrix[ii][0] = 0
    matrix[0] = [0] * len(matrix[0])
    result = 0
    for ii in range(1, len(matrix)):
      for jj in range(1, len(matrix[0])):
        if string_b[ii - 1] == string_a[jj - 1]:
          matrix[ii][jj] = matrix[ii - 1][jj - 1] + 1
          result = max(result , matrix[ii][jj])
        else:
          matrix[ii][jj] = 0
    for ii in matrix:
      print ii
    return result
 
print findLCS("mihir", "mih")

  
