alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 
 
 
def has_duplicates(s):
    h = histogram(s)
    for values in histogram(s).values():
        if values>1:
            return True
    return False
#to implement the has_duplicates
for str_1 in test_dups:
    if has_duplicates(str_1):
        print(str_1,'has duplicates')
    else:
        print(str_1,'has no duplicates')
        

def missing_letters(str_2):
        missings = [ ] #missing takes an empty list
        dict_2 = histogram(str_2)
        for missing in alphabet:
            if missing not in dict_2:
                missings .append(missing)
        missings . sort()
        return str(missings)
for miss_let in test_miss:         
            str_3 = missing_letters(miss_let.replace(" " ," "))           
            if str_3 == " ":             
                print(miss_let,"is missing letters", str_3)
            else:
              print(miss_let,"uses all the letters")
