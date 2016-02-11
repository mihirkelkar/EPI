def checkBalanced(node):
  if node == None:
    return -1
  
  left_height = checkBalanced(node.left)
  if left_height == False:
    return False
  right_height = checkBalanced(node.right)
  if right_height == False:
    return False
  if math.abs(left_height - right_height) > 1:
    return False
  return max(left_height, right_height) + 1
