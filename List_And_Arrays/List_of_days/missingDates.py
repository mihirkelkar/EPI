from datetime import date, timedelta as td
def missingDates(array):
  #The array is of format mm-dd-yyyy
  #Lets split it into array of tuples
  array = [ii.split("-") for ii in array]
  
  #Sort this array
  sorted_array = sorted(array, key = lambda x: (int(x[2]), int(x[1]), int(x[0])))
  sorted_array = [date(int(ii[2]), int(ii[0]), int(ii[1])) for ii in sorted_array]
  for ii in range(1, len(sorted_array)):
    delta = sorted_array[ii] - sorted_array[ii - 1]
    for jj in range(delta.days + 1):
      print sorted_array[ii-1] + td(days=jj)

missingDates(['02-25-1992', '01-25-1992', '10-01-2001'])

