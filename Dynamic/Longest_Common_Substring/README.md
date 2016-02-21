Given two strings find the longest common substring

Is any of the strings is null, the LCS will be zero

If both chars are same. 
  LCS[i][j] = LCS[i][j] + 1

else:
  LCS[i][j] = 0


