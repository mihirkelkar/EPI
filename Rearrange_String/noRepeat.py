def noRepeat(theString):
  #assuming no spaces, punctuations and all lower case. 
  string_dict = {}
  for char in theString:
    try:
      string_dict[char] += 1
    except:
      string_dict[char] = 1
  maxNum = max(string_dict.values())
  if maxNum > (len(theString) + 1) / 2:
    return False
  else:
    new_array = ["" for ii in range(0, len(theString))]
    items = sorted(string_dict.items(), key = lambda ii: -ii[1])
    off_set = 0
    index = 0
    #print items
    cur_char = items.pop(0)
    cur_char_count = cur_char[1]
    for ii in range(0, len(theString) + 1):
      if index < len(theString):
        if cur_char_count > 0:
          pass
        else:
          cur_char = items.pop(0)
          cur_char_count = cur_char[1]
        new_array[index] = cur_char[0]
        cur_char_count -= 1
        #print index, 
        #print cur_char[0]
        #print cur_char_count
        #print "--------------"
        index += 2
      else:
        index = new_array.index("") 
    return "".join(new_array)    

print noRepeat("aab")
print noRepeat("mihir")
print noRepeat("google")
