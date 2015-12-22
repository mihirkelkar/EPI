Given an input string and a dictionary of words, find out if the input string can be segmented into a space separated sequence of dictionary words. 

eg. Lets the dictionay words be {i, like, sam, sung, samsung, mobile, ice, cream, icecream}

Input: ilike
output : True
coz i + like

Input: ilikesamsung
output: True
coz: i+like+samsung and i+like+sam+sung

The idea of implementation is simple, we consider each prefix and search it in
dictionary. If the prefix is present in dictionary, we recur for rest of the string (suffix). If the recursive call for suffix returns true, we return true. 
If we have tried all prefixes and none of them resulted in a solution , we return false. 


