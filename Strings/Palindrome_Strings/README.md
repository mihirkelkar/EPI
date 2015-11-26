Given two strings, check whether the two strings are composed of the same exact letters ignoring capitalization, spacing, punctuation. Each letter should have the same count in both strings. 

Method 1: Lower case and sort both strings. If they match perfectly. They are anagrams. 

Time Complexity : O(nLogn) for the sort. 

Method 2: Add entries for string one to a hash table and maintain count. 

Subtract counts as you traverse through the second string. If all counts for letters end up being zero. Its a perfect match. 

Time Complexity : O(n) for time and O(n) in Memory 
