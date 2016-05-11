Given an expression with only '}' and '{' so that the expression becomes balanced, the balanced expresion is '{}'


An Efficient Solution can solve this problem in O(n) time. The idea is to first remove all balanced part of expression. For example, convert “}{{}}{{{” to “}{{{” by removing highlighted part. If we take a closer look, we can notice that, after removing balanced part, we always end up with an expression of the form }}…}{{…{, an expression that contains 0 or more number of closing brackets followed by 0 or more numbers of opening brackets.

How many minimum reversals are required for an expression of the form “}}..}{{..{” ?. Let m be the total number of closing brackets and n be the number of opening brackets. We need ⌈m/2⌉ + ⌈n/2⌉ reversals. For example }}}}{{ requires 2+1 reversals.
