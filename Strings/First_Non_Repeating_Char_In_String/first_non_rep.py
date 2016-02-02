def first_non_rep(string):
  word_dict = {}
  for index, ii in enumerate(string):
    try:
      temp = word_dict[ii]
      new_temp = [temp[0], temp[1] + 1]
      word_dict[ii] = new_temp
    except:
      word_dict[ii] = [index, 1]
  #print word_dict.values()
  for ii in sorted(word_dict.values(), key = lambda x: x[0]):
    if ii[1] == 1:
      return string[ii[0]]

print first_non_rep('mihir')
