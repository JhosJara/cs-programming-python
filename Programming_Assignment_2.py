def is_divisible(x,y):#Function retrieved from section 6.4 of the Python textbook
    if x % y == 0:
        return True
    else:
        return False

def is_power(number,power):
    """Evaluates if the 'power' argument is power of 'number'"""
    if is_divisible(number,power):
        if number==power: #Base case to evaluate when the base and the power are equal
            return True
        elif power==1 and number!=1: #Base case for power of 1
            return False
        else:
            recurse=number/power
            if recurse>1:
                return is_power(recurse,power)#is_power recursive call
            else:
                return True
    else:
        return False
    
#Test cases of  the is_power function   
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))


