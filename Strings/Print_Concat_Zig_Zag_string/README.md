Print concatenation of zig zag string in 'n' rows

Given a string and number of rows 'n'. Print the string formed by concatenating n rows when input string is written in row wise zig zag order. 

Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G   
  B   D   F   H
Now concatenate the two rows and ignore spaces 
in every row. We get "ACEGBDFH"

Input: str = "GEEKSFORGEEKS"
       n = 3
Output: GSGSEKFREKEOE
Explanation: Let us write input string in Zig-Zag fashion
             in 3 rows.
G       S       G       S
  E   K   F   R   E   K
    E       O       E
Now concatenate the two rows and ignore spaces 
in every row. We get "GSGSEKFREKEOE"
