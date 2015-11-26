def make_larger_number(number):
  number = [int(char) for char in str(number)]
  current_pos = len(number) - 2
  smallest_so_far = current_pos + 1
  while (number[current_pos] >= number[current_pos + 1]) and (current_pos >= 0):
    #print number[current_pos]
    if number[current_pos] < number[smallest_so_far]:
      smallest_so_far = current_pos
    current_pos -= 1
  if current_pos >= 0:
    print number
    number[current_pos], number[smallest_so_far] = number[smallest_so_far], number[current_pos]
    temp = number[current_pos + 1:]
    temp.sort()
    print number[:current_pos + 1] + temp
make_larger_number(12543)
