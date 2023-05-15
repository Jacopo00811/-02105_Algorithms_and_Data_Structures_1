def bin(x):
    if x == 0:
        return "0"
    s = ""
    while x:
        s = str(x % 2) + s
        x //= 2
    return s
"""
The line 7, x //= 2 is an in-place operator that updates the value of x by dividing it by 2 using integer division. 
The // operator returns the result of integer division, discarding the remainder and always rounding down to the nearest integer.
For example, if x = 5, the first time this line is executed, x will be updated to x = 5 // 2 = 2. The next time, x will be updated 
to x = 2 // 2 = 1. Finally, x will be updated to x = 1 // 2 = 0. By dividing x by 2 repeatedly and storing the remainders, 
we are able to construct the binary representation of x as a string.
"""

