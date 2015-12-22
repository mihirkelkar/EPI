word_dict = ['i', 'like', 'sam', 'sung', 'samsung', 'ice', 'cream', 'icecream']

def wordBreak(word):
  if len(word) == 0:
    return True
  vec = [False for ii in word]
  #Vec[ii] is set to True if string from 0 to ii included is present in word_dict.
  for ii in range(0, len(word)):
    print vec
    print "------------"
    if not vec[ii] and (word[0:ii+1] in word_dict):
      vec[ii] = True
    if vec[ii]:
      #Check if ii+1 
      for jj in range(ii+1, len(word)):
        print word[ii+1:jj+1]
        if not vec[jj] and (word[ii+1:jj+1] in word_dict):
          vec[jj] = True
        if (jj == len(word)-1) and vec[jj] == True:
          return True
  return False

print wordBreak('ilike')
print wordBreak('samsung')
print wordBreak('google')
