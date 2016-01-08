def partitionIntoAnagrams(array):
  anagramMap = {}
  for ii in array:
    try:
      anagramMap[''.join(sorted(ii))] += [ii]
    except:
      anagramMap[''.join(sorted(ii))] = [ii]
  #print anagramMap
  return [string for sublist in  anagramMap.values() for string in sublist]

array = ['elvis', 'silent', 'debitcard', 'lives', 'listen', 'badcredit']
print partitionIntoAnagrams(array)
