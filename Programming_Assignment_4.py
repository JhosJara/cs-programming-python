alphabet = "abcdefghijklmnopqrstuvwxyz"   
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

#PART 1

def has_duplicates(word):
    """Takes a str praramter and returns True if the string has any repeated character"""
    temp = histogram(word) 
    temp_list = temp.values()#Get the values of the dictionary created by histogram function

    counter = 0 #Counts how many duplicates there are in the string

    for j in temp_list:
        if j != 1: #Evaluates the values of the dictionary to find duplicates
                counter=+1
      
    if counter > 0:
        return True

    else:
        return False


#Loop to traverse test_dup
print('Output: Part 1')
for i in test_dups:
    res = has_duplicates(i)
    if res == True:
        print(i, " has duplicates")
    else:
        print(i, " has no duplicates")
        
print('\n')





#PART 2
def missing_letters(word):
    """ Takes a string parameter and returns anew string with all the letters of the alphabet
    that are not in the argument string"""

    temp = histogram(word)#Get the letters in the argument
    res = ''
    for j in alphabet:
        if j not in temp:#Evaluates in each letter in the dictionary keys
                res = res + j #if it is not in the histogram, it concatenates to res

    return res 

              
                
#Loop to traverse test_miss
print('Output: Part 2')
for i in test_miss:
    res = missing_letters(i)
    if res != '':
        print(i,' is missing letters',res)

    else:
        print(i,' is no missing letters')

        

            
            
