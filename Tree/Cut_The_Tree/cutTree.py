import sys
def main():
  #temp = list()
  #temp = sys.stdin.readlines()
  temp = ['6', '100 200 100 500 100 600', '1 2','2 3','2 5','4 5', '5 6']
  enter_list = temp[2::]
  x_list = [int(x.split(" ")[0]) for x in enter_list]
  y_list = [int(x.split(" ")[1]) for x in enter_list]
  change = list()
  for ii in range(0, len(x_list)):
    if x_list[ii] in y_list:
      pass
    else:
      if x_list[ii] == 1:
        pass
      else:
        change.append(ii)
  for ii in change:
    x_list[ii], y_list[ii] = y_list[ii], x_list[ii]
  temp_dict = {}
  for ii in range(0, len(x_list)):
      try:
        temp_dict[x_list[ii]] = temp_dict[x_list[ii]] + [y_list[ii]]
      except:
        temp_dict[x_list[ii]] = [y_list[ii]] 
  print temp_dict
  vals = [int(x) for x in temp[1].split(" ")]
  print vals
  for ii in range(0, len(x_list)):
    x = x_list[ii]
    y = y_list[ii]
    new_list = rem(y,temp_dict)
    #just replace this with the appropriate minus statement and we're done. 
    #print sum(vals) - new_sum(new_list, vals)
    
def rem(num , dict):
  list = []
  try:
    list = dict[num] 
  except:
    pass
  for ii in list:
      list += rem(ii, dict)
  return list
    
def new_sum(new_list, vals):
  sum = 0
  for ii in new_list:
    print ii
    sum += vals[ii - 1]
  return sum

main()

