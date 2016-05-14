Find all occurences of a given word on a matrix. 

Given a 2D grid of characters and a word, find all occurrences of given word in grid. A word can be matched in all 8 directions at any point. Word is said be found in a direction if all characters match in this direction (not in zig-zag form).

The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up, Vertically Down and 4 Diagonals.

Input:
mat[ROW][COL]= { {'B', 'N', 'E', 'Y', 'S'},
     	         {'H', 'E', 'D', 'E', 'S'},
	         {'S', 'G', 'N', 'D', 'E'}
               };
Word = “DES”

Output:
D(1, 2) E(1, 1) S(2, 0) 
D(1, 2) E(1, 3) S(0, 4) 
D(1, 2) E(1, 3) S(1, 4)
D(2, 3) E(1, 3) S(0, 4)
D(2, 3) E(1, 3) S(1, 4)
D(2, 3) E(2, 4) S(1, 4)


