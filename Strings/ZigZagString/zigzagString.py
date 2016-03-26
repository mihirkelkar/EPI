def zigzagString(string, rows):
  new_list = [[] * ii for ii in range(rows)]
  index = 0
  counter = 0
  flag = True
  while counter < len(string):
    if index == 0 or index == rows-1:
      flag = not flag
    else:
      if flag:
        for ii in range(0, index):
          new_list[ii].append(" ")
        for ii in range(index+1, rows):
          new_list[ii].append(" ")  
    new_list[index].append(string[counter])
    if flag:
      index -=1  
    else:
      index += 1
    counter += 1
  print '\n'.join([' '.join(ii) for ii in new_list])

zigzagString('paypalishiring', 3)
zigzagString('leetcodeishiring', 4)  
  
