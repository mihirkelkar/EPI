def url(string, length):
  string = list(string)
  #Count number of spaces
  space_count = 0
  ii = 0
  while ii < length:
    if string[ii] == ' ':
      space_count += 1
    ii += 1
  new_length = length + 2 * space_count

  #start iterating from the end of the string list, 
  #if its a legitimate char move it to the last unfilled index
  #if its a space then add %20 to three cols in the last unfilled indexes

  new_index = new_length - 1

  ii = length - 1
  while ii >= 0:
    if string[ii] == ' ':
      string[new_index] = '0'
      string[new_index - 1] = '2'
      string[new_index - 2] = '%'
      new_index -= 3
    else:
      string[new_index] = string[ii]
      new_index -= 1
    ii -= 1
  
  print ''.join(string)
  
url("Mr John Smith    ",13)  
