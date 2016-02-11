"""
 Im just going to use lists instead of linked lists
"""

"""
	 1
     2       3
   4   5   6   7
  8 9 1 2 4 5 2 1

"""

makeLists(node, list_set = list(), level=1): 
  if node != None:
    if len(list_set) < level:
      list_set.append([])
      list_set[-1].append(node.value)
    else:
      list_set[level-1].append(node.value)
    list_set = makeLists(node.left, list_set, level+1)
    list_set = makeLists(node.right, list_set, level+1)
  return list_set
