import string

def work_on_letter(string_one):
  return "".join([char.lower() for char in string_one if char in string.letters])

def sorting_method(string_one, string_two):
  strings = [string_one, string_two]
  strings = [work_on_letter(ii) for ii in strings]
  if sorted(strings[0]) == sorted(strings[1]):
    return True
  return False

def hash_method(string_one, string_two):
  temp = {}
  strings = [string_one, string_two]
  strings = [work_on_letter(ii) for ii in strings]
  for ii in strings[0]:
    if ii in temp:
      temp[ii] += 1
    else:
      temp[ii] = 0
  for jj in strings[0]:
    if ii not in temp:
      return False
    else:
      temp[ii] -= 1
  if sum(temp.values()) > 0:
    return False
  return True

print sorting_method("rAceCar", "racecar")
print hash_method(" RACECAR, ", "rcaacre")
