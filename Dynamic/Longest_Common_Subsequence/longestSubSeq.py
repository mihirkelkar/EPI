def longSub(string_one, string_two):
  lcs = list()
  solution = list()
  for ii in range(0, len(string_one)+1):
    lcs.append([0] * (len(string_two)+1))
    solution.append([None] * (len(string_two)+1))
  for ii in range(1, len(lcs)):
    for jj in range(1, len(lcs[0])):
      if string_one[ii - 1] == string_two[jj - 1]:
        lcs[ii][jj] = lcs[ii - 1][jj - 1] + 1
        solution[ii][jj] = 'diag'
      else:
        if lcs[ii - 1][jj] > lcs[ii][jj - 1]:
          lcs[ii][jj] = lcs[ii - 1][jj]
          solution[ii][jj] = 'up'
        else:
          lcs[ii][jj] = lcs[ii][jj - 1]
          solution[ii][jj] = 'left'
  string_buffer = ''
  while ii > 0 and jj > 0:
      if solution[ii][jj] == 'diag':
        string_buffer += string_one[ii - 1]
        ii -= 1
        jj -= 1
      elif solution[ii][jj] == 'up':
        ii -= 1
      elif solution[ii][jj] == 'left':
        jj -= 1
  for ii in lcs:
    print ii
  print "The longest common subseq is %s" %string_buffer

longSub('acbdea', 'abcda')
