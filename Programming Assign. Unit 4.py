
def is_divisible(x, y): # from Think Python Book
  return x % y == 0
def is_power(a, b):# is_power function

    if b == a: # if the numbers are equal 
        return True
    elif not is_divisible(a,b) : # call is_divisible function 
      return False 
    elif b == 1: # if the second number equal with 1
        return False
    return is_power(int(a/b), b) # call  itself


print("is_power(10, 2) returns: ", is_power(10, 2)) # test case 1 
print("is_power(27, 3) returns: ", is_power(27, 3)) # test case 2 
print("is_power(1, 1) returns: ", is_power(1, 1)) # test case 3 
print("is_power(10, 1) returns: ", is_power(10, 1)) # test case 4 
print("is_power(3, 3) returns: ", is_power(3, 3)) # test case 5


---------------------------------
is_power(10, 2) returns:  False
is_power(27, 3) returns:  True
is_power(1, 1) returns:  True
is_power(10, 1) returns:  False
is_power(3, 3) returns:  True
---------------------------------