def str_rev(string):
  start = 0
  end = len(string)-1
  string = list(string)
  while start < end:
    string[start], string[end] = string[end], string[start]
    start += 1
    end -= 1

  start = counter = 0
  while counter <= len(string):
    if counter != len(string) and string[counter] != ' ':
      counter += 1
    else:
      end = counter - 1
      while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
      counter += 1
      start = counter

  print ''.join(string)

str_rev('mihir kelkar')
