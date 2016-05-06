import string
def reverseNoSpecial(stringOne):
  stringOne = list(stringOne)
  start = 0
  end = len(stringOne) - 1
  letters = string.letters
  while stringOne[start] not in letters:
      start += 1
  while stringOne[end] not in letters:
      end -= 1
  while start < end:
    if stringOne[start] in letters and stringOne[end] in letters:
      stringOne[start], stringOne[end] = stringOne[end], stringOne[start]  
      start += 1
      end -= 1
    else:
      if stringOne[start] not in letters:
        start += 1
      else:
        end -= 1
  return ''.join(stringOne)

print reverseNoSpecial('m$ihi%r')
print reverseNoSpecial('w$')
