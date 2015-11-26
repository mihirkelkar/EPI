def permutations(string):
  new_ret_list = list()
  if len(string) > 1:
    ret_list = list(set(permutations(string[1:])))
    for word in ret_list:
      for index in range(0, len(word) + 1):
        new_ret_list.append(word[:index] + string[0] + word[index:])
    return new_ret_list
  else:
    return [string]



print permutations("abc")  
print permutations("mihir")
