def zigzag(string_one, number):
  new_string = [''] * number
  direction = 'down'
  counter = 0
  num_count = 0
  while counter < len(string_one):
    new_string[num_count] = new_string[num_count] + string_one[counter]
    if direction == 'down':
      if num_count == number - 1:
        direction = 'up'
        num_count -= 1
      else:
        num_count += 1
    elif direction == 'up':
      if num_count == 0:
        direction = 'down'
        num_count += 1
      else:
        num_count -= 1
    counter += 1
  return ''.join(new_string)

print zigzag('abcdefgh',2)
print zigzag('geeksforgeeks',3)
