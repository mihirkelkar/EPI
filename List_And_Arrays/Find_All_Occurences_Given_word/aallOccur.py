def findAllOccur(matrix, row, col, string_one, path = []):
  if string_one == '':
    return 
  if (row<len(matrix) and row>=0) and  (col<len(matrix[0]) and col>=0):
    if matrix[row][col] == string_one[0]:
      if len(string_one) == 1:
        print path + [(row, col)]
      else:
        for ii in [-1, 0, 1]:
          for jj in [-1, 0, 1]:
            if ii == 0 and jj == 0:
              continue
            else:
              findAllOccur(matrix,row+ii,col+jj,string_one[1:], path + [(row, col)])



def main():
  mat = [
          ['B', 'N', 'E', 'Y', 'S'],
          ['H', 'E', 'D', 'E', 'S'],
          ['S', 'G', 'N', 'D', 'E']
        ]
  string = 'DES'         
  for row in range(0, len(mat)):
    for col in range(0, len(mat[0])):
      if mat[row][col] == string[0]:
        findAllOccur(mat, row, col, string)
      
if __name__ == "__main__":
  main()    
    
  

