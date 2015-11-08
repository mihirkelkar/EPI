Given a string of opening and closing paranthesis, check whether it's balanced. We have  types of parantheis. Check whether the string is well formatted and has balanced paranthesis. 

Go from left to right and push the closing braces onto a stack. 

Now, go from left to right again and for every opening paran, pop the stack. 
If the type of parans match move on, else return false. 

The stack should be empty by the end of the string parse. 
