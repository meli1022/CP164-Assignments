"""
------------------------------------------------------------------------
Functions
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-15"
------------------------------------------------------------------------
"""



def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    
  
    diff_list = [] 
  
    for i in range(1, len(a)): 
        diff_list.append(a[i] - a[i-1]) 

    for i in range(1,len(diff_list)):
        if diff_list[i]>=diff_list[i-1]:
            md = diff_list[i]
        else:
            md = diff_list[i-1]
    return md

def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """


    for i in name:
        if name[0].isdigit():
            valid = False
        elif i is ("_") or i.isalnum():
            valid = True
        else:
            valid = False
    return valid
        
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = arix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    
    total = 0
    counter = 0 
    small = a[0][0]
    large = a[0][0]
    
    for x in a:
        for y in x:
            if y < small: 
                small = y 
            if y > large:
                large = y
            counter += 1
            total += y
    average = total / counter
    return small, large, total, average 

def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = arix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    
    b = []
    for i in a:
        for j in i:
            b.append(j)
    return b

def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of arixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = arixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the arix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    
    c = []
    list_ans = []

    for x in range(len(a)):
        for y in range(len(a[0])):
            list_ans.append(a[x][y]+b[x][y])
    
    for i in range (0, len(list_ans),len(a[0])):
        c.append(list_ans[i:i+len(a[0])])
    
    return c

def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = arixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the arix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = [[0 for i in range(len(a[0]))]for j in range (len(a))]
   
    for i in range(len(a)):

        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D arix rotated to the right.
    a must be unchanged.
    Use: b = arix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    
    row = len(a)
    col = len(a[0])
    b = []
   
    for i in range(col):
        b.append([])
        for x in range(row):
            b[i].append(0)
    for i in range(row):
        for x in range(col):
            newrow = row - i -1
            b[x][newrow] = a [i][x]
            
    return b
  
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    
    u, l, d, w, r = 0, 0, 0, 0, 0
    
    for i in fv.read():
        if i.isupper():
            u+=1
        elif i.islower():
            l += 1
        elif i.isdigit():
            d += 1
        elif i == " ":
            w += 1
        else:
            r += 1
    return u, l, d, w, r

def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    
    VOWELS = ['a','e','i','o','u']
    out = ""
    for i in range(len(s)):
        if s[i]not in VOWELS:
            out += s[i]
    return out

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ""
    VOWELS = "aeiou"
    isCap = False
    if not word[0].islower():
        isCap = not isCap
        
    if word[0] in VOWELS:
        pl = word + "way"
        
    else:
        consonants = ""
        others = ""
        
        for i in word:
            if i in (VOWELS + "y"):
                others += i
            else: 
                consonants += i
        if isCap:
            pl = others[0].capitalize()+others[1:].lower + consonants.lower() + "ay"
            
        else: 
            pl = others + consonants.lower() + "ay"
            
        return pl